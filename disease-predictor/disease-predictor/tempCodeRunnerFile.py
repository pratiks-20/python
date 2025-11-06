import os
import io
import json
import uuid
from datetime import datetime
from flask import Flask, request, render_template, jsonify, session
from flask_cors import CORS
from google import genai
from google.genai import types
from PIL import Image
import secrets

# --- CONFIGURATION ---
# Use environment variables for security
GEMINI_API_KEY = os.environ.get('GEMINI_API_KEY', '')
UPLOAD_FOLDER = 'uploads'
HISTORY_FOLDER = 'history'
ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'webp', 'bmp'}
MAX_FILE_SIZE = 10 * 1024 * 1024  # 10MB

app = Flask(__name__)
app.secret_key = secrets.token_hex(16)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['MAX_CONTENT_LENGTH'] = MAX_FILE_SIZE
CORS(app)

# Create necessary folders
os.makedirs(UPLOAD_FOLDER, exist_ok=True)
os.makedirs(HISTORY_FOLDER, exist_ok=True)

# Initialize Gemini Client
try:
    client = genai.Client(api_key=AIzaSyD2XC4KgDsqSAKQZ7UqThewh4YIsnd_L24)
except Exception as e:
    print(f"Error initializing Gemini client: {e}")
    client = None

# --- UTILITY FUNCTIONS ---
def allowed_file(filename):
    """Checks if the file extension is allowed."""
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

def validate_image(file_path):
    """Validates that the file is a proper image."""
    try:
        img = Image.open(file_path)
        img.verify()
        return True
    except:
        return False

def save_to_history(prediction_data, image_filename):
    """Saves prediction history to JSON file."""
    history_file = os.path.join(HISTORY_FOLDER, 'predictions.json')
    
    history_entry = {
        'id': str(uuid.uuid4()),
        'timestamp': datetime.now().isoformat(),
        'image': image_filename,
        'prediction': prediction_data
    }
    
    try:
        if os.path.exists(history_file):
            with open(history_file, 'r') as f:
                history = json.load(f)
        else:
            history = []
        
        history.insert(0, history_entry)  # Add to beginning
        history = history[:50]  # Keep only last 50 predictions
        
        with open(history_file, 'w') as f:
            json.dump(history, f, indent=2)
    except Exception as e:
        print(f"Error saving history: {e}")

# --- GEMINI PREDICTION LOGIC ---
def get_image_prediction(image_path):
    """Calls Gemini API with enhanced medical analysis prompt."""
    if not client:
        return {"error": "AI Service Unavailable: Client initialization failed."}
    
    try:
        img = Image.open(image_path)
        
        # Enhanced medical analysis prompt
        prompt = [
            """You are an advanced AI medical imaging assistant specializing in diagnostic analysis. 
            Analyze this medical image (skin condition, X-ray, MRI, CT scan, etc.) with clinical precision.
            
            Provide:
            1. Primary diagnostic prediction with medical terminology
            2. Detailed visual analysis of key findings
            3. Confidence assessment
            4. Potential differential diagnoses (alternative possibilities)
            5. Recommended next steps for clinical evaluation
            6. Critical safety disclaimer
            
            Base your analysis on visible clinical features, patterns, morphology, and imaging characteristics.""",
            img,
            """Output as JSON with fields: 'disclaimer', 'primary_prediction', 'visual_rationale', 
            'confidence_score', 'differential_diagnoses' (array), 'recommended_actions' (array), 
            'severity_level' (Low/Moderate/High/Critical), 'urgency' (Routine/Urgent/Emergency)."""
        ]
        
        # Enhanced schema for comprehensive analysis
        diagnosis_schema = types.Schema(
            type=types.Type.OBJECT,
            properties={
                "disclaimer": types.Schema(
                    type=types.Type.STRING, 
                    description="Mandatory medical safety and legal disclaimer"
                ),
                "primary_prediction": types.Schema(
                    type=types.Type.STRING, 
                    description="Primary diagnostic prediction with medical terminology"
                ),
                "visual_rationale": types.Schema(
                    type=types.Type.STRING, 
                    description="Detailed clinical analysis of visual findings"
                ),
                "confidence_score": types.Schema(
                    type=types.Type.STRING, 
                    description="Confidence percentage (e.g., '85%')"
                ),
                "differential_diagnoses": types.Schema(
                    type=types.Type.ARRAY,
                    items=types.Schema(type=types.Type.STRING),
                    description="Alternative diagnostic possibilities"
                ),
                "recommended_actions": types.Schema(
                    type=types.Type.ARRAY,
                    items=types.Schema(type=types.Type.STRING),
                    description="Clinical recommendations and next steps"
                ),
                "severity_level": types.Schema(
                    type=types.Type.STRING,
                    description="Clinical severity: Low, Moderate, High, or Critical"
                ),
                "urgency": types.Schema(
                    type=types.Type.STRING,
                    description="Clinical urgency: Routine, Urgent, or Emergency"
                )
            },
            required=[
                "disclaimer", "primary_prediction", "visual_rationale", 
                "confidence_score", "differential_diagnoses", "recommended_actions",
                "severity_level", "urgency"
            ]
        )
        
        config = types.GenerateContentConfig(
            response_mime_type="application/json",
            response_schema=diagnosis_schema,
            temperature=0.2  # Balanced for clinical accuracy
        )
        
        response = client.models.generate_content(
            model='gemini-2.0-flash-exp',
            contents=prompt,
            config=config
        )
        
        return json.loads(response.text)
        
    except Exception as e:
        print(f"Gemini API Error: {e}")
        return {"error": f"Failed to get prediction: {str(e)}"}

# --- FLASK ROUTES ---
@app.route('/')
def index():
    """Renders the main application page."""
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    """Handles image upload and returns comprehensive prediction."""
    if 'file' not in request.files:
        return jsonify({"error": "No file uploaded"}), 400
    
    file = request.files['file']
    
    if file.filename == '':
        return jsonify({"error": "No file selected"}), 400
    
    if not allowed_file(file.filename):
        return jsonify({"error": "Invalid file type. Please upload PNG, JPG, JPEG, WEBP, or BMP"}), 400
    
    try:
        # Generate unique filename
        file_ext = file.filename.rsplit('.', 1)[1].lower()
        unique_filename = f"{uuid.uuid4()}.{file_ext}"
        filepath = os.path.join(app.config['UPLOAD_FOLDER'], unique_filename)
        
        # Save and validate file
        file.save(filepath)
        
        if not validate_image(filepath):
            os.remove(filepath)
            return jsonify({"error": "Invalid image file"}), 400
        
        # Get AI prediction
        prediction_result = get_image_prediction(filepath)
        
        if "error" not in prediction_result:
            # Save to history
            save_to_history(prediction_result, unique_filename)
        
        # Clean up uploaded file
        try:
            os.remove(filepath)
        except:
            pass
        
        if "error" in prediction_result:
            return jsonify(prediction_result), 500
        
        return jsonify(prediction_result)
        
    except Exception as e:
        return jsonify({"error": f"Server error: {str(e)}"}), 500

@app.route('/history', methods=['GET'])
def get_history():
    """Returns prediction history."""
    history_file = os.path.join(HISTORY_FOLDER, 'predictions.json')
    
    try:
        if os.path.exists(history_file):
            with open(history_file, 'r') as f:
                history = json.load(f)
            return jsonify(history)
        return jsonify([])
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route('/stats', methods=['GET'])
def get_stats():
    """Returns usage statistics."""
    history_file = os.path.join(HISTORY_FOLDER, 'predictions.json')
    
    try:
        if os.path.exists(history_file):
            with open(history_file, 'r') as f:
                history = json.load(f)
            
            stats = {
                'total_predictions': len(history),
                'recent_predictions': len([h for h in history if 
                    (datetime.now() - datetime.fromisoformat(h['timestamp'])).days < 7])
            }
            return jsonify(stats)
        return jsonify({'total_predictions': 0, 'recent_predictions': 0})
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.errorhandler(413)
def too_large(e):
    return jsonify({"error": "File too large. Maximum size is 10MB"}), 413

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
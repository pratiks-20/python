from django.shortcuts import render
import re

def login_view(request):
    message = ""
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")

        # Regex for username: only letters and numbers
        if not re.match(r"^[A-Za-z0-9]+$", username):
            message = "Invalid username! Only letters and numbers allowed."
        elif password != "admin123":
            message = "Incorrect password!"
        else:
            message = "Login successful ✅"
            
    return render(request, "login.html", {"message": message})

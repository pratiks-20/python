import os

cwd = os.getcwd()
print("Current directory:", cwd)

print("Contents:", os.listdir(cwd))

os.makedirs('example_dir', exist_ok=True)
os.rename('example_dir', 'renamed_dir')


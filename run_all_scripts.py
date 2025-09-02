import os
import subprocess

# Directory containing the scripts (current directory)
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))

# Find all Python files except this runner script
python_files = [
    f for f in os.listdir(SCRIPT_DIR)
    if f.endswith('.py') and f != os.path.basename(__file__)
]

for script in python_files:
    try:
        result = subprocess.run(["python3", script], capture_output=True, text=True, check=True)
        print(result.stdout, end="")
    except subprocess.CalledProcessError as e:
        print(e.stdout or "", end="")
        print(e.stderr or "", end="")

ptint("hello")
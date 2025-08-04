"""
This script installs requirements from python_test_elevate_core/requirements.txt
and can be extended to install other dependencies as needed.
"""
import subprocess
import sys
import os

# Build the path to requirements.txt in python_test_elevate_core
core_req_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'Rheem_core', 'requirements.txt'))
sys.path.append(os.path.dirname(core_req_path))
# Install requirements from core
try:
    subprocess.check_call([
        sys.executable, '-m', 'pip', 'install', '-r', core_req_path
    ])
    print(f"Installed requirements from {core_req_path}.")
except subprocess.CalledProcessError as e:
    print(f"Failed to install requirements from {core_req_path}. Error: {e}")

rheem_utilities_path = os.path.abspath(os.path.dirname(__file__))
sys.path.append(rheem_utilities_path)
print(sys.path,"Rheem_Utlities_path added to sys.path")  # Print sys.path for debugging

import subprocess
import sys
import os

# Build the path to python_test_elevate_utilities
utilities_setup_script = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'Rheem_utilities', 'setup_utilities.py'))
utilities_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'Rheem_utilities'))

# Run setup_utilities.py to install requirements from core
subprocess.check_call([sys.executable, utilities_setup_script])

# Install python_test_elevate_utilities in editable mode
subprocess.check_call([sys.executable, '-m', 'pip', 'install', '-e', utilities_path])
subprocess.check_call([sys.executable, '-m', 'playwright', 'install'])
print(f"Installed {utilities_path} in editable mode.")
rheem_web_path = os.path.abspath(os.path.dirname(__file__))
sys.path.append(rheem_web_path)
print(sys.path,"Rheem_web_path added to sys.path ")  # Print sys.path for debugging

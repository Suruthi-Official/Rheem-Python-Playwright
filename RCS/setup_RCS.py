import subprocess
import sys
import os


# # Path to setup_web.py in Rheem_web
web_setup_script = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'Rheem_web', 'setup_web.py'))

# # Path to each folders
utilities_setup_script = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'Rheem_utilities'))
rheem_web_setup_script = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'Rheem_web'))
RCS_path = os.path.abspath(os.path.dirname(__file__))

# # Run setup_web.py to link rheem_utilities to rheem_web
subprocess.check_call([sys.executable, web_setup_script])

# # Install RCS in editable mode
RCS_path = os.path.abspath(os.path.dirname(__file__))
print(f"RCS path: {RCS_path}")
# subprocess.check_call([sys.executable, '-m', 'pip', 'install', '-e', RCS_path])

# # Set the PYTHONPATH environment variable permanently
current_pythonpath = os.environ.get('PYTHONPATH', '')
print(f"Current PYTHONPATH: {current_pythonpath}")
path_to_add= RCS_path+";"+rheem_web_setup_script+";"+utilities_setup_script

if path_to_add not in current_pythonpath or current_pythonpath == '':
    print(f"Adding {path_to_add} to PYTHONPATH.")
    new_pythonpath = f"{path_to_add};{current_pythonpath}"
    subprocess.run(["setx", "PYTHONPATH", new_pythonpath, "/m"])
    print(f"Updated PYTHONPATH: {new_pythonpath}")


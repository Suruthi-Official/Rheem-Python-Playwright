import json
import os
from Rheem_utilities.utils.constants import Constants

def load_config():
    with open(Constants.CONFIG_PATH, 'r') as f:
        return json.load(f)
    
def load_constants():
    with open(Constants.CONSTANTS_PATH, 'r') as f:
        return json.load(f)    
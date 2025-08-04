import os
from configparser import ConfigParser
from sys import path as sys_path
from Rheem_utilities.utils.constants import Constants


class WebConstants:
    """
    Loads and provides access to web framework configuration constants.
    Reads from a properties file (INI format).
    """
    properties = {}
    with open(Constants.WEB_PROP_PATH, 'r') as file:
        for line in file:
            line = line.strip()
            if line and not line.startswith('#'):  # Ignore empty lines and comments
                key, value = line.split('=', 1)
                properties[key.strip()] = value.strip()

#     """
#     Loads properties from the web.properties file and sets class attributes.
#     """
BROWSER_TYPE = WebConstants.properties['browser'].upper()
REPORT_ENABLED = WebConstants.properties['reports'].lower() == "true"
BROWSER_QUIT = WebConstants.properties['browser.quit'].lower() == "true"
BROWSER_HEADLESS = WebConstants.properties['browser.headless'].lower() == "true"
BROWSER_MAXIMIZE = WebConstants.properties['browser.maximize'].lower() == "true"
STEPWISE_SCREENSHOT = WebConstants.properties['stepwise.screenshot'].lower() == "true"
DESKTOP_SCREENSHOT = WebConstants.properties['desktop.screenshot'].lower() == "true"
PAGE_OBJECT_TYPE = WebConstants.properties['page.object.type'].lower()
DEFAULT_WAIT_TIME_SEC = int(WebConstants.properties['default.wait.time.sec'])
IMPLICIT_WAIT_TIME_SEC = int(WebConstants.properties['implicit.wait.time.sec'])
LOG_LEVEL = WebConstants.properties['log.level'].upper()
ENVIRONMENT = WebConstants.properties['environment'].lower()


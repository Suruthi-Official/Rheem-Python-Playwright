import os
import configparser

class Constants:
    """
    The Constants class provides various static constants and utility methods used across the framework.
    It loads configuration properties from the 'tep.properties' file and provides paths for resources, input/output data, and browser settings.
    """
    # The base path of the current project directory.
    BASE_PATH = os.getcwd()
    # BASE_PATH = os.path.abspath(os.path.dirname(__file__))

    # The file separator for the current operating system.
    FILE_SEPARATOR = os.sep

    # The path to the PageObjects directory, which contains the page object model files.
    PAGE_OBJECTS_PATH = os.path.join(BASE_PATH, "page_objects")

    # The path to the resources directory, which contains configuration files and other resources.
    RESOURCES_PATH = os.path.join(BASE_PATH, "resources")

    # The path to the 'web.properties' configuration file.
    WEB_PROP_PATH = os.path.join(BASE_PATH, "resources", "web.properties")

    # The path to the 'api.properties' configuration file.
    API_PROP_PATH = os.path.join(BASE_PATH, "resources", "api.properties")

    # The path to the 'database.properties' configuration file.
    DB_PROP_PATH = os.path.join(BASE_PATH, "resources", "database.properties")

     # The path to the application configuration file.
    CONFIG_PATH = os.path.join(BASE_PATH, "config.json")

    # The path to the application constants file.
    CONSTANTS_PATH= os.path.join(BASE_PATH, "constants.json")

    # The path to the application log file.
    LOG_PATH = os.path.join(BASE_PATH,"logs", "results.log")
    # Load properties from the 'tep.properties' file
    # TEP_PROPERTIES = configparser.ConfigParser()
    # if os.path.exists(TEP_PROP_PATH):
    #     TEP_PROPERTIES.read(TEP_PROP_PATH)
    #     # configparser expects sections, so we use a workaround for Java-style .properties files
    #     with open(TEP_PROP_PATH) as f:
    #         props = dict(line.strip().split('=', 1) for line in f if '=' in line and not line.strip().startswith('#'))
    # else:
    #     props = {}

    # The path to the test application directory, loaded from the 'tep.properties' file.
    # TEST_APP_PATH = os.path.join(TEST_PATH, "resources", props.get("project.name", ""))

    # The path to the 'features' directory inside the test application, loaded from the 'tep.properties' file.
    # TEST_APP_FEATURE_PATH = os.path.join(TEST_APP_PATH, "features")

    # The path to the test data input directory for web-related data, loaded from the 'tep.properties' file.
    # TEST_DATA_INPUT_PATH = os.path.join(TEST_APP_PATH, "input")

    # The path to the test data output directory for web-related results.
    # TEST_DATA_OUTPUT_PATH = os.path.join(TARGET_PATH, "output")
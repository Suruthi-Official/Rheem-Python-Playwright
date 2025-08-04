from utils import logger_utils
from Rheem_utilities.utils.constants import Constants

class NavigationMenu:
    
    log = logger_utils.LoggerUtils(name=__name__, log_file=Constants.LOG_PATH)

    def __init__(self, driver, selectors):
        self.driver = driver
        self.selectors = selectors

    def click_menu_button(self):
        NavigationMenu.log.info("Clicking the menu button.")
        self.driver.click.click_element(self.selectors.get_menu_button())

    def click_device_management(self):
        NavigationMenu.log.info("Clicking Device Management in the navigation menu.")
        self.driver.click.click_element(self.selectors.get_device_management())



 


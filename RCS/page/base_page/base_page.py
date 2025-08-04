from RCS.page.login_page.login_page_selectors import LoginPageSelectors
from RCS.page.login_page.login_page import LoginPage
from RCS.page.site_details_page.site_details_page_selectors import SiteDetailsPageSelectors
from RCS.page.site_details_page.site_details_page import SiteDetailsPage
from RCS.page.navigation_menu.navigation_selectors import NavigationMenuSelector
from RCS.page.navigation_menu.navigation_menu import NavigationMenu
from RCS.page.device_management_page.device_management_page import DeviceManagementPage
from RCS.page.device_management_page.device_management_page_selectors import DeviceManagementPageSelectors

class BasePage:
    def __init__(self, driver):
        self.driver = driver
        self.login_page_selectors = LoginPageSelectors(driver)
        self.login_page = LoginPage(driver, self.login_page_selectors)
        self.siteDetailsPageSelectors = SiteDetailsPageSelectors(driver)
        self.siteDetailsPage = SiteDetailsPage(driver, self.siteDetailsPageSelectors)
        self.navigation_menu_selector = NavigationMenuSelector(driver)
        self.navigation_menu = NavigationMenu(driver, self.navigation_menu_selector)
        self.device_management_page_selectors = DeviceManagementPageSelectors(driver)
        self.device_management_page = DeviceManagementPage(driver, self.device_management_page_selectors)
       

        
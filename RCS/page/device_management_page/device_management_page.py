from utils import logger_utils
from Rheem_utilities.utils.constants import Constants
from RCS.page.navigation_menu.navigation_selectors import NavigationMenuSelector
class DeviceManagementPage:
    log = logger_utils.LoggerUtils(name=__name__, log_file=Constants.LOG_PATH)

    def __init__(self, driver, selectors):
        self.driver = driver
        self.selectors = selectors

    # def search_device_management_page(self):
    #     page = self.driver  

    #     # Wait for search box to be present and clickable
    #     page.playWrightWaits.wait_for_element(self.selectors.get_device_management_search(), timeout=5000)
    #     page.playWrightWaits.wait_for_element(self.selectors.get_site_address(), timeout=15000)
    #     page.playWrightWaits.sleep(15)
    #     # Search by address
    #     address_elements = self.driver.get_elements(self.selectors.site_address)
    #     print("Address Elements:", address_elements)
    #     for address_element in address_elements:
    #         # address_text = page.text(context =address_element)
    #         # print(address_text)
    #         page.fill.fill_text(self.selectors.get_device_management_search(), address_text)
    #         assert page.inner_text(self.selectors.get_site_address()) == address_text
    #         page.fill.fill_text(self.selectors.get_device_management_search(), "")
    #         break

    #     # Search by device name
    #     device_elements = self.driver.get_elements(self.selectors.device_name)
    #     for _ in device_elements:
    #         page.fill.fill_text(self.selectors.get_device_management_search(), "Gen")
    #         page.fill.fill_text(self.selectors.get_device_management_search(), "")

    #         # Search by MAC ID
    #         page.click.click_element(self.selectors.get_site_card())
    #         mac_id = page.text(self.selectors.get_search_mac_id())
    #         print(mac_id)

    #         page.click.click_element(NavigationMenuSelector.get_menu_button())
    #         page.click.click_element(self.selectors.get_device_management())
    #         page.wait_for_timeout(5000)

    #         assert page.is_visible(self.selectors.SEARCH)
    #         page.fill.fill_text(self.selectors.get_device_management_search(), mac_id)
    #         page.fill.fill_text(self.selectors.get_device_management_search(), "")
    #         break

    #     # Search for an invalid term
    #     page.fill_text(self.selectors.get_device_management_search(), "Search")
    #     assert page.text(self.selectors.get_error_search()) == Constants.ERROR_SEARCH
    #     page.fill_text(self.selectors.get_device_management_search(), "")

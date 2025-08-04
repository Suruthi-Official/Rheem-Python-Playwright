from utils import logger_utils
from Rheem_utilities.utils.constants import Constants
import allure

class SiteDetailsPage:
    
    log = logger_utils.LoggerUtils(name=__name__, log_file=Constants.LOG_PATH)

    def __init__(self, driver, selectors):
        self.driver = driver
        self.selectors = selectors

    def verify_status_overview_section(self):
        allure.attach("Action - Verify Status OverView Section", name="Status OverView", attachment_type=allure.attachment_type.TEXT) 
        SiteDetailsPage.log.info("Starting verification of the status overview section.")
        
        self.driver.playWrightWaits.wait_for_element(self.selectors.site_details_table, timeout=15000)
        SiteDetailsPage.log.debug("Waited for the status overview table to befrom RCS.page.site_details_page.site_details_page_selectors import visible.")

        rows = self.driver.get_elements(self.selectors.site_details_table)
        self.driver.allure_report.allure_screenshot(execute=True)

        assert len(rows) > 0, "No data visible in the status overview section."
        SiteDetailsPage.log.debug(f"Number of rows found: {len(rows)}")

        for row in rows:
            third_data_cell = self.driver.get_element(self.selectors.third_data_cell, context=row)
            if third_data_cell:
                SiteDetailsPage.log.debug("Clicking on the third data cell.")
                third_data_cell.click()
            else:
                self.driver.allure_report.allure_screenshot(execute=True)
                SiteDetailsPage.log.warning("Third data cell not found in the current row.")

    def click_clear_selection_button(self):
        allure.attach("Action - Verify Clear Selection", name="Clear Selection", attachment_type=allure.attachment_type.TEXT) 
        if self.driver.getElementStatus.is_displayed(self.selectors.get_clear_selection_button()):
            SiteDetailsPage.log.info("Clicking the clear selection button.")
            self.driver.click.click_element(self.selectors.get_clear_selection_button())
        else:
            self.driver.allure_report.allure_screenshot(execute=True)
            SiteDetailsPage.log.warning("Clear selection button is not displayed.")

    def click_sign_out(self):
        allure.attach("Action - Sign Out", name="Sign Out", attachment_type=allure.attachment_type.TEXT) 
        if self.driver.getElementStatus.is_displayed(self.selectors.get_sign_out_button()):
            SiteDetailsPage.log.info("Clicking Sign out button.")
            self.driver.click.click_element(self.selectors.get_sign_out_button())
        else:
            self.driver.allure_report.allure_screenshot(execute=True)
            SiteDetailsPage.warning("Sign out button is not displayed.")

class SiteDetailsPageSelectors:
    site_details_table = "table tr"
    third_data_cell = "td:nth-child(3)"

    def __init__(self, driver):
        self.driver = driver

    def get_clear_selection_button(self):
        return self.driver.get_page().locator("//button[text()='Clear Selection']")

    def get_sign_out_button(self):
        return self.driver.get_page().locator("//button[text()='Sign Out']")

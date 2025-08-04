class NavigationMenuSelector:
    def __init__(self, driver):
        self.driver = driver
        self.log = driver.logger
        self.allure_report = driver.allure_report

    def get_menu_button(self):
        return self.driver.get_page().locator("//button[@aria-label='menu']")
    
    def get_device_management(self):
        return self.driver.get_page().locator("//span[text()='Device Management']")


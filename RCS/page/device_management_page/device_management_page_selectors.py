class DeviceManagementPageSelectors:

    def __init__(self, driver):
        self.driver = driver
        self.site_address = "(//label[contains(text(),'Site')]/following-sibling::div//span)[1]"
        self.device_name = "//div[contains(@class,'truncate-text truncate-2')]//span[@class='truncate-links']"
    
    def get_device_management_search(self):
        return self.driver.get_page().locator("//div[contains(@class, 'site-list-container')]//input[@placeholder='Search']")
       
    def get_site_address(self): 
        return self.driver.get_page().locator("(//label[contains(text(),'Site')]/following-sibling::div//span)[1]")

    def get_site_card(self):
        return self.driver.get_page().locator("//div[@class='truncate-text truncate-2']//span[@class='truncate-links']")  
    
    def get_search_mac_id(self):
        return self.driver.get_page().locator("//span[label='MAC Address']/div")
    
    def get_device_management(self):
        return self.driver.get_page().locator("//span[@class='MuiTypography-root MuiTypography-body1 MuiListItemText-primary css-yb0lig']")
    
    def get_error_search(self):
        return self.driver.get_page().locator("//div[text()='No devices available at this organization.']")
    
    def get_device_name(self):
        return self.driver.get_page().locator("//div[contains(@class,'truncate-text truncate-2')]//span[@class='truncate-links']")
class LoginPageSelectors:
    def __init__(self, driver):
        self.driver = driver

    def get_selectRole(self):
        return self.driver.get_page().locator("//div[@id='mui-component-select-role']")

    def get_selectRoledropdown(self):
        return self.driver.get_page().locator("//li[@data-value='property_facility_manager']")

    def get_email_input(self):
        return self.driver.get_page().locator("//input[@name='email']")

    def get_password_input(self):
        return self.driver.get_page().locator("//input[@name='password']")

    def get_login_button(self):
        return self.driver.get_page().locator("//button[@type='submit']")

    def get_error_message(self):
        return self.driver.get_page().locator("//div[@class='MuiAlert-message']")

# class LoginPageSelectors:

#     def get_selectRole(driver):
#         """
#         returns the locator for the role selection dropdown on the login page.
#         """
#         return driver.get_page().locator("//div[@id='mui-component-select-role']")
    
#     def get_selectRoledropdown(driver):
#         return driver.get_page().locator("//li[@data-value='property_facility_manager']")

#     def get_email_input(driver):
#         """
#         Returns the locator for the email input field on the login page.
#         """
#         return driver.get_page().locator("//input[@name='email']")
    
#     def get_password_input(driver):
#         """
#         Returns the locator for the password input field on the login page.
#         """
#         return driver.get_page().locator("//input[@name='password']")
    
#     def get_login_button(driver):
#         """
#         Returns the locator for the login button 
#         """
    
#         return driver.get_page().locator("//button[@type='submit']")
    
#     def get_error_message(driver):
#         """
#         Returns the locator for the error message on the login page.
#         """
#         return driver.get_page().locator("//div[@class='MuiAlert-message']")

 






# from Rheem_web.web.WebAppDriver import WebAppDriver
# class login_page_selectors:

#     """Selectors for the login page elements."""
#     selectRole = "//div[@id='mui-component-select-role']"
#     selectRoledropdown = "//li[@data-value='property_facility_manager']"
#     usernameInput = "//input[@name='email']"
#     passwordInput = "//input[@name='password']"
#     loginButton = "//button[@type='submit']"
#     error_messsage = "//div[@class='MuiAlert-message']"

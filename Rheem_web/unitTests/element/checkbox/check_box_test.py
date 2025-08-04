import time
from web import web_app_driver

def test_ActionCheckBox():
    driver = web_app_driver.WebAppDriver()
    driver.browser_event.go_to_url("https://practice-automation.com/form-fields/")
    checkbox_selector = "#drink1"
    driver.actionCheckBox.check(checkbox_selector)
    assert driver.actionCheckBox.is_checked(checkbox_selector), "Checkbox should be checked"
    driver.quit()

def test_javaScriptCheckbox():
    driver = web_app_driver.WebAppDriver()    
    driver.browser_event.go_to_url("https://practice-automation.com/form-fields/")
    checkbox_selector = "#drink1"
    driver.javaScriptCheckBox.uncheck(checkbox_selector)
    # Verify checkbox is unchecked
    assert not driver.javaScriptCheckBox.is_checked(checkbox_selector), "Checkbox should be unchecked"
    driver.quit()


test_javaScriptCheckbox()
   
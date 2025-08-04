from sys import path as sys_path
sys_path.append('../')
from web import web_app_driver

def test_tab_event():
    driver = web_app_driver.WebAppDriver()
    driver.browser_event.go_to_url("https://www.w3schools.com")

    # Open a new tab
    driver.tabEvent.create_new("https://playwright.dev")
    # Switch to the new tab
    assert driver.get_page_url() == "https://playwright.dev/"  # Check if the new tab opened correctly

    # Close the current tab
    driver.tabEvent.close_current_tab()

    # Switch back to the original tab
    driver.tabEvent.switch_to_first_tab()
    assert driver.get_page_url() == "https://www.w3schools.com/"  # Verify we are back on the original tab

    driver.quit()

test_tab_event()
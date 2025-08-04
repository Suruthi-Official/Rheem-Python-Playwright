from sys import path as sys_path
sys_path.append('../')
from web import web_app_driver

def test_window_event():
    driver = web_app_driver.WebAppDriver()
    driver.browser_event.go_to_url("https://www.w3schools.com")

    # Open a new window
    driver.windowEvent.create_new_window("https://playwright.dev")
    # Switch to the new window
    assert driver.get_page_url() == "https://playwright.dev/"  # Check if the new window opened correctly

    # Close the current window
    driver.windowEvent.close_current_window()

    # Switch back to the original window
    driver.windowEvent.switch_to_old_window()
    assert driver.get_page_url() == "https://www.w3schools.com/"  # Verify we are back on the original window

    driver.quit()

test_window_event()
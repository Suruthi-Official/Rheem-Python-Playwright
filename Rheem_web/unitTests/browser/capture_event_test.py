from sys import path as sys_path
sys_path.append('../')
from web import web_app_driver

def test_capture_event():
    driver = web_app_driver.WebAppDriver()
    driver.browser_event.go_to_url("https://www.w3schools.com")
    # Capture the screenshot
    driver.captureEvent.capture_screenshot()
    # Capture the Desktop screenshot
    driver.captureEvent.capture_desktop_screenshot()

    driver.quit()


test_capture_event()
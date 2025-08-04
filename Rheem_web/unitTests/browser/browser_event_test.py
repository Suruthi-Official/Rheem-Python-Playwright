from sys import path as sys_path
sys_path.append('../')
from web import web_app_driver


def test_navigation():
    driver = web_app_driver.WebAppDriver()
    driver.browser_event.go_to_url("https://example.com")
    assert driver.get_page_url() == "https://example.com/" #"Navigation to URL failed"
    driver.browser_event.back()
    driver.browser_event.go_to_url("https://www.w3schools.com")
    assert driver.get_page_url() != "https://example.com"# "Back navigation failed"
    driver.browser_event.forward()
    assert driver.get_page_url() != "https://example.com"# "Forward navigation failed"
    driver.browser_event.refresh()
    print(driver.get_page_url())
    assert driver.get_page_url() == "https://www.w3schools.com/"# "Page refresh failed"
    driver.quit()


test_navigation()

from sys import path as sys_path
sys_path.append('../')
from web.config import web_enums
from web.base import playwright_driver


def test_example():
    driver = playwright_driver.PlayWrightDriver()
    driver.launch_browser()
    driver.open_url("https://example.com")
    driver.close_browser()

def test_example_browser_input():
    driver = playwright_driver.PlayWrightDriver()
    driver.launch_browser(web_enums.BrowserType.CHROME.name)
    driver.open_url("https://example.com")
    driver.close_browser()

test_example()
from sys import path as sys_path
sys_path.append('../')
from web import web_app_driver

def test_window_manipulation():
    driver = web_app_driver.WebAppDriver()
    driver.browser_event.go_to_url("https://www.w3schools.com")

    driver.windowManipulation.resize_browser(650, 480)
    driver.windowManipulation.zoom_in_out("ADD")
    driver.windowManipulation.maximize_browser()

    print(driver.pageObjects.get("EY.searchBox"))
    driver.quit()

test_window_manipulation()

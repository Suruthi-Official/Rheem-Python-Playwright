import pytest
from web.web_app_driver import WebAppDriver
from RCS.page.base_page.base_page import BasePage

@pytest.fixture(scope="session")
def webAppDriver():
    """
    Fixture to initialize the Playwright driver.
    """
    driver = WebAppDriver()
    yield driver
    driver.quit()

@pytest.fixture(scope="session")
def base_page(webAppDriver): 
    return BasePage(webAppDriver)

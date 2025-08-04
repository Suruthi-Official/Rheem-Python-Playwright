import os
from pytest_bdd import given, scenarios ,parsers ,then,when
from RCS.utils.config_util import load_config,load_constants
# from RCS.page.login_page.login_page import LoginPage


config = load_config()
constants = load_constants()

scenarios(os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "features", "login.feature")))

@given("I launch the url")
def launch_url(base_page):
     base_page.login_page.launch_url()


@given(parsers.parse("I login as {ROLE}"))
def login(base_page, ROLE):
    base_page.login_page.login(ROLE)

@when("I navigate to Site Management page")
def navigate_to_site_management_page(webAppDriver):
     webAppDriver.browser_event.wait_for_url_load(constants["SITE_DETAILS_URL"])
     try:
        assert webAppDriver.get_page_url() == constants["SITE_DETAILS_URL"]
        webAppDriver.logger.info("Site Details page is opened successfully")
     except AssertionError as exception:
            raise exception 


@then("I verify whether Status overview section is displayed")  
def verify_status_overview_section(base_page):
     base_page.siteDetailsPage.verify_status_overview_section()
     base_page.siteDetailsPage.click_clear_selection_button()
     base_page.siteDetailsPage.click_sign_out()
    
@when("I navigate to Device Management page")
def navigate_to_device_management_page(base_page,webAppDriver):
    base_page.navigation_menu.click_menu_button()
    base_page.navigation_menu.click_device_management()
    try:
        assert webAppDriver.get_page_url() == constants["DEVICE_MANAGEMENT_URL"]
        webAppDriver.logger.info("Device Management page is opened successfully")
    except AssertionError as exception:
        raise exception

@then("I verify whether Search functionality is working fine")
def verify_search_functionality(base_page):
     base_page.device_management_page.search_device_management_page()
   
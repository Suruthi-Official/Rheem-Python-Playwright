from utils import logger_utils
from Rheem_utilities.utils.constants import Constants
import allure
from web.config import web_constants
from RCS.utils.config_util import load_config, load_constants
import sys
from Rheem_web.web.trace.trace_logs import Trace_logs

config = load_config()
constants = load_constants()

class LoginPage:
    
    log = logger_utils.LoggerUtils(name=__name__, log_file=Constants.LOG_PATH)

    def __init__(self, driver, selectors):
        self.driver = driver
        self.selectors = selectors

    def launch_url(self):
        allure.attach("Action - Launch the URL", name="Launch_url", attachment_type=allure.attachment_type.TEXT) 
        self.driver.browser_event.go_to_url(constants["APPLICATION_URL"])
        try:
            assert self.driver.get_page_url() == constants["APPLICATION_URL"]
            LoginPage.log.info("Application is Launched successfully") 
        except AssertionError as exception:
            raise exception 

    @Trace_logs.trace_test("login")
    def login(self,ROLE):
        allure.attach("Action - Login the application", name="Login", attachment_type=allure.attachment_type.TEXT)
        username = config[web_constants.ENVIRONMENT][ROLE]["username"]
        password = config[web_constants.ENVIRONMENT][ROLE]["password"]

        self.driver.click.click_element(self.selectors.get_selectRole())
        self.driver.click.click_element(self.selectors.get_selectRoledropdown())
        self.driver.fill.fill_text(self.selectors.get_email_input(), username)
        self.driver.fill.fill_text(self.selectors.get_password_input(), password)
        self.driver.click.click_element(self.selectors.get_login_button())   
        self.driver.allure_report.allure_screenshot(execute=True)

        assert self.driver.getElementStatus.is_displayed(self.selectors.get_login_button()), "Login failed"

        try:
            self.driver.browser_event.wait_for_url_load(constants["SITE_DETAILS_URL"])
            LoginPage.log.info(f"Log in as {ROLE} is successful ")
        except:
            self.driver.getElementStatus.is_displayed(self.selectors.get_error_message())
            self.driver.allure_report.allure_screenshot(execute=True)
            LoginPage.log.info(f"Log in failed for {ROLE} ")
            sys.exit(1)

    @Trace_logs.trace_test("login_with_nonPageObjectModel")
    def login_with_nonPageObjectModel(self, ROLE):
        allure.attach("Action - Login the application", name="Login", attachment_type=allure.attachment_type.TEXT) 
        username = config[web_constants.ENVIRONMENT][ROLE]["username"]
        password = config[web_constants.ENVIRONMENT][ROLE]["password"]

        self.driver.click.click_element("LoginPage.selectRole")
        self.driver.click.click_element("LoginPage.selectRoledropdown")
        self.driver.fill.fill_text("LoginPage.usernameInput", username)
        self.driver.fill.fill_text("LoginPage.passwordInput", password)
        self.driver.click.click_element("LoginPage.loginButton")   
        self.driver.allure_report.allure_screenshot(execute=True)

        assert self.driver.getElementStatus.is_displayed(self.selectors.get_login_button()), "Login failed"

        try:
            self.driver.browser_event.wait_for_url_load(constants["SITE_DETAILS_URL"])
            LoginPage.log.info(f"Log in as {ROLE} is successful ")
        except:
            self.driver.getElementStatus.is_displayed(self.selectors.get_error_message())
            self.driver.allure_report.allure_screenshot(execute=True)
            LoginPage.log.info(f"Log in failed for {ROLE} ")
            sys.exit(1)

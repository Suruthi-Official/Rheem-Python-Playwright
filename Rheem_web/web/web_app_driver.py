from web.base import playwright_driver
from web.browser import window_scrolling
from web.element.checkbox import javascript_checkbox
from Rheem_web.web.element.fill import fill
from Rheem_web.web.element.click import click
from Rheem_web.web.element.dropdown import Dropdown, action_dropdown
from web.browser import browser_event, capture_event, tab_event, window_event, window_manipulation
from web.element.checkbox import checkbox
from web.element.click import javascript_click
from web.element.fill import fill_keys, javascript_fill
from web.element.getter import get_element_status
from web.base import playwright_waits
from utils import logger_utils
from Rheem_web.web.allure import allure_report
from Rheem_web.web.trace import trace_logs
from Rheem_web.web.config import web_constants
from web.config import page_objects


class WebAppDriver:


    def __init__(self):
        """
        Initialize the WebAppDriver instance.

        This constructor initializes the PlayWrightDriver and launches the browser.
        It also sets up various event handlers and utility classes for interacting with web elements.
        """
        self.playwrightdriver = playwright_driver.PlayWrightDriver()  # Initialize PlayWrightDriver instance
        self.page = self.playwrightdriver.launch_browser()  # Launch the browser when WebAppDriver is initialized
        self.playwrightdriver.maximize_window()  # Maximize the browser window
        self.browser_event = browser_event.BrowserEvent(self.playwrightdriver)
        self.captureEvent = capture_event.CaptureEvent(self.playwrightdriver)
        self.windowEvent = window_event.WindowEvent(self.playwrightdriver)
        self.tabEvent = tab_event.TabEvent(self.playwrightdriver)
        self.windowManipulation = window_manipulation.WindowManipulation(self.playwrightdriver)
        self.windowScrolling = window_scrolling.WindowScrolling(self.playwrightdriver)
        self.actionCheckBox = checkbox.ActionCheckBox(self.playwrightdriver)  # Initialize ActionCheckBox with the driver
        self.javaScriptCheckBox = javascript_checkbox.JavaScriptCheckBox(self.playwrightdriver)  # Initialize JavaScriptCheckBox with the driver
        self.fill = fill.Fill(self.playwrightdriver)  # Initialize Fill with the driver
        self.javaScriptFill = javascript_fill.JavaScriptFill(self.playwrightdriver)  # Initialize JavaScriptFill with the driver
        self.fill_keys = fill_keys.Fill_keys(self.playwrightdriver)  # Initialize PlaywrightFill with the driver
        self.click = click.Click(self.playwrightdriver)  # Initialize Click with the driver
        self.javaScriptClick = javascript_click.JavaScriptClick(self.playwrightdriver)  # Initialize JavaScriptClick with the driver
        self.dropdown = Dropdown.Dropdown(self.playwrightdriver)
        self.getElementStatus = get_element_status.GetElementStatus(self.playwrightdriver)  # Initialize GetElement with the driver
        self.playWrightWaits = playwright_waits.PlayWrightWaits(self.playwrightdriver)  # Initialize PlayWrightDriver instance
        self.logger = logger_utils.LoggerUtils(name=__name__,level=web_constants.LOG_LEVEL)
        self.allure_report=allure_report.Allure_report(self.playwrightdriver)
        self.trace_logs=trace_logs.Trace_logs(self.playwrightdriver)
        

    def get_page(self):
        """
        Get the current page instance.

        Returns:
            Page: The current page instance managed by PlayWrightDriver.
        """
        return self.playwrightdriver.page

    def set_page(self, page):
        """
        Set the current page instance.

        Args:
            page: The page instance to set for the PlayWrightDriver.
        """
        self.playwrightdriver.page = page

    def quit(self):
        """
        Close the browser.

        This method will close the browser using the PlayWrightDriver instance if a page is currently open.
        """
        if self.page:
            self.playwrightdriver.close_browser()  # Close the browser using PlayWrightDriver

    def get_page_url(self):
        """
        Returns the current URL of the page.

        Returns:
            str: The URL of the current page, or None if no page is open.
        """
        return self.playwrightdriver.page.url if self.playwrightdriver.page else None
    
    def get_locator(self, obj):
        """
        Returns a Locator for the given object (selector or Locator).
        """
        if isinstance(obj, str):
            return self.playwrightdriver.page.locator(obj)
        return obj

    def get_page_title(self):
        """
        Returns the current title of the page.

        Returns:
            str: The title of the current page, or None if no page is open.
        """
        return self.playwrightdriver.page.title() if self.playwrightdriver.page else None

    def get_elements(self, locator: str):
        """
        Get all elements matching the specified locator.

        Args:
            locator: The CSS selector for the elements to retrieve.

        Returns:
            list: A list of elements matching the locator.
        """
        return self.playwrightdriver.page.query_selector_all(locator)

    def get_element(self, locator: str, context=None):
        """
        Get a single element matching the specified locator.

        Args:
            locator: The CSS selector for the element to retrieve.
            context: Optional; a context within which to search for the element.

        Returns:
            Element: The first element matching the locator.

        Raises:
            Exception: If the element is not found or the page is not ready.
        """
        # self.playwrightdriver.page.wait_for_selector(locator)
        if context:
            return context.query_selector(locator)
        
        return self.playwrightdriver.page.query_selector(locator)
    
    def _get_locator(self, obj):
        """
        Returns a Locator for the given object (selector or Locator).
        """
        if isinstance(obj, str):
            return self.playwrightdriver.get_element(page_objects.PageObjects().get(obj)[0],page_objects.PageObjects().get(obj)[1])
        return obj    
    
    

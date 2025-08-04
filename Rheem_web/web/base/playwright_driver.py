from playwright.sync_api import sync_playwright
from web.config import web_enums
from utils import logger_utils
from Rheem_utilities.utils.constants import Constants
from web.config.page_objects import PageObjects
from web.config import web_constants

class PlayWrightDriver:
    
    log = logger_utils.LoggerUtils(name=__name__)

    def __init__(self):
        """
        Initialize the PlayWrightDriver instance.

        """
        self.browser_type = None
        self.browser_value = None
        self.browser = None
        self.context = None
        self.page = None
        self.playwright = None

    def launch_browser(self, browser_type=None):
        """
        Launch the specified browser.

        Args:
            browser_type: Optional; the type of browser to launch. If not provided, defaults to the browser type defined in WebConstants.

        Returns:
            page: The newly created page instance for further interactions.
        """
        self.browser_type = browser_type.upper() if browser_type else web_constants.BROWSER_TYPE
        if self.browser_type == web_enums.BrowserType.CHROME.name:
            self.browser_value = web_enums.BrowserType.CHROME.value
        elif self.browser_type == web_enums.BrowserType.FIREFOX.name:
            self.browser_value = web_enums.BrowserType.FIREFOX.value
        elif self.browser_type == web_enums.BrowserType.EDGE.name:
            self.browser_value = web_enums.BrowserType.EDGE.value
        elif self.browser_type == web_enums.BrowserType.SAFARI.name:
            self.browser_value = web_enums.BrowserType.SAFARI.value
        elif self.browser_type == web_enums.BrowserType.CHROME_CANARY.name:
            self.browser_value = web_enums.BrowserType.CHROME_CANARY.value

        self.playwright = sync_playwright().start()  # Start Playwright
        self.browser = self.playwright[self.browser_value].launch(headless=web_constants.BROWSER_HEADLESS)
        self.context = self.browser.new_context()  # Create a new context
        page = self.context.new_page()  # Create a new page within the context
        self.page = page
        PlayWrightDriver.log.info(f"{self.browser_value} is Launched")
        self.maximize_window()
        return page  # Return self for chaining

    def maximize_window(self):
        """
        Maximize the browser window to the current viewport size.
        """
        viewport_size = self.page.evaluate("() => ({ width: window.innerWidth, height: window.innerHeight })")
        self.page.set_viewport_size(viewport_size)

    def open_url(self, url):
        """
        Navigate to the specified URL.

        Args:
            url: The URL to open in the browser.
        """
        self.page.goto(url)

    def close_browser(self):
        """
        Close the browser and its context.
        """
        if self.context:
            self.context.close()  # Close the context if it exists
        if self.browser:
            self.browser.close()
            PlayWrightDriver.log.info("Browser is closed")
        else:
            self.stop_playwright()  # Stop Playwright after closing the browser

    def stop_playwright(self):
        """
        Stop the Playwright instance.
        """
        if self.playwright:
            self.playwright.stop()

    def get_page(self):
        """
        Get the current page instance.

        Returns:
            page: The current page instance.

        Raises:
            Exception: If no page is currently open.
        """
        if self.page:
            return self.page
        else:
            raise Exception("No page is currently open. Please launch a browser first.")
        
    
    def get_context(self):
        """
        Get the current browser context.

        Returns:
            context: The current browser context instance.

        Raises:
            Exception: If no context is currently available.
        """
        if self.context:
            return self.context
        else:
            raise Exception("No browser context is currently available. Please launch a browser first.")
        

    def get_page_title(self):
        """
        Get the title of the current page.

        Returns:
            str: The title of the current page.

        Raises:
            Exception: If no page is currently open.
        """
        if self.page:
            return self.page.title()
        else:
            raise Exception("No page is currently open. Please launch a browser first.")

    def get_element_po(self, locator: str):
        """
        Get an element from the current page using the specified locator.

        Args:
            locator: The locator string to find the element.

        Returns:
            element: The found element. 
        """
        return self.driver.query_selector(locator)

    def get_element_locator_string(self, element):
        """
        Get the locator string (outer HTML) of the specified element.

        Args:
            element: The element for which to get the locator string.

        Returns:
            str: The outer HTML of the element.
        """
        return element.evaluate("el => el.outerHTML")
    
    def get_locator(self, obj):
        """
        Returns a Locator for the given object (selector or Locator).
        :param obj: CSS selector (str) or Locator.
        :return: Locator
        """
        if isinstance(obj, str):
            return self.page.locator(obj)
        return obj

    # def _get_locator_po(self, obj):
    #     """
    #     Returns a Locator for the given object (selector or Locator).
    #     """
    #     if isinstance(obj, str):
    #         return self.playwrightdriver.get_element(PageObjects.PageObjects().get(obj))
    #     return obj
    
    def get_element(self, locator: str, value: str):
        element = None
        locator = locator.lower()  # Convert locator to lowercase for case-insensitive comparison

        if locator == "id":
            element = self.page.locator(f'#{value}')  # Using CSS selector for ID
        elif locator == "name":
            element = self.page.locator(f'[name="{value}"]')  # Using attribute selector for name
        elif locator == "xpath":
            element = self.page.locator(f'xpath={value}')  # Using XPath selector
        elif locator == "css":
            element = self.page.locator(value)  # Directly using CSS selector
        elif locator == "tagname":
            element = self.page.locator(value)  # Using tag name as CSS selector
        elif locator == "linktext":
            element = self.page.locator(f'text="{value}"')  # Using text selector for link text
        elif locator == "classname":
            element = self.page.locator(f'.{value}')  # Using CSS selector for class name
        elif locator == "partiallinktext":
            element = self.page.locator(f'text*="{value}"')  # Using partial text selector
        else:
            element = None

        return element

 

    
 
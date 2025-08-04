import time
from web.config import page_objects


class WebConstants:
    DEFAULT_WAIT_TIME_SEC = 10  # Default wait time in seconds


class PlayWrightWaits:
    def __init__(self, playwrightdriver):
        """
        Initialize the PlayWrightWaits instance.

        Args:
            playwrightdriver: An instance of the PlayWrightDriver class to interact with the browser.
        """
        self.playwrightdriver = playwrightdriver

    def until_js_and_jquery_to_load(self):
        """
        Wait until both JavaScript and jQuery are fully loaded.

        Returns:
            bool: True if both JavaScript and jQuery are fully loaded, False otherwise.
        """
        jQuery_load = self.playwrightdriver.page.evaluate("return jQuery.active") == 0 if self.playwrightdriver.page.evaluate("return typeof jQuery !== 'undefined'") else True
        js_load = self.playwrightdriver.page.evaluate("return document.readyState") == "complete"
        return jQuery_load and js_load

    def until_title_contains(self, page_title: str, duration: int = WebConstants.DEFAULT_WAIT_TIME_SEC):
        """
        Wait until the page title contains the specified text.

        Args:
            page_title: The text to look for in the page title.
            duration: The maximum time to wait for the title to contain the text (in seconds).

        Returns:
            bool: True if the title contains the specified text within the duration, False otherwise.
        """
        self.until_js_and_jquery_to_load()
        start_time = time.time()
        while time.time() - start_time < duration:
            if page_title in self.playwrightdriver.page.title():
                return True
            time.sleep(0.5)
        return False

    def until_element_displayed(self, selector: str, seconds: int = WebConstants.DEFAULT_WAIT_TIME_SEC):
        """
        Wait until the specified element is displayed.

        Args:
            selector: The CSS selector for the element to wait for.
            seconds: The maximum time to wait for the element to be displayed (in seconds).
        """
        self.until_js_and_jquery_to_load()
        start_time = time.time()
        while time.time() - start_time < seconds:
            if self.playwrightdriver.page.is_visible(selector):
                self.scroll_to(selector)
                return
            time.sleep(0.5)

    def until_element_not_displayed(self, selector: str, seconds: int = WebConstants.DEFAULT_WAIT_TIME_SEC):
        """
        Wait until the specified element is not displayed.

        Args:
            selector: The CSS selector for the element to wait for.
            seconds: The maximum time to wait for the element to be hidden (in seconds).
        """
        self.until_js_and_jquery_to_load()
        start_time = time.time()
        while time.time() - start_time < seconds:
            if not self.playwrightdriver.page.is_visible(selector):
                self.scroll_to(selector)
                return
            time.sleep(0.5)

    def until_element_clickable(self, selector: str, seconds: int = WebConstants.DEFAULT_WAIT_TIME_SEC):
        """
        Wait until the specified element is clickable.

        Args:
            selector: The CSS selector for the element to wait for.
            seconds: The maximum time to wait for the element to be clickable (in seconds).
        """
        self.until_element_displayed(selector, seconds)
        self.until_js_and_jquery_to_load()
        start_time = time.time()
        while time.time() - start_time < seconds:
            if self.playwrightdriver.page.is_enabled(selector):
                self.scroll_to(selector)
                return
            time.sleep(0.5)

    def until_element_not_clickable(self, selector: str, seconds: int = WebConstants.DEFAULT_WAIT_TIME_SEC):
        """
        Wait until the specified element is not clickable.

        Args:
            selector: The CSS selector for the element to wait for.
            seconds: The maximum time to wait for the element to be non-clickable (in seconds).
        """
        self.until_element_displayed(selector, seconds)
        self.until_js_and_jquery_to_load()
        start_time = time.time()
        while time.time() - start_time < seconds:
            if not self.playwrightdriver.page.is_enabled(selector):
                self.scroll_to(selector)
                return
            time.sleep(0.5)

    def sleep(self, seconds: int):
        """
        Pause the execution for a specified number of seconds.

        Args:
            seconds: The number of seconds to pause execution.
        """
        time.sleep(seconds)

    def scroll_to(self, selector: str):
        """
        Scroll the page to bring the specified element into view.

        Args:
            selector: The CSS selector for the element to scroll to.
        """
        element = self.playwrightdriver.page.query_selector(selector)
        if element:
            self.playwrightdriver.page.evaluate("element => element.scrollIntoView(true);", element)
            self.playwrightdriver.page.evaluate("element => element.style.background = 'GreenYellow';", element)
            time.sleep(0.1)
            self.playwrightdriver.page.evaluate("element => element.style.background = '';", element)

    def wait_for_element(self, locator: str, timeout: int = 5000):
        """
        Waits for an element to be present in the DOM.

        Args:
            locator: The selector for the element.
            timeout: Maximum time to wait for the element (in milliseconds).

        Returns:
            The element if found within the timeout, otherwise raises an exception.
        """
        locator = self._get_locator(locator)
        return locator.wait_for(state="visible",timeout=timeout)
       
    
    def _get_locator(self, obj):
        """
        Returns a Locator for the given object (selector or Locator).
        """
        if isinstance(obj, str):
            return self.playwrightdriver.get_element(page_objects.PageObjects().get(obj)[0],page_objects.PageObjects().get(obj)[1])
        return obj

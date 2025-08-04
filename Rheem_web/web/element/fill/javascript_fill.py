class JavaScriptFill:
    """
    Allows sending text to a web element using JavaScript execution in Playwright.
    Sets the 'value' attribute of the specified element to simulate typing.
    """

    def __init__(self, playwrightdriver):
        """
        Initialize with a Playwright Page instance.

        :param page: Playwright Page object.
        """
        self.playwrightdriver = playwrightdriver

    def _get_locator(self, obj):
        """
        Returns a Locator for the given object (selector or Locator).

        :param obj: CSS selector (str) or Locator.
        :return: Locator
        """
        if isinstance(obj, str):
            return self.playwrightdriver.page.locator(obj)
        return obj

    def send_keys(self, obj, text: str):
        """
        Sends text to the specified web element using JavaScript.
        Sets the 'value' attribute of the element to the provided text.

        :param obj: Selector (str) or Locator for the element.
        :param text: The text to send to the web element.
        """
        locator = self._get_locator(obj)
        locator.wait_for(state="visible")
        if locator.is_enabled():
            locator.evaluate("(el, value) => el.value = value", text)
            
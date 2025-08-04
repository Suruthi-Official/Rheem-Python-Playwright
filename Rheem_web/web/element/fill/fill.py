from web.config import page_objects
class Fill:
    """
    Provides methods to send text to web elements and clear input fields using Playwright.
    Waits for elements to be visible before interacting.
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
            return self.playwrightdriver.get_element(page_objects.PageObjects().get(obj)[0],page_objects.PageObjects().get(obj)[1])
        return obj

    def fill_text(self, obj, text: str):
        """
        Sends the specified text to the web element.

        :param obj: Selector (str) or Locator for the element.
        :param text: The text to send to the web element.
        """
        locator = self._get_locator(obj)
        locator.wait_for(state="visible")
        locator.type(text)

     
    def activate_and_type(self, obj, text: str):
        """
        Sends a sequence of keys (text) to a web element.

        :param obj: Selector (str) or Locator for the element.
        :param text: The text to send to the element.
        """
        locator = self._get_locator(obj)
        locator.wait_for(state="visible")
        locator.click()
        locator.type(text)   

    def clear_inputs(self, obj):
        """
        Clears the text of the web element.

        :param obj: Selector (str) or Locator for the element.
        """
        locator = self._get_locator(obj)
        locator.wait_for(state="visible")
        locator.fill("")
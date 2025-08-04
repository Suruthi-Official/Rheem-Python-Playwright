
class JavaScriptClick:
    """
    Provides methods for performing click and double-click actions on elements
    using JavaScript execution in Playwright. Useful when standard click actions
    do not work (e.g., element is not interactable).
    """

    def __init__(self, playwrightdriver):
        """
        Initializes the JavaScriptClick with a Playwright Page instance.
        :param page: The Playwright Page object.
        """
        self.playwrightdriver = playwrightdriver

    def _get_locator(self, obj):
        """
        Returns a Locator for the given object (selector or Locator).
        """
        if isinstance(obj, str):
            return self.playwrightdriver.page.locator(obj)
        return obj

    def click(self, obj):
        """
        Clicks the element using JavaScript execution.
        Waits for the element to be visible and enabled.
        :param obj: Selector (str) or Locator for the element.
        """
        locator = self._get_locator(obj)
        locator.wait_for(state="visible")
        locator.wait_for(state="enabled")
        locator.evaluate("el => el.click()")

    def double_click(self, obj):
        """
        Double-clicks the element using JavaScript execution.
        Waits for the element to be visible and enabled.
        :param obj: Selector (str) or Locator for the element.
        """
        locator = self._get_locator(obj)
        locator.wait_for(state="visible")
        locator.wait_for(state="enabled")
        locator.evaluate("el => { el.click(); el.click(); }")

        
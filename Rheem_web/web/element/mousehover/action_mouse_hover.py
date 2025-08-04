from playwright.sync_api import Page, Locator

class ActionMouseHover:
    """
    Provides a method to simulate a mouse hover over an element using Playwright.
    Accepts either a selector string or a Locator.
    """

    def __init__(self, page: Page):
        """
        Initialize with a Playwright Page instance.
        :param page: Playwright Page object.
        """
        self.page = page

    def _get_locator(self, obj):
        """
        Returns a Locator for the given object (selector or Locator).
        :param obj: CSS selector (str) or Locator.
        :return: Locator
        """
        if isinstance(obj, str):
            return self.page.locator(obj)
        return obj

    def mouse_hover(self, obj):
        """
        Simulates a mouse hover over the specified element.
        :param obj: Selector (str) or Locator for the element.
        """
        locator = self._get_locator(obj)
        locator.wait_for(state="visible")
        locator.hover()
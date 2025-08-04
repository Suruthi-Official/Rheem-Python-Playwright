class GetElementStatus:
    """
    Utility methods to check the state of an element using Playwright.
    Supports checking if an element is selected, enabled, or displayed.
    Accepts either a selector string or a Locator.
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

    def is_selected(self, obj):
        """
        Checks if the element is selected (for checkboxes or radio buttons).
        :param obj: Selector (str) or Locator for the element.
        :return: True if selected, False otherwise.
        """
        locator = self._get_locator(obj)
        locator.wait_for(state="attached")
        return locator.is_checked()  # For checkboxes/radios

    def is_enabled(self, obj):
        """
        Checks if the element is enabled (can be interacted with).
        :param obj: Selector (str) or Locator for the element.
        :return: True if enabled, False otherwise.
        """
        locator = self._get_locator(obj)
        locator.wait_for(state="attached")
        return locator.is_enabled()

    def is_displayed(self, obj):
        """
        Checks if the element is visible on the page.
        :param obj: Selector (str) or Locator for the element.
        :return: True if visible, False otherwise.
        """
        locator = self._get_locator(obj)
        try:
            return locator.is_visible()
        except Exception:
            return False
from time import time


class ActionCheckBox:
    """
    Provides actions to interact with checkboxes on a webpage using Playwright.
    Includes methods to check, uncheck, and toggle checkbox elements.
    """

    def __init__(self, playwrightdriver):
        """
        Initializes the ActionCheckBox with a Playwright Page instance.
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

    def check(self, obj):
        """
        Checks a checkbox if it is not already checked.
        :param obj: Selector (str) or Locator for the checkbox.
        """
        locator = self._get_locator(obj)
        locator.wait_for(state="visible")
        if not locator.is_checked():
            locator.check()

    def uncheck(self, obj):
        """
        Unchecks a checkbox if it is checked.
        :param obj: Selector (str) or Locator for the checkbox.
        """
        locator = self._get_locator(obj)
        locator.wait_for(state="visible")
        if locator.is_checked():
            locator.uncheck()

    def toggle(self, obj):
        """
        Toggles the checkbox (checks if unchecked, unchecks if checked).
        :param obj: Selector (str) or Locator for the checkbox.
        """
        locator = self._get_locator(obj)
        locator.wait_for(state="visible")
        locator.click()

    def is_checked(self, obj):
        """
        Toggles the checkbox (checks if unchecked, unchecks if checked).
        :param obj: Selector (str) or Locator for the checkbox.
        """
        return self.playwrightdriver.page.is_checked(obj)
    

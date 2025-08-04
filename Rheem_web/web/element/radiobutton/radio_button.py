from playwright.sync_api import Page, Locator

class RadioButton:
    """
    Provides a method to select a radio button element using Playwright.
    Waits for the radio button to be visible, checks if it is selected,
    and clicks it if it is not already selected.
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

    def select(self, obj):
        """
        Selects the radio button identified by selector or Locator.
        Waits for the element to be visible, checks if it is selected,
        and clicks it if it is not already selected.

        :param obj: Selector (str) or Locator for the radio button.
        """
        locator = self._get_locator(obj)
        locator.wait_for(state="visible")
        if not locator.is_checked():
            locator.click()
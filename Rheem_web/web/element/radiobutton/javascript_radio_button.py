from playwright.sync_api import Page, Locator

class JavaScriptRadioButton:
    """
    Allows selecting a radio button element using JavaScript in Playwright.
    Executes a script to check the radio button if it is not already selected.
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
        Selects the radio button identified by selector or Locator using JavaScript.
        Waits for the element to be visible, then checks it if not already selected.
        :param obj: Selector (str) or Locator for the radio button.
        """
        locator = self._get_locator(obj)
        locator.wait_for(state="visible")
        locator.evaluate("""
            el => { if (!el.checked) { el.checked = true; el.dispatchEvent(new Event('change', { bubbles: true })); } }
        """)
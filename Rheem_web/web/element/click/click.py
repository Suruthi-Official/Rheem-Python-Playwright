from web.config import page_objects
class Click:
    """
    Provides methods for performing click and double-click actions on elements using Playwright.
    Retries are handled natively by Playwright's robust API.
    """

    def __init__(self, playwrightdriver):
        """
        Initializes the Click with a Playwright Page instance.
        :param page: The Playwright Page object.
        """
        self.playwrightdriver = playwrightdriver


    def click_element(self, obj):
        """
        Clicks the element identified by selector or Locator.
        Waits for the element to be visible before clicking.
        :param obj: Selector (str) or Locator for the element.
        """
        locator = self._get_locator(obj)
        locator.wait_for(state="visible")
        locator.click()

    def double_click(self, obj):
        """
        Double-clicks the element identified by selector or Locator.
        Waits for the element to be visible before double-clicking.
        :param obj: Selector (str) or Locator for the element.
        """
        locator = self._get_locator(obj)
        locator.wait_for(state="visible")
        locator.dblclick()

    def _get_locator_po(self, obj):
        """
        Returns a Locator for the given object (selector or Locator).
        """
        if isinstance(obj, str):
            return self.playwrightdriver.page.locator(obj)
        return obj    

    def _get_locator(self, obj):
        """
        Returns a Locator for the given object (selector or Locator).
        """
        if isinstance(obj, str):
            return self.playwrightdriver.get_element(page_objects.PageObjects().get(obj)[0],page_objects.PageObjects().get(obj)[1])
        return obj

    
     
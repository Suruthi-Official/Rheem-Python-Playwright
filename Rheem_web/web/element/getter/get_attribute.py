from playwright.sync_api import Page, Locator
from web.config import page_objects

class GetAttribute:
    """
    Provides methods to fetch the text or attribute value of a given element using Playwright.
    Supports both selector strings and Locator objects.
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
            return self.playwrightdriver.get_element(page_objects.PageObjects().get(obj)[0],page_objects.PageObjects().get(obj)[1])
        return obj

    
def text(self, obj, context=None):
    """
    Retrieves the text content of the element.
    
    :param obj: Selector (str) or Locator for the element.
    :param context: Optional context (Locator) to narrow the search scope.
    :return: The text content of the element.
    """
    if context:
        locator = context.locator(self._get_locator(obj).selector)
    else:
        locator = self._get_locator(obj)
    
    locator.wait_for(state="visible")
    return locator.inner_text()


    def fetch(self, obj, attribute_name):
        """
        Retrieves the value of a specific attribute of the element.
        :param obj: Selector (str) or Locator for the element.
        :param attribute_name: The name of the attribute.
        :return: The value of the specified attribute.
        """
        locator = self._get_locator(obj)
        locator.wait_for(state="visible")
        return locator.get_attribute(attribute_name)
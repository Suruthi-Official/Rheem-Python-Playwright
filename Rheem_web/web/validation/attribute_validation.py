from playwright.sync_api import Page, Locator
from web.validation import Assertion

class AttributeValidation:
    """
    Provides methods to verify the value of an element's attribute.
    Compares the actual value of an attribute with the expected value,
    and asserts whether they should match or not.
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

    def verify(self, obj, attribute_name: str, expected_attribute_value: str, should_be_matched: bool):
        """
        Verifies the value of an element's attribute against an expected value.

        :param obj: Selector (str) or Locator for the element.
        :param attribute_name: The name of the attribute to verify.
        :param expected_attribute_value: The expected value of the attribute.
        :param should_be_matched: Whether the attribute value should match the expected value.
        """
        locator = self._get_locator(obj)
        locator.wait_for(state="visible")
        displayed_attribute_value = locator.get_attribute(attribute_name)

        assert displayed_attribute_value is not None, f"Attribute '{attribute_name}' not found on element."

        if should_be_matched:
            Assertion.equals(
                displayed_attribute_value,
                expected_attribute_value,
                f'Expected: Attribute value "{expected_attribute_value}" should match with actual attribute value "{displayed_attribute_value}". But attribute value is not matched.'
            )
        else:
            Assertion.not_equals(
                displayed_attribute_value,
                expected_attribute_value,
                f'Expected: Attribute value "{expected_attribute_value}" should not match with actual attribute value "{displayed_attribute_value}". But attribute value is matched.'
            )
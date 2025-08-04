

class Dropdown:
    """
    Provides methods for interacting with standard HTML select dropdowns using Playwright.
    Includes methods to select, deselect, and multi-select options from dropdown lists.
    """

    def __init__(self,playwrightdriver ):
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

    def select(self, option, option_by, obj):
        """
        Selects an option from the dropdown by index, value, or text.
        :param option: The option to select (index, value, or text).
        :param option_by: The method to identify the option ('index', 'value', 'text').
        :param obj: Selector (str) or Locator for the dropdown.
        """
        locator = self._get_locator(obj)
        locator.wait_for(state="visible")
        if option_by == "index":
            locator.select_option(index=int(option) - 1)
        elif option_by == "value":
            locator.select_option(value=option)
        elif option_by == "text":
            locator.select_option(label=option)

    def deselect(self, option, option_by, obj):
        """
        Deselects an option from a multi-select dropdown by index, value, or text.
        :param option: The option to deselect (index, value, or text).
        :param option_by: The method to identify the option ('index', 'value', 'text').
        :param obj: Selector (str) or Locator for the dropdown.
        """
        locator = self._get_locator(obj)
        locator.wait_for(state="visible")
        selected = locator.evaluate("el => Array.from(el.selectedOptions).map(o => o.value)")
        if option_by == "index":
            idx = int(option) - 1
            value = locator.evaluate(f"el => el.options[{idx}].value")
            selected = [v for v in selected if v != value]
        elif option_by == "value":
            selected = [v for v in selected if v != option]
        elif option_by == "text":
            value = locator.evaluate(f"el => Array.from(el.options).find(o => o.text === '{option}')?.value")
            selected = [v for v in selected if v != value]
        locator.select_option(selected)

    def deselect_all(self, obj):
        """
        Deselects all options in a multi-select dropdown.
        :param obj: Selector (str) or Locator for the dropdown.
        """
        locator = self._get_locator(obj)
        locator.wait_for(state="visible")
        locator.select_option([])

    def multi_select(self, options, obj):
        """
        Selects multiple options in a multi-select dropdown by visible text.
        :param options: List of option texts to select.
        :param obj: Selector (str) or Locator for the dropdown.
        """
        locator = self._get_locator(obj)
        locator.wait_for(state="visible")
        values = []
        for option in options:
            value = locator.evaluate(f"el => Array.from(el.options).find(o => o.text === '{option}')?.value")
            if value:
                values.append(value)
        locator.select_option(values)
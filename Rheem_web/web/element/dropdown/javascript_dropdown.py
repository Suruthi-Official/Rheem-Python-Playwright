from playwright.sync_api import Page, Locator

class JavaScriptDropdown:
    """
    Provides methods for interacting with dropdown elements (select elements)
    using JavaScript execution in Playwright. Supports selecting, deselecting,
    and handling multi-select options by index, value, or visible text.
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

    def select(self, option, option_by, obj):
        """
        Selects an option in a dropdown by index, value, or text using JavaScript.
        :param option: The option to select (index, value, or text).
        :param option_by: 'index', 'value', or 'text'.
        :param obj: Selector (str) or Locator for the dropdown.
        """
        locator = self._get_locator(obj)
        locator.wait_for(state="visible")
        if option_by == "index":
            index = int(option) - 1
            locator.evaluate(f"select => select.options[{index}].selected = true")
        elif option_by == "value":
            locator.evaluate(
                "(select, value) => { for(let i=0; i<select.options.length; i++){ if(select.options[i].value == value){ select.options[i].selected = true; }}}",
                option
            )
        elif option_by == "text":
            locator.evaluate(
                "(select, text) => { for(let i=0; i<select.options.length; i++){ if(select.options[i].text == text){ select.options[i].selected = true; }}}",
                option
            )

    def deselect(self, option, option_by, obj):
        """
        Deselects an option in a dropdown by index, value, or text using JavaScript.
        :param option: The option to deselect (index, value, or text).
        :param option_by: 'index', 'value', or 'text'.
        :param obj: Selector (str) or Locator for the dropdown.
        """
        locator = self._get_locator(obj)
        locator.wait_for(state="visible")
        if option_by == "index":
            index = int(option) - 1
            locator.evaluate(f"select => select.options[{index}].selected = false")
        elif option_by == "value":
            locator.evaluate(
                "(select, value) => { for(let i=0; i<select.options.length; i++){ if(select.options[i].value == value){ select.options[i].selected = false; }}}",
                option
            )
        elif option_by == "text":
            locator.evaluate(
                "(select, text) => { for(let i=0; i<select.options.length; i++){ if(select.options[i].text == text){ select.options[i].selected = false; }}}",
                option
            )

    def deselect_all(self, obj):
        """
        Deselects all options in a multi-select dropdown using JavaScript.
        :param obj: Selector (str) or Locator for the dropdown.
        """
        locator = self._get_locator(obj)
        locator.wait_for(state="visible")
        locator.evaluate(
            "select => { for(let i=0; i<select.options.length; i++){ if(select.options[i].selected){ select.options[i].selected = false; }}}"
        )

    def select_all(self, obj):
        """
        Selects all options in a multi-select dropdown using JavaScript.
        :param obj: Selector (str) or Locator for the dropdown.
        """
        locator = self._get_locator(obj)
        locator.wait_for(state="visible")
        locator.evaluate(
            "select => { for(let i=0; i<select.options.length; i++){ if(!select.options[i].selected){ select.options[i].selected = true; }}}"
        )
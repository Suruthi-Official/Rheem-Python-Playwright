import os
import json
import yaml
from collections import defaultdict

from utils.excel_reader import ExcelReader
from Rheem_utilities.utils.constants import Constants
from web.config import web_constants


class PageObjects:
    """
    Manages loading, retrieval, modification, and saving of Page Object data from YAML, JSON, or Excel.
    Provides methods for retrieving and updating locators for elements defined in the Page Object model.
    """

    def __init__(self):
        """
        Initializes the page objects by loading data from the configured file format.
        :param config: A dict with keys 'type', 'input_path', 'output_path', and optionally 'excel_loader'.
        """
        self.objects = defaultdict(lambda: defaultdict(dict))
        extension = web_constants.PAGE_OBJECT_TYPE
        page_objects_path = Constants.PAGE_OBJECTS_PATH
        try:
            if extension in ('yaml', 'yml'):
                with open(os.path.join(page_objects_path, 'page_objects.yaml'), 'r', encoding='utf-8') as f:
                    self.objects = yaml.safe_load(f)
            elif extension == 'json':
                with open(os.path.join(page_objects_path, 'page_objects.json'), 'r', encoding='utf-8') as f:
                    self.objects = json.load(f)
            elif extension in ('xlsx', 'excel', 'xls'):
                # Requires a custom loader function for Excel
                self.excel_reader = ExcelReader()
                self.objects= self.excel_reader.get_page_objects(os.path.join(page_objects_path, 'page_objects.xlsx'))
            else:
                self.objects = {}
        except Exception:
            self.objects = {}

        # # Ensure every element has a default "value" key if not present
        # if self.objects:
        #     for page in self.objects:
        #         for element in self.objects[page]:
        #             self.objects[page][element].setdefault('value', '')

    def get(self, obj_name):
        """
        Retrieves the locator (key-value pair) for a given element on a page.
        :param obj_name: The name of the object in the format "page.element".
        :return: (locator_type, locator_value) tuple or (None, None) if not found.
        """
        try:
            page, element = obj_name.split('.', 1)
            for locator, value in self.objects[page][element].items():
                if locator.lower() not in ('value',) and value:
                    if locator.lower() in ("id", "css", "name", "xpath", "tagname", "linktest", "classname", "partiallinktest"):
                        return locator, value
        except Exception:
            pass
        return None, None

    def set(self, obj_name, locator, locator_value):
        """
        Sets the value of a specific locator for a given element.
        :param obj_name: The name of the object in the format "page.element".
        :param locator: The type of locator (e.g., "xpath", "css", etc.).
        :param locator_value: The value of the locator.
        :return: The value of the locator that was set.
        """
        try:
            page, element = obj_name.split('.', 1)
            self.objects[page][element][locator] = locator_value
            return locator_value
        except Exception:
            return ""

    def get_locator_value(self, obj_name, locator):
        """
        Retrieves the value of a specific locator for a given element.
        :param obj_name: The name of the object in the format "page.element".
        :param locator: The type of locator.
        :return: The value of the locator, or an empty string if not found.
        """
        try:
            page, element = obj_name.split('.', 1)
            return self.objects[page][element].get(locator, "")
        except Exception:
            return ""

    def unload(self, output_path):
        """
        Saves the current page objects to both YAML and JSON formats.
        :param output_path: Directory to save the files.
        """
        os.makedirs(output_path, exist_ok=True)
        try:
            # Write YAML file
            with open(os.path.join(output_path, 'page_objects.yaml'), 'w', encoding='utf-8') as f:
                yaml.dump(self.objects, f, allow_unicode=True)
            # Write JSON file
            with open(os.path.join(output_path, 'page_objects.json'), 'w', encoding='utf-8') as f:
                json.dump(self.objects, f, indent=2, ensure_ascii=False)
        except Exception:
            pass
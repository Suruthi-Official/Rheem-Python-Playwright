import base64
import re


class Strings:
    """
            Extracts the locator from a WebElement string representation.

            :param element_string: The string containing the locator.
            :return: The locator substring.
            """

    @staticmethod
    def parse_locator_from_webelement_string(element_string: str) -> str:

        return element_string[element_string.index(" -> ") + 4:]

    """
            Maps a string key name to the Playwright key representation.

            :param key: The string representing a key (e.g., "ENTER", "BACK_SPACE").
            :return: The Playwright key string.
            """

    @staticmethod
    def identify_key(key: str) -> str:

        key_map = {
            "NULL": "Null",
            "CANCEL": "Cancel",
            "HELP": "Help",
            "BACK_SPACE": "Backspace",
            "TAB": "Tab",
            "CLEAR": "Clear",
            "RETURN": "Enter",
            "ENTER": "Enter",
            "SHIFT": "Shift",
            "LEFT_SHIFT": "Shift",
            "CONTROL": "Control",
            "LEFT_CONTROL": "Control",
            "ALT": "Alt",
            "LEFT_ALT": "Alt",
            "PAUSE": "Pause",
            "ESCAPE": "Escape",
            "SPACE": " ",
            "PAGE_UP": "PageUp",
            "PAGE_DOWN": "PageDown",
            "END": "End",
            "HOME": "Home",
            "LEFT": "ArrowLeft",
            "ARROW_LEFT": "ArrowLeft",
            "UP": "ArrowUp",
            "ARROW_UP": "ArrowUp",
            "RIGHT": "ArrowRight",
            "ARROW_RIGHT": "ArrowRight",
            "DOWN": "ArrowDown",
            "ARROW_DOWN": "ArrowDown",
            "INSERT": "Insert",
            "DELETE": "Delete",
            "SEMICOLON": ";",
            "EQUALS": "=",
            "NUMPAD0": "Numpad0",
            "NUMPAD1": "Numpad1",
            "NUMPAD2": "Numpad2",
            "NUMPAD3": "Numpad3",
            "NUMPAD4": "Numpad4",
            "NUMPAD5": "Numpad5",
            "NUMPAD6": "Numpad6",
            "NUMPAD7": "Numpad7",
            "NUMPAD8": "Numpad8",
            "NUMPAD9": "Numpad9",
            "MULTIPLY": "*",
            "ADD": "+",
            "SEPARATOR": ",",
            "SUBTRACT": "-",
            "DECIMAL": ".",
            "DIVIDE": "/",
            "F1": "F1",
            "F2": "F2",
            "F3": "F3",
            "F4": "F4",
            "F5": "F5",
            "F6": "F6",
            "F7": "F7",
            "F8": "F8",
            "F9": "F9",
            "F10": "F10",
            "F11": "F11",
            "F12": "F12"
        }
        return key_map.get(key.upper(), "Null")

    """
            Removes UTF-16 escape sequences (e.g., \\uXXXX) from the string.

            :param data: The string to process.
            :return: The string with UTF-16 escapes replaced by their characters.
            """

    @staticmethod
    def remove_utf_characters(data: str) -> str:

        def replace(match):
            return chr(int(match.group(1), 16))

        return re.sub(r'\\u([0-9A-Fa-f]{4})', replace, data)

    """
            Fetches a substring from the string using a regex and group index.

            :param string: The source string.
            :param regex: The regex pattern.
            :param group: The group index to fetch.
            :return: The matched group or None.
            """

    @staticmethod
    def string_fetch(string: str, regex: str, group: int) -> str | None:

        match = re.search(regex, string)
        return match.group(group) if match else None

    """
            Searches for a substring in a list of strings using a regex pattern.

            :param lst: The list of strings to search.
            :param search_string: The substring to search for.
            :return: The matched string or None.
            """

    @staticmethod
    def substring_search_in_list(lst: list[str], search_string: str) -> str | None:

        regex = rf"^@({search_string})(.*)\d+"
        for string in lst:
            if re.match(regex, string):
                return string
        return None

    """
           Encodes a string using Base64.

           :param string: The string to encode.
           :return: The Base64 encoded string.
           """

    @staticmethod
    def encode(string: str) -> str:

        return base64.b64encode(string.encode()).decode()

    """
            Decodes a Base64 encoded string.

            :param bytes_str: The Base64 encoded string.
            :return: The decoded string.
            """

    @staticmethod
    def decode(bytes_str: str) -> str:

             return base64.b64decode(bytes_str.encode()).decode()

    """
           Asserts that two strings are equal.

           :param str1: The first string.
           :param str2: The second string.
           :raises AssertionError: If the strings are not equal.
           """

    @staticmethod
    def compare_strings(str1: str, str2: str):
        assert str1 == str2, f"Strings do not match: '{str1}' != '{str2}'"

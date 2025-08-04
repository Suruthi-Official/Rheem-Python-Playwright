import random
import string

class StringUtils:
    """
    Utility methods for string operations such as obfuscation, indentation, and random string generation.
    This class cannot be instantiated.
    """
    def __new__(cls, *args, **kwargs):
        raise NotImplementedError("StringUtils class cannot be instantiated.")

    @staticmethod
    def secret(secret):
        return "null" if secret is None else "*" * len(secret)

    @staticmethod
    def indent(text, indent_char="  ", amount=1):
        indentation = indent_char * amount
        return "\n".join(f"{indentation}{line}" for line in text.splitlines())

    @staticmethod
    def random_string(length):
        characters = string.ascii_letters + string.digits
        return ''.join(random.choice(characters) for _ in range(length))

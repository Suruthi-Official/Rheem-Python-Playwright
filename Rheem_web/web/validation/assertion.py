# src/main/python/web/validation/assertion.py

import os
import pytest_check as check

class Assertion:
    """
    Provides methods for both hard and soft assertions.
    Allows switching between assertion types during test execution.
    """

    # Default assertion type is 'soft'
    _default_assertion = os.environ.get("DEFAULT_ASSERTION", "soft")

    @classmethod
    def switch_assertion(cls, assertion_type: str):
        """
        Switches the type of assertion to be used ('soft' or 'hard').
        """
        cls._default_assertion = assertion_type
        os.environ["DEFAULT_ASSERTION"] = assertion_type

    @classmethod
    def equals_true(cls, condition: bool, message: str = ""):
        """
        Asserts that the provided condition is true.
        """
        if cls._default_assertion == "soft":
            check.is_true(condition, message)
        else:
            assert condition, message

    @classmethod
    def equals_false(cls, condition: bool, message: str = ""):
        """
        Asserts that the provided condition is false.
        """
        if cls._default_assertion == "soft":
            check.is_false(condition, message)
        else:
            assert not condition, message

    @classmethod
    def equals(cls, actual, expected, message: str = ""):
        """
        Asserts that actual equals expected.
        """
        if cls._default_assertion == "soft":
            check.equal(actual, expected, message)
        else:
            assert actual == expected, message

    @classmethod
    def not_equals(cls, actual, expected, message: str = ""):
        """
        Asserts that actual does not equal expected.
        """
        if cls._default_assertion == "soft":
            check.not_equal(actual, expected, message)
        else:
            assert actual != expected, message
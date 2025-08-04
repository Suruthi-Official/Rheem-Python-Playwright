from datetime import datetime, date, timedelta
import time

class DateTimeUtils:
    """
    Utility class for date and time operations.
    """

    @staticmethod
    def get_current_date_time():
        """
        Retrieves the current system date and time formatted as a string.
        Format: "yyyy/MM/dd hh:mm:ss AM/PM"
        """
        return datetime.now().strftime("%Y/%m/%d %I:%M:%S %p")

    @staticmethod
    def get_current_date():
        """
        Retrieves the current system date formatted as a string.
        Format: "yyyy/MM/dd"
        """
        return datetime.now().strftime("%Y/%m/%d")

    @staticmethod
    def get_current_time():
        """
        Retrieves the current system time formatted as a string.
        Format: "hh:mm:ss AM/PM"
        """
        return datetime.now().strftime("%I:%M:%S %p")

    @staticmethod
    def get_date_after_days(origin_date, days):
        """
        Calculates the date after a specified number of days from the origin date.
        :param origin_date: "yyyy-MM-dd" or "TODAY"
        :param days: int
        :return: "yyyy-MM-dd"
        """
        if origin_date.upper() == "TODAY":
            new_date = datetime.now() + timedelta(days=days)
        else:
            new_date = datetime.strptime(origin_date, "%Y-%m-%d") + timedelta(days=days)
        return new_date.strftime("%Y-%m-%d")

    @staticmethod
    def get_date_before_days(origin_date, days):
        """
        Calculates the date before a specified number of days from the origin date.
        :param origin_date: "yyyy-MM-dd" or "TODAY"
        :param days: int
        :return: "yyyy-MM-dd"
        """
        if origin_date.upper() == "TODAY":
            new_date = datetime.now() - timedelta(days=days)
        else:
            new_date = datetime.strptime(origin_date, "%Y-%m-%d") - timedelta(days=days)
        return new_date.strftime("%Y-%m-%d")

    @staticmethod
    def convert_date_format(date_str, current_format, expected_format):
        """
        Converts the format of a given date string from the current format to the expected format.
        :param date_str: str
        :param current_format: str
        :param expected_format: str
        :return: str
        """
        dt = datetime.strptime(date_str, current_format)
        return dt.strftime(expected_format)

    @staticmethod
    def date_difference_in_days(date1, date2):
        """
        Calculates the difference in days between two dates.
        :param date1: datetime.date or datetime.datetime
        :param date2: datetime.date or datetime.datetime
        :return: int
        """
        if isinstance(date1, datetime):
            date1 = date1.date()
        if isinstance(date2, datetime):
            date2 = date2.date()
        return abs((date1 - date2).days)
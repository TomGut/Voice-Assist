import locale
from datetime import datetime


class Time_Skill:
    """ 
    Functionality to provide date, time and week no.
    """

    def __init__(self) -> None:
        self._locale = locale.setlocale(locale.LC_ALL, "")
        self._today = datetime.today()

    def get_date(self) -> str:
        """
        Provide formatted date.

        Returns:
            str: 
                date with weekday full name, day of month as decimal number,
                month in full name.
        """
        date = self._today.strftime("%A, %-d %B")
        return date

    def get_week_number(self) -> str:
        """
        Provide formatted year's week number.

        Returns:
            str: Year's week no (Monday as the first day of the week considered as 0) as a decimal number. 
        """
        week = self._today.strftime("%-W")
        return week

    def get_time(self) -> str:
        """
        Provide formatted hour.

        Returns:
            str: hour in format hh:mm
        """
        hour = self._today.strftime("%X")
        return hour

""" 
Functionality to provide date, time and week no.
"""

import locale
from datetime import datetime
from typing import Optional


class Time_Skill:
    def __init__(self) -> None:
        locale.setlocale(locale.LC_ALL, "")
        self._today = datetime.today()

    def get_date(self) -> Optional[datetime]:
        date = self._today.strftime("%A, %-d %B")
        return date

    def get_week_number(self) -> Optional[datetime]:
        week = self._today.strftime("%-W")
        return week

    def get_time(self) -> Optional[datetime]:
        hour = self._today.strftime("%X")
        return hour

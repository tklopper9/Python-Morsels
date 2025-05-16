from datetime import date, datetime, timedelta
from enum import Enum

class NextDate():
    def __init__(self, weekday, after_today=False):
        self.weekday = weekday
        self.after_today = after_today
    def days_until(self):
        day_diff =  self.weekday.value - date.today().weekday()
        if day_diff < 0:
            day_diff = 7 + day_diff
        if self.after_today is True:
            if day_diff == 0:
                day_diff = 7
        return day_diff
    def date(self):
        return date.today() + timedelta(days = self.days_until())
    def __repr__(self):
        return f"Nextday({self.weekday.name}, after_today=={self.after_today})"

def days_until(weekday, after_today=False):
    day_diff = weekday.value - date.today().weekday()
    if day_diff < 0:
        day_diff = 7 + day_diff
    if after_today is True:
        if day_diff == 0:
                day_diff = 7
    return day_diff

def next_date(weekday, after_today=False):
        return date.today() + timedelta(days = days_until(weekday, after_today=after_today))

def days_to_tuesday(after_today=False):
    return days_until(Weekday.TUESDAY, after_today=after_today)

def next_tuesday(after_today=False):
    return next_date(Weekday.TUESDAY, after_today=after_today)
        

class Weekday(Enum):
    MONDAY = 0
    TUESDAY = 1
    WEDNESDAY = 2
    THURSDAY = 3
    FRIDAY = 4
    SATURDAY = 5
    SUNDAY = 6
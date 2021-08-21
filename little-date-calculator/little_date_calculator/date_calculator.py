"""
date calculator module
"""
from little_date_calculator.error import ValidationError

# the -1 is just placeholder
MONTH_DAYS = [-1, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
BEGIN_YEAR = 1901


class DateCalculator:

    @classmethod
    def is_leap_year(cls, year: int) -> bool:
        """ the leap year logic from
        https://docs.microsoft.com/en-us/office/troubleshoot/excel/determine-a-leap-year

        :param year: the year to check whether is leap year
        :return: true if it is leap year, else false
        """
        if year % 400 == 0 or (year % 4 == 0 and year % 100 != 0):
            return True
        return False

    def validate(self, date: dict) -> bool:
        expected_max_day = MONTH_DAYS[int(date["month"])]
        if int(date["month"]) == 2 and self.is_leap_year(int(date["year"])):
            expected_max_day += 1

        if int(date["day"]) > expected_max_day:
            return False
        return True

    def convert_days(self, date: dict) -> int:
        """ this method calculate the days between 01/01/1901 to the input date

        :param date:
        :return: number of days since 01/01/1901 to the input date
        """

        if not self.validate(date):
            raise ValidationError(f"{date} is invalid date")

        days = int(date["day"])
        begin_month = 1
        while begin_month < int(date["month"]):
            if self.is_leap_year(int(date["year"])) and begin_month == 2:
                days += MONTH_DAYS[begin_month] + 1
            else:
                days += MONTH_DAYS[begin_month]
            begin_month += 1

        begin_year = BEGIN_YEAR
        acc_leap_days = 0
        while begin_year < int(date["year"]):
            if self.is_leap_year(begin_year):
                acc_leap_days += 1
            begin_year += 1

        return days + (int(date["year"]) - BEGIN_YEAR)*365 + acc_leap_days

    def diff(self, start_date: dict, end_date: dict):
        if self.convert_days(start_date) >= self.convert_days(end_date):
            raise ValidationError("input end date need to be large than start date")
        return self.convert_days(end_date) - self.convert_days(start_date) - 1

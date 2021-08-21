"""
date input parser module
"""
import re
from little_date_calculator.error import ValidationError, FormatError


class ParserDDMMYYYY:

    @classmethod
    def validate(cls, date: str) -> bool:
        """This method validate the input date with the regex, that match with format
        dd/mm/yyyy

        :param date: date to be validated
        :return: true if date with format dd/mm/yyyy, else false
        """

        regex = re.compile(
            '(^(((0[1-9]|1[0-9]|2[0-8])[\/](0[1-9]|1[012]))|((29|30|31)[\/](0[13578]|1[02]))|((29|30)[\/](0[4,6,9]|11)))[\/](19|[2-9][0-9])\d\d$)|(^29[\/]02[\/](19|[2-9][0-9])(00|04|08|12|16|20|24|28|32|36|40|44|48|52|56|60|64|68|72|76|80|84|88|92|96)$)',
            re.I)

        match = regex.match(str(date))
        return bool(match)

    @classmethod
    def parse(cls, date: str):
        date_splits = date.split("/")
        return {"year": date_splits[2], "month": date_splits[1], "day": date_splits[0]}


class DateInputParser:

    def __init__(self, date_format: str):
        if date_format == "dd/mm/yyyy":
            self._parser = ParserDDMMYYYY()
        else:
            raise FormatError(f"input date format {date_format} is not supported")

        self._date_format = date_format

    def parse(self, date):
        if self._parser.validate(date):
            return self._parser.parse(date)
        raise ValidationError(f"input date {date} not compile with date format {self._date_format}")

import datetime
from little_date_calculator.date_calculator import DateCalculator
import random
from datetime import datetime, timedelta


def test_convert_days():
    test_size = 1000
    while test_size > 0:
        random_days = random.randint(0, 401401)
        test_date = datetime.strptime("01/01/1901", "%d/%m/%Y") + timedelta(days=random_days)
        test_size -= 1
        calculator = DateCalculator()
        assert random_days + 1 == calculator.convert_days({"year": test_date.strftime("%Y"), "month": test_date.strftime("%m"), "day": test_date.strftime("%d")})

def test_validation():
    false_date = [{"year": "1985",
                   "month": "02",
                   "day": "29"},
                  {"year": "1985",
                   "month": "11",
                   "day": "31"}]
    calculator = DateCalculator()

    for date in false_date:
        assert calculator.validate(date) == False

    valid_date = [{"year": "1984",
                   "month": "02",
                   "day": "29"},
                  {"year": "1985",
                   "month": "11",
                   "day": "30"}]

    for date in valid_date:
        assert calculator.validate(date) == True

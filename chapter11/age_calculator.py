# age_calculator.py
import datetime

class AgeCalculator:
    def __init__(self, birthday):
        self.year, self.month, self.day = (
            int(x) for x in birthday.split("-")
        )

    def calculate_age(self, date):
        year, month, day = (int(x) for x in date.split("-"))
        age = year - self.year
        if (month, day) < (self.month, self.day):
            age -= 1
        return age

class DateAgeAdapter:
    
    def _str_date(self, date):
        return date.strftime("%Y-%m-%d")
    
    def __init__(self, birthday):
        birthday = self._str_date(birthday)
        self.calculator = AgeCalculator(birthday)
    
    def get_age(self, date):
        date = self._str_date(date)
        return self.calculator.calculate_age(date)

class AgeableDate(datetime.date):
    
    def split(self, char):
        return self.year, self.month, self.day

def main():
    # max = AgeCalculator('1964-03-23')
    # max = AgeCalculator('1969-10-07')
    # max = AgeCalculator('1998-04-16')
    # print('Age:', max.calculate_age('2020-12-28'))

    # bday = datetime.date(1998,4,16) 
    # max = DateAgeAdapter(bday)
    # today = datetime.date.today()
    # print('Age:', max.get_age(today))

    bday = AgeableDate(1998,4,16)
    today = AgeableDate.today()
    print(today)
    max = AgeCalculator(bday)
    print('Age:', max.calculate_age(today))


if __name__ == '__main__':
    main() 

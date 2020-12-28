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

def main():
    # max = AgeCalculator('1964-03-23')
    # max = AgeCalculator('1969-10-07')
    max = AgeCalculator('1998-04-16')
    print('Age:', max.calculate_age('2020-12-28'))

if __name__ == '__main__':
    main() 

# Задание 8.1
# Реализовать класс «Дата», функция-конструктор которого должна принимать дату в виде строки формата «день-месяц-год».
# В рамках класса реализовать два метода. Первый, с декоратором @classmethod.
# Он должен извлекать число, месяц, год и преобразовывать их тип к типу «Число».
# Второй, с декоратором @staticmethod, должен проводить валидацию числа, месяца и года (например, месяц — от 1 до 12).
# Проверить работу полученной структуры на реальных данных.

class Date:
    days_in_month = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

    def __init__(self, s_date):
        self.date = s_date

    @classmethod
    def get_date_elements(cls, n_date):
        day, month, year = n_date.date.split('-')
        day = int(day) if day.isdigit() else 0
        month = int(month) if month.isdigit() else 0
        year = int(year) if year.isdigit() else 0
        return [day, month, year]

    @staticmethod
    def validate_date(day, month, year):
        if month >= 1 and month <= 12 and ((month != 2 and day <= Date.days_in_month[month-1]) or
                                           (month == 2 and (day <= 28 or (day == 29 and
                                                                         ((year % 4 == 0 and year % 100 != 0) or
                                                                          (year % 400 == 0)))))):
            return True
        return False


current_date = Date('29-02-2000')
day, month, year = current_date.get_date_elements(current_date)
print(f'День: {day}. Месяц: {month}. Год: {year}')
if Date.validate_date(day, month, year):
    print('Дата корректна')
else:
    print('Дата некорректна!')
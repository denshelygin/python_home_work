'''
Задание №2
В модуль с проверкой даты добавьте возможность запуска в терминале с передачей даты на проверку
'''
from sys import argv


def dat(st):
    day, month, year = map(int, (st.split(".")))
    if year in range(1, 10000) and month in range(1, 13) and day in range(1, 32):
        if year % 400 == 0 or year % 4 == 0 and year % 100 != 0 and month == 2:
            if day <= 29:
                return True
            else:
                return False
        if month in [1, 3, 5, 7, 8, 10, 12]:
            if day <= 31:
                return True
            else:
                return False
        elif month == 2:
            if day <= 28:
                return True
            else:
                return False
        else:
            if day <= 30:
                return True
            else:
                return False
    else:
        return False


str_data = argv[1]
print(dat(str_data))
'''
Задание №1
Напишите функцию, которая принимает на вход строку —
абсолютный путь до файла. Функция возвращает кортеж из трёх
элементов: путь, имя файла, расширение файла
'''

import os

def fun(f_path: str) -> tuple:
    path, filename = os.path.split(f_path)
    name, extension = filename.split('.')
    return path, name, extension


way_fail = "D:\Софт\Telegram Desktop\homework_3.xlsx"
print(fun(way_fail))



'''
Напишите программу, которая принимает две строки вида “a/b” - дробь с числителем и знаменателем.
Программа должна возвращать сумму и произведение* дробей.
Для проверки своего кода используйте модуль fractions'''
import fractions

str1 = str(input("Введите дробное число в формате н/н: "))
str2 = str(input("Введите дробное число в формате н/н: "))

fr1 = str1.split('/')
fr2 = str2.split('/')
summa = str(int(fr1[0]) * int(fr2[1]) + int(fr1[1]) * int(fr2[0])) + '/' + str(int(fr2[1]) * int(fr1[1]))
mult = str(int(fr1[0]) * int(fr2[0])) + '/' + str(int(fr1[1]) * int(fr2[1]))
print(f'Сумма {summa}, Произведение {mult}')
f1 = fractions.Fraction(int(fr1[0]), int(fr1[1]))
f2 = fractions.Fraction(int(fr2[0]), int(fr2[1]))
print(f'Проверка Fractions сумма {f1+f2}, произведение {f1*f2}')


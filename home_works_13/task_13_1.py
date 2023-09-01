'''
Задание №1
Треугольник существует только тогда, когда сумма любых двух его сторон больше третьей.
Дано a, b, c - стороны предполагаемого треугольника. Требуется сравнить длину каждого
отрезка-стороны с суммой двух других. Если хотя бы в одном случае отрезок окажется больше
суммы двух других, то треугольника с такими сторонами не существует. Отдельно сообщить является
ли треугольник разносторонним, равнобедренным или равносторонним.
'''


class TriangleExseption(Exception):

    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def __str__(self):
        return f'Треугольник со сторонами {self.a}, {self.b}, {self.c} не может существовать'


a = float(input("Введите длину стороны a: "))
b = float(input("Введите длину стороны b: "))
c = float(input("Введите длину стороны c: "))

if a + b <= c or a + c <= b or b + c <= a:
    raise TriangleExseption(a, b, c)
else:
    if a == b == c:
        print("Треугольник является равносторонним.")
    elif a == b or a == c or b == c:
        print("Треугольник является равнобедренным.")
    else:
        print("Треугольник является разносторонним.")

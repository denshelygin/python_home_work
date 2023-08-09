'''
Задание№3
Возьмите задачу о банкомате из семинара 2. Разбейте её на отдельные операции — функции.
Дополнительно сохраняйте все операции поступления и снятия средств в список.

Напишите программу банкомат.
✔ Начальная сумма равна нулю
✔ Допустимые действия: пополнить, снять, выйти
✔ Сумма пополнения и снятия кратны 50 у.е.
✔ Процент за снятие — 1.5% от суммы снятия, но не менее 30 и не более 600 у.е.
✔ После каждой третей операции пополнения или снятия начисляются проценты - 3%
✔ Нельзя снять больше, чем на счёте
✔ При превышении суммы в 5 млн, вычитать налог на богатство 10% перед каждой
операцией, даже ошибочной
✔ Любое действие выводит сумму денег
'''

summ = 0
count_add = 0
count_out = 0

summa = 0
LIST = ('50', '100', '150', '500', '1000', '5000', 'Другое', 'Выход')
percent = 1.5
count = 0
TAX = 10
operation = {}


def task_choice() -> str:
    print('Выберите следующие действия\n'
          '1: Пополнить\n'
          '2: Снять\n'
          '3: Выйти\n')
    choice = input('Введите номер действия: ').strip()
    while not choice.isdigit() or choice > '3':
        print('Выберите следующие действия\n'
              '1: Пополнить\n'
              '2: Снять\n'
              '3: Выйти\n')
        choice = input('Введите номер действия: ').strip()
    return choice


def account_replenishment() -> None | object:  # Пополнение счета

    global summa, LIST, percent, count, TAX, operation
    print(f'Ваш баланс на данный момент составляет {summa}')
    if summa > 5_000_000:
        percent = TAX
    if count % 3 == 0:
        percent += 3
    print('Доступные варианты')
    [print(f'{v}', end='   ') if i != 2 and i != len(LIST) - 1 else print(
        f'{v}') for i, v in enumerate(LIST)]
    replenish = input('Введите число для пополнение: ').strip()
    while replenish not in LIST:
        print('Доступные варианты')
        [print(f'{v}', end='   ') if i != 2 and i != len(LIST) - 1 else print(
            f'{v}') for i, v in enumerate(LIST)]
        replenish = input('Введите число для пополнение: ').strip()
    if replenish.isdigit():
        if replenish in LIST:
            summa += int(replenish)
            print(f'Ваш баланс на данный момент составляет {summa}')
            count += 1
            operation.setdefault('Пополнение', []).append(replenish)
        else:
            print('Данное число не найдено')
    elif replenish == 'Другое':
        try:
            replenish = int(
                input("Введите другое число для пополнение: ").strip())
            summa += int(replenish)
            operation.setdefault('Пополнение', []).append(replenish)
            count += 1
            print(f'Ваш баланс на данный момент составляет {summa}')
        except ValueError:
            print('Был введён не корректный символ\nЗавершение программы...')
    elif replenish == 'Выход':
        return task_choice()


def account_withdrawal() -> None | object:  # Снятие денег
    global summa, LIST, percent, count, TAX, operation
    print(f'Ваш баланс на данный момент составляет {summa}')
    if summa > 5_000_000:
        percent = TAX
    if count % 3 == 0:
        percent += 3
    print('Доступные варианты')
    [print(f'{v}', end='   ') if i != 2 and i != len(LIST) - 1 else print(
        f'{v}') for i, v in enumerate(LIST)]
    replenish = input('Введите число для снятие наличных: ').strip()
    while replenish not in LIST:
        print('Доступные варианты')
        [print(f'{v}', end='   ') if i != 2 and i != len(LIST) - 1 else print(
            f'{v}') for i, v in enumerate(LIST)]
        replenish = input('Введите число снятие наличных: ').strip()
    if replenish.isdigit():
        if replenish in LIST:
            if summa - int(replenish) < 0:
                print("Не достаточно средств")
            else:
                replenish = int(replenish)
                summa -= replenish + (30 if (s := ((
                                                    replenish / 100) * percent))
                                                < 30 else 600 if s > 600 else s)
                summa = f'{summa:.2f}'
                summa = float(summa)
                operation.setdefault('Снятие', []).append(replenish)
                print(f'Ваш баланс на данный момент составляет {summa}')
                count += 1
        else:
            print('Данное число не найдено')
    elif replenish == 'Другое':
        try:
            replenish = int(
                input("Введите другое число снятие наличных: ").strip())
            if summa - int(replenish) < 0:
                print("Не достаточно средств")
            else:
                replenish = int(replenish)
                summa -= replenish + (30 if (s := ((
                                            replenish / 100) * percent))
                                            < 30 else 600 if s > 600 else s)
                summa = f'{summa:.2f}'
                summa = float(summa)
                operation.setdefault('Снятие', []).append(replenish)
                count += 1
                print(f'Ваш баланс на данный момент составляет {summa}')
        except ValueError:
            print('Был введён не корректный символ\nЗавершение программы...')
    elif replenish == 'Выход':
        return task_choice()


def action(num: str) -> object | str:
    if num == '1':
        return account_replenishment()
    elif num == '2':
        return account_withdrawal()
    else:
        return 'Завершение программы'


def main() -> object | str:
    flag = task_choice()
    while flag < '3':
        check = action(flag)
        if check is not None:
            flag = check
        else:
            flag = task_choice()

    else:
        print("Завершение программы")

main()
print(operation)
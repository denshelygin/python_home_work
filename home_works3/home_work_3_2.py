'''
Задание №2
Дан список повторяющихся элементов.
Вернуть список с дублирующимися элементами.
В результирующем списке не должно быть дубликатов.
'''

lst = [1, 1, 3, 5, 8, 2, 8, 5, 2]
new_lst = []
for item in lst:
    if lst.count(item) > 1 and item not in new_lst:
        new_lst.append(item)

print(new_lst)





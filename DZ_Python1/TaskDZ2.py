# Задача 18: Требуется найти в массиве A[1..N] самый близкий по
# величине элемент к заданному числу X. Пользователь в первой строке
# вводит натуральное число N – количество элементов в массиве. В
# последующих строках записаны N целых чисел Ai
# . Последняя строка
# содержит число X
# 5
# 1 2 3 4 5
# 6
# -> 5

input() # Введите кол-во элементов списка
lst = sorted(list(map(int, input().split()))) # Ввести через пробел элементы списка
x = int(input())
elem = 0
for i in lst:
    if i < x:
        elem = i
print(elem)
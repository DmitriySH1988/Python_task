# Задача 10: На столе лежат n монеток. Некоторые из них лежат вверх
# решкой, а некоторые – гербом. Определите минимальное число
# монеток, которые нужно перевернуть, чтобы все монетки были
# повернуты вверх одной и той же стороной. Выведите минимальное
# количество монет, которые нужно перевернуть.
# 5 -> 1 0 1 1 0
# 2

import random

n = int(input('Введите число: '))
list1 = []
for i in range(n):
    list1.append(random.randint(0,1))
print(*list1)

o = 0
r = 1
count1 = 0
count2 = 0
for i in list1:
    if i == o:
        count1+=1
    elif i == r:
        count2+=1
if count1 < count2:
    print(count1)
else:
    print(count2)

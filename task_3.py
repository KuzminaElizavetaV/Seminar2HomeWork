'''Задача 3. Реализуйте алгоритм перемешивания списка. Список размерностью 10 задается случайными целыми числами,
 выводится на экран, затем перемешивается, опять выводится на экран. SHUFFLE нельзя юзать '''

import random

list = [random.randint(1, 20) for _ in range(10)]
print(list)

for i in range(len(list)):
        index_aleatory = random.randint(0, len(list) - 1)
        temp = list[i]
        list[i] = list[index_aleatory]
        list[index_aleatory] = temp
print(list)

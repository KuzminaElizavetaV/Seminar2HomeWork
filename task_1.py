''' Задача 1. Напишите программу, которая принимает на вход вещественное или целое число и показывает сумму его
цифр. Через строку нельзя решать.
*Пример:*
- 6782 -> 23
- 0,56 -> 11 '''
try:
    num = input('Введите целое или дробное число:  ')
    sum = 0
    if num.find("."):
        num = float(num)
        while (num).is_integer() != True:
            num = num*10
        num = int(num)
        while num > 0:
            num_1 = num % 10
            sum = sum + num_1
            num //= 10
    else:
        num = int(num)
        while num > 0:
            num_1 = num % 10
            sum = sum + num_1
            num //= 10
    print(sum)
except:
    print('Введите целое или дробное число!!!')
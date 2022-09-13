# 2. Задайте два числа. Напишите программу, которая найдёт НОК (наименьшее общее кратное)
# этих двух чисел. НОК - наименьшее общее кратное, которое делится и на первое, и на второе
# число. 
 
number_1 = int(input('Введите первое число: '))
number_2 = int(input('Введите второе число: '))
if number_1 > number_2:
    max_number = number_1
    min_number = number_2
else:
    max_number = number_2
    min_number = number_1
if max_number % min_number == 0:
    nok = max_number
else:
    nok = max_number * min_number
print(f'Наименьшее общее кратное {number_1} и {number_2} равно {nok}.')

# 2. Напишите программу, которая будет принимать на вход дробь и показывать первую 
# цифру дробной части числа.
    
#     *Примеры:*
    
#     - 6,78 -> 7
#     - 5 -> нет
#     - 0,34 -> 3
namber = float (input('Введите число: '))

if namber == 0:
    print ('Нет')
else:
    namber = int(namber%1*10)
    print(namber)
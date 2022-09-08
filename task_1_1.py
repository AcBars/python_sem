# 2. Напишите программу, которая на вход принимает 5 чисел и находит максимальное из них.
    
#     Примеры:
    
#     - 1, 4, 8, 7, 5 -> 8
#     - 78, 55, 36, 90, 2 -> 90
nam_list = []
for _ in range (5):
    nam_list.append(int(input('Введите число:')))
temp = 0
for i in nam_list:
    if temp <= i:
        temp = i
print ('Из ', nam_list, 'самое большое это: ', temp)
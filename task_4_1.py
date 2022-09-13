# 1. Задайте строку из набора чисел. Напишите программу, которая покажет большее и
# меньшее число. В качестве символа-разделителя используйте пробел.
 

stroka_numbers = '1 3 45 56'
numbers_list = stroka_numbers.split(' ')
numbers_list_1 = [int(x) for x in numbers_list]
get_min = min(numbers_list_1)
get_max = max(numbers_list_1)
print(f'Максимальный элемент строки равен: {get_max}, минимальный элемент строки равен: {get_min}')

# 1. Напишите программу, которая будет на вход принимать число N и выводить числа 
# от -N до N
    
#     *Примеры:* 
    
#     - 5 -> -5, -4, -3, -2, -1, 0, 1, 2, 3, 4, 5

namber = int(input('Введите число: '))
if namber > 0:
    negative_number = namber * -1
    for _ in range(namber * 2 + 1):
        print (negative_number)
        negative_number += 1
elif namber < 0:
    negative_number = namber * -1
    for _ in range(namber * -2 + 1):
        print (negative_number)
        negative_number -= 1
else:
    print(namber)
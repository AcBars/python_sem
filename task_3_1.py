# 1. Задайте список. Напишите программу, которая определит, присутствует ли в заданном
# списке строк некое число.

from random import random
from random import randint
def word_cre():
    list_length = randint(2, 10)
    list_numbers = []
    for i in range(list_length):
        list_numbers.append(randint(1040, 1103))
    for i, char in enumerate(list_numbers):
        list_numbers[i] = chr(char)
    word = ("".join(map(str,list_numbers))) + str(randint(2, 10))
    return word
list_word = []
for i in range(randint(2,5)):
    list_word.append(word_cre())



for i in list_word:
    print(i)
    for j in i:
        if j.isdigit():
            print(f"Есть число: {j}")



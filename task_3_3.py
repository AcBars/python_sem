# 3. Удалите в целочисленном массиве все положительные числа, которые являются
# палиндромами.

from random import random
from random import randint
def word_cre():
    list_length = randint(2, 10)
    list_numbers = []
    for i in range(list_length):
        list_numbers.append(randint(1040, 1103))
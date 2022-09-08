# 2.Найти сумму элементов массива, лежащих между максимальным и минимальным по значению
# элементами


import random
arr = []
for _ in range(10):
    temp = random.randrange(0, 10)
    arr.append(temp)
print(arr)
temp = arr[0]
for i in arr:
    if temp > arr[i]:
        temp_max_index = i
temp = arr[0]
for i in arr:
    if temp < arr[i]:
        temp_min_index = i
arr_result = []
for temp_min_index in temp_max_index:
    i = 0
    arr_result[i] = arr
print(arr_result)
# 2. Напишите программу, которая определит позицию второго вхождения строки в списке
# либо сообщит, что её нет.



spisok = ["йцу", "фыв", "ячс", "цук", "йцукен", "цук", "йцу"]
perem = "цук"
index = 0
cont = 0
for i in spisok:
    if i == perem:
        index += 1
    if index == 2:
        break
    cont += 1
if index == 0:
    print(f'Значения "{perem}" нет в списке.')
else:
    print(f"ответ: {cont}")

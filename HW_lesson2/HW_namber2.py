el_count = int(input("Введите количество элементов списка: "))
_list = []
i = 0
el = 0
while i < el_count:
    _list.append(input("Введите следующее значение списка: "))
    i += 1

for el in range(int(len(_list) / 2)):
    _list[el], _list[el + 1] = _list[el + 1], _list[el]
    el += 2
print(_list)

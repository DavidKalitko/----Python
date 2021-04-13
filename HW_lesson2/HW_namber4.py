_str = input("введите строку: ")
_word = []
num = 1
for el in range(_str.count(' ') + 1):
    _word = _str.split()
    if len(str(_word)) <= 10:
        print(f" {num} {_word [el]}")
        num += 1
    else:
        print(f" {num} {_word [el] [0:10]}")
        num += 1

n = int(input("Введите целое положительное число: "))
_max = n % 10
while n >= 1:
    n = n // 10
    if n % 10 > _max:
        _max = n % 10
    if n > 9:
        continue
    else:
        print("Максимальное цифра в числе ", _max)
        break

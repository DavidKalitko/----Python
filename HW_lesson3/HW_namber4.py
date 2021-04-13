def my_func(x, y):
    try:
        x, y = float(x), int(y)
        if x <= 0 or y >= 0:
            return "Не коректный ввод данных"
        else:
            result = 1
            for _ in range(abs(y)):
                result /= x
                return f"Результат: {round(result, 6)}"
    except ValueError:
        return "Работа только с числам"


number1 = input("Введите действительное положительное число, x = ")
number2 = input("Введите целое отрицательное число, y = ")

print(my_func(number1, number2))

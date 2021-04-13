def division():
    while True:
        try:
            num1 = int(input("Введите 1-е число: "))
            num2 = int(input("Введите 2-е число: "))
            div = num1 / num2
            break
        except ValueError:
            print("Введите цифры")
        except ZeroDivisionError:
            print("Дилить на 0 нельзя")
    return div


print(f"Результат деления  {division()}")

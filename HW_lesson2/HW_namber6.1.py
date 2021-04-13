goods = int(input("Введите количество товара: "))
n = 1
my_dict = []
my_list = []
while n <= goods:
    my_dict = dict({'название': input("введите название: "), 'цена': input("Введите цену: "),
                    'количество': input('Введите количество: '), 'eд': input("Введите единицу измерения: ")})
    my_list.append((n, my_dict))
    n += 1
for i in my_list:
    print(i)

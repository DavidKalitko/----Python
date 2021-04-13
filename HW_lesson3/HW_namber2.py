def my_func(name, surname, year, city, email, telephone):
    return ' '.join([name, surname, year, city, email, telephone])


print(my_func(name=input('Здравствуйте, введите ваше Имя: '), surname=input('Фамилию: '), year=input('Год рождения: '),
              city=input('Название вашего города: '), email=input('Email: '), telephone=input('Номер телефона: ')))

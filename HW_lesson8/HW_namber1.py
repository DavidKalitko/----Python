class Data:
    def __init__(self, day_month_year):
        self.day_month_year = str(day_month_year)

    @classmethod
    def extract(cls, day_month_year):
        my_date = []
        for i in day_month_year.split():
            if i != '-': my_date.append(i)

        return int(my_date[0]), int(my_date[1]), int(my_date[2])

    @staticmethod
    def valid(day, month, year):

        if 1 <= day <= 31:
            if 1 <= month <= 12:
                if 2028 >= year >= 0:
                    return f'Проверка пройдена'
                else:
                    return f'Неправильный год'
            else:
                return f'Неправильный месяц'
        else:
            return f'Неправильный день'

    def __str__(self):
        return f'Текущая дата {Data.extract(self.day_month_year)}'


today = Data('21 - 1 - 2021')
print(today)
print(Data.valid(21, 11, 2029))
print(today.valid(16, 13, 2011))
print(Data.extract('21 - 8 - 2011'))
print(today.extract('17 - 11 - 2020'))
print(Data.valid(3, 10, 2019))

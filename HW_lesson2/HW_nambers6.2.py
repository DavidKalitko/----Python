goods = []
features = {'название': '', 'цена': '', 'количество': '', 'единица измерения': ''}
analytics = {'название': [], 'цена': [], 'количество': [], 'единица измерения': []}
num = 0
feature_ = None
control = None
while True:
    control = input("Для выхода нажмите 'Q', для продолжения нажмите 'Enter', для аналитики нажмите 'A'.").upper()
    if control == 'Q':
        break
    num += 1
    if control == 'A':
        print(f'\n Текущая аналитика \n {"-" * 30}')
        for key, value in analytics.items():
            print(f'{key[:25]:>25}: {value}')
            print("-" * 30)
    for f in features.keys():
        feature_ = input(f'Характеристика "{f}"')
        features[f] = int(feature_) if (f == 'цена' or f == 'количество') else feature_
        analytics[f].append(features[f])
    goods.append((num, features))

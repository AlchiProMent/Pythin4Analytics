# Кодирование меток

from sklearn import preprocessing
import pandas as pd

if __name__ == '__main__':

    # создать простой набор словесных меток
    labels = ['яблоко', 'шоколад', 'яблоко', 'виноград', 'шоколад', 'сыр', 'сахар']

    # Создать кодировщик
    encoder = preprocessing.LabelEncoder()
    # Обучить его
    encoder.fit(labels)

    # Вывести карту меток
    print('Карта меток:')
    for i, item in enumerate(encoder.classes_):
        print(f'{item} -> {i}')

    # Получить коды на основании словесных меток
    test_labels = ['виноград', 'яблоко', 'шоколад']
    encoded_values = encoder.transform(test_labels)
    print()
    print('Метки:', test_labels)
    print('Их коды:', encoded_values)

    # По кодам получить метки
    encoded_values = [2, 4, 0, 1]
    # Обратное преобразование
    decoded_lables = encoder.inverse_transform(encoded_values)
    print()
    print('Коды:', encoded_values)
    print('Соответствующие им метки:', decoded_lables)

    iris_file_name = 'iris.csv'
    # загрузить массив в DataFrame pandas
    df = pd.read_csv(iris_file_name, header=None)
    # получить метки
    lbl = df.values[:, -1]
    print()
    # обучить кодировщик на новых данных
    encoder.fit(lbl)
    print('Метки для набора IRIS')
    for i, item in enumerate(encoder.classes_):
        print(f'{item} -> {i}')








# МЕТОДЫ ПРЕДВАРИТЕЛЬНОЙ ОБРАБОТКИ ДАННЫХ
import numpy as np
from sklearn import preprocessing

if __name__ == '__main__':
    # тестовые данные
    input_data = np.array([[5.3, -1.4,  5.5],
                           [2.2,  7.8, -6.1],
                           [3.4,  0.3,  2.2],
                           [8.1, -8.8, -4.3]])

    # Бинаризация данных
    data_binarized = preprocessing.Binarizer(threshold=2.2).transform(input_data)
    print('Бинаризация данных:')
    print(data_binarized)
    print()

    # среднее и стандартное отклонение
    print('Исключение среднего')
    print('До обработки:')
    print('Среднее =', input_data.mean(axis=0))
    print('Стандартное отклонение =', input_data.std(axis=0))

    # удалить среднее
    data_scaled = preprocessing.scale(input_data)
    print('После обработки:')
    print('Среднее =', data_scaled.mean(axis=0))
    print('Стандартное отклонение =', data_scaled.std(axis=0))

    # Масштабирование

    # создать масштабатор
    scaler_minmax = preprocessing.MinMaxScaler(feature_range=(0, 1))
    # преобразовать данные
    data_scaled_minmax = scaler_minmax.fit_transform(input_data)
    print()
    print('Min max масштабирование:')
    print(data_scaled_minmax)
    print()

    # Нормализация

    d_l1 = preprocessing.normalize(input_data, norm='l1')
    d_l2 = preprocessing.normalize(input_data, norm='l2')
    print('L1 нормализация:')
    print(d_l1)
    print()
    print('L2 нормализация:')
    print(d_l2)
    print()

    # проверка данных

    # просмотреть все строки
    for i in range(d_l1.shape[0]):
       # получить очередную строку массива
       vect = d_l1[0,:]
       summa = 0.0
       # просуммировать абсолютные значения всех элементов строки
       for n in vect:
           summa += abs(n)
       print(f'{i}: {summa}')








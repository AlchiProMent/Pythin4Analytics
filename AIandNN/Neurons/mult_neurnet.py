# Построение многослойной нейронной сети

import numpy as np
import matplotlib.pyplot as plt
import neurolab as nl

if __name__ == '__main__':

    # Сгенерировать тренировочные данные
    min_val = -15
    max_val = 15
    num_points = 130
    # создать интервал размерностью num_points, начиная с min_val до max_val
    x = np.linspace(min_val, max_val, num_points)
    # y = 3 * x**2 + 5
    y = 3 * np.square(x) + 5
    y /= np.linalg.norm(y)

    # Создание данных и меток нужной мерности
    data = x.reshape(num_points, 1)
    labels = y.reshape(num_points, 1)

    # Визуализация данных
    plt.figure()
    plt.scatter(data, labels)
    plt.xlabel('Ось 1')
    plt.ylabel('Ось 2')
    plt.title('Входные данные')

    # Определение многослойной нейронной сети с двумя скрытыми слоями
    # Первый скрытый слой состоит из 10 нейронов, второй - из 6.
    # Выходной слой состоит из одного нейрона
    nn = nl.net.newff([[min_val, max_val]], [10, 6, 1])

    # В качестве обучающего алгоритма установить метод градиентного спуска
    nn.trainf = nl.train.train_gd

    # Обучение нейронной сети
    error_progress = nn.train(data, labels,
                              epochs=2000,      # количество эпох
                              show=100,         # интервал выводимых ошибок
                              goal=0.01)        # штраф за ошибку

    # Выполнение нейронной сети на тренировочных данных
    output = nn.sim(data)
    y_pred = output.reshape(num_points)

    # График прогресса обучения
    plt.figure()
    plt.plot(error_progress)
    plt.xlabel('Число эпох')
    plt.ylabel('Ошибки')
    plt.title('Прогресс в ошибке обучения')

    # создать дополнительный интервал
    x_dense = np.linspace(min_val, max_val, num_points * 2)
    # запустить нейронную сеть на новых данных для прогноза
    y_dense_pred = nn.sim(x_dense.reshape(x_dense.size,1)).reshape(x_dense.size)

    # График результата
    plt.figure()
    # На одном графике фактические и прогнозные значения
    plt.plot(x_dense, y_dense_pred, '-', x, y, '.', x, y_pred, 'p')
    plt.title('Фактические и прогнозные значения')

    # вывести все графики в конце программы
    plt.show()

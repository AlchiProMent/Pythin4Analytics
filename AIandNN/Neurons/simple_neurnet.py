# Построение однослойной нейронной сети

import numpy as np
import matplotlib.pyplot as plt
import neurolab as nl

if __name__ == '__main__':

    # Загрузить входные данные
    text = np.loadtxt('simple_nn.txt')

    # Поделить на данные и метки
    data = text[:, 0:2]
    labels = text[:, 2:]

    # Вывести данные
    plt.figure()
    plt.scatter(data[:,0], data[:,1])
    plt.xlabel('Ось 1')
    plt.ylabel('Ось 2')
    plt.title('Входные данные')
    #plt.show()

    # Минимальные и максимальные значения для каждого измерения
    dim1_min, dim1_max = data[:,0].min(), data[:,0].max()
    dim2_min, dim2_max = data[:,1].min(), data[:,1].max()

    # Количество нейронов в выходном слое
    num_output = labels.shape[1]

    dim1 = [dim1_min, dim1_max]
    dim2 = [dim2_min, dim2_max]

    # Создать однослойную нейронную сеть
    nn = nl.net.newp([dim1, dim2], num_output)

    # Тренировать сеть
    error_progress = nn.train(data, labels,
                              epochs=100,       # количество эпох
                              show=20,          # интервал нумерации ошибок
                              lr=0.03)          # параметр скорости настройки

    # Показать график прогресса обучения
    plt.figure()
    plt.plot(error_progress)
    plt.xlabel('Число эпох')
    plt.ylabel('Ошибки обучения')
    plt.title('Прогресс обучения')
    # вывести сетку
    plt.grid()


    # Запуск классификатор на тестовых точках данных ------------------

    # тестовые точки
    data_test = [[0.4, 4.3], [4.4, 0.6], [4.7, 8.1]]

    print('\nОпределение меток для тестовых точек:')
    for item in data_test:
        print(item, '-->', nn.sim([item])[0])

    plt.show()
    print('\nПрограмма завершила работу.')












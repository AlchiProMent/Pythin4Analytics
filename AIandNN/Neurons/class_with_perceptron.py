# Создание классификатора на основе персептрона

import numpy as np
import matplotlib.pyplot as plt

import neurolab as nl

if __name__ == '__main__':

    # Загрузить данные из файла
    text = np.loadtxt('for_perceptron.txt')

    # Выделить данные...
    data = text[:, :2]
    # ... и метки
    labels = text[:, 2].reshape((text.shape[0], 1))

    # Отобразить данные
    plt.figure()
    plt.scatter(data[:,0], data[:,1])
    plt.xlabel('Измерение 1')
    plt.ylabel('Измерение 2')
    plt.title('Входные данные')
    plt.show()

    # Минимальные и максимальные значения для каждого измерения
    dim1_min, dim1_max, dim2_min, dim2_max = 0, 1, 0, 1

    # Количество нейронов в выходном слое
    num_output = labels.shape[1]

    # Задать персептрон с двумя входными нейронами (поскольку у нас есть два измерения во входных данных)
    dim1 = [dim1_min, dim1_max]
    dim2 = [dim2_min, dim2_max]

    # создание однослойного персептрона
    perceptron = nl.net.newp([dim1, dim2], num_output)

    # Обучение персептрона на данных
    error_progress = perceptron.train(data, labels, epochs=100, show=20, lr=0.03)

    # Вывести прогресс тренировок
    plt.figure()
    plt.plot(error_progress)
    plt.xlabel('Количество эпох')
    plt.ylabel('Ошибки тренировки')
    plt.title('Прогресс обучения по количеству ошибок в эпохах')
    plt.grid()

    plt.show()









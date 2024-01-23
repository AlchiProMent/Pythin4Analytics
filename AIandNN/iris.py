# обучение персепторна на наборе Iris

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.colors import ListedColormap
from perceptron import Perceptron

def plot_decision_region(X, y, classifier, resolution=0.02):
    # вывести маркеры значений на закрашенном фоне; фон закрасить с применением обученного персептрона
    # настроить генератор маркеров и палитру
    markers = ['s', 'x', 'o', '^', 'v']
    colors = ['red', 'blue', 'lightgreen', 'gray', 'cyan']
    cmap = ListedColormap(colors[:len(np.unique(y))])

    # пространство для вывода графика
    x1_min, x1_max = X[:, 0].min() - 1, X[:, 0].max() + 1
    x2_min, x2_max = X[:, 1].min() - 1, X[:, 1].max() + 1
    # задать сетку
    xx1, xx2 = np.meshgrid(np.arange(x1_min, x1_max, resolution),
                           np.arange(x2_min, x2_max, resolution))

    # нарисовать контур; z - значение высот для контура. z рассчитывается при помощи обученного перцептрона
    narr = np.array([xx1.ravel(), xx2.ravel()])
    z = classifier.predict(narr.T)
    z = z.reshape(xx1.shape)
    plt.contourf(xx1, xx2, z, alpha=0.4, cmap=cmap)

    plt.xlim(xx1.min(), xx1.max())
    plt.ylim(xx2.min(), xx2.max())

    # образцы классов
    for ind, cl in enumerate(np.unique(y)):
        plt.scatter(x=X[y == cl, 0], y=X[y == cl, 1], alpha=0.8, color=cmap(ind), marker=markers[ind], label=cl)



if __name__ == '__main__':
    #
    iris_file_name = 'iris.csv'
    # загрузить массив в DataFrame pandas
    df = pd.read_csv(iris_file_name, header=None)

    # вывести 5 последних записей набора
    print(df.tail())

    # получить первый 100 меток класса в строковом формате
    y = df.iloc[0:100, 4].values
    # преобразовать их в -1 или 1
    y = np.where(y == 'Iris-setosa', -1, 1)

    # получить из набора IRIS 0-ю (длина чашелистника) и 2-ю колонки (длина лепестка) для ста первых строк
    X = df.iloc[0:100, [0, 2]].values

    # вывести маркеры первых 50 значений
    plt.scatter(X[:50, 0], X[:50, 1], color='red', marker='o', label='щетинистый')
    # вывести маркеры следующих 50 значений
    plt.scatter(X[50:100, 0], X[50:100, 1], color='blue', marker='x', label='разноцветный')

    plt.xlabel('Длина чашелистиника')
    plt.ylabel('Длина лепестка')
    plt.legend(loc='upper left')
    # открыть окно с графиком
    plt.show()

    # тренировка персептрона
    ppn = Perceptron(tempo=0.1, iter_count=10)
    # тренировка на ранее подготовленных данных
    ppn.fit(X, y)

    # вывести процесс изменения числа ошибок в процессе обучения персептрона
    plt.plot(range(1, len(ppn.errors)+1), ppn.errors, marker='o')
    plt.xlabel('Эпохи')
    plt.ylabel('Число случаев ошибочной классификации')
    plt.show()

    # запустить проверку обученного перцептрона
    plot_decision_region(X, y, classifier=ppn)
    plt.xlabel('длина чашелистника [см]')
    plt.ylabel('длина лепестка [см]')
    plt.legend(loc='upper left')
    plt.show()







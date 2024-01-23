# Кластеризация методом k-средних

import numpy as np
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans

if __name__ == '__main__':

    # загрузить данные из файла
    X = np.loadtxt('clustering_k_means.txt', delimiter=',')

    # Вывести данные на графике
    plt.figure()
    plt.scatter(X[:,0], X[:,1], marker='o', facecolors='cyan', edgecolors='black', s=80)
    x_min, x_max = X[:, 0].min() - 1, X[:, 0].max() + 1
    y_min, y_max = X[:, 1].min() - 1, X[:, 1].max() + 1
    plt.title('Входные данные')
    plt.xlim(x_min, x_max)
    plt.ylim(y_min, y_max)
    plt.xticks(())
    plt.yticks(())
    plt.show()

    # Создать модель кластеризации методом k-средних
    num_clusters = 5
    kmeans = KMeans(init='k-means++', n_clusters=num_clusters, n_init=10)
    # Обучить модель кластеризации
    kmeans.fit(X)

    # Сетка графика
    step_size = 0.01
    x_min, x_max = X[:, 0].min() - 1, X[:, 0].max() + 1
    y_min, y_max = X[:, 1].min() - 1, X[:, 1].max() + 1
    x_vals, y_vals = np.meshgrid(np.arange(x_min, x_max, step_size), np.arange(y_min, y_max, step_size))

    # Прогнозирование выходных меток для всех точек сетки
    output = kmeans.predict(np.c_[x_vals.ravel(), y_vals.ravel()])

    # Построить различные сектора и раскрасить их

    output = output.reshape(x_vals.shape)
    plt.figure()
    plt.clf()

    # Отобразить данные в виде изображения на 2D-растре
    # interpolation - интерполяция при масштабировании изображения
    plt.imshow(output, interpolation='nearest', extent=(x_vals.min(), x_vals.max(),
                                                        y_vals.min(), y_vals.max()),
               cmap=plt.cm.Paired,      # выбор цветовой карты
               aspect='auto',           # соотношение сторон осей
               origin='lower')          # положение точки 0,0

    # Наложение входных точек
    plt.scatter(X[:,0], X[:,1], marker='o', facecolors='none', edgecolors='black', s=80)

    # Центры кластеров
    cluster_centers = kmeans.cluster_centers_
    plt.scatter(cluster_centers[:,0], cluster_centers[:,1],
                marker='o', s=100, linewidths=2, facecolors='red', color='yellow', zorder=12)

    x_min, x_max = X[:, 0].min() - 1, X[:, 0].max() + 1
    y_min, y_max = X[:, 1].min() - 1, X[:, 1].max() + 1
    plt.title('Границы кластеров')
    plt.xlim(x_min, x_max)
    plt.ylim(y_min, y_max)
    plt.xticks(())
    plt.yticks(())

    plt.show()
















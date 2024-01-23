# Оценка количества кластеров с использованием метода сдвига среднего

import numpy as np
import matplotlib.pyplot as plt

from sklearn.cluster import MeanShift, estimate_bandwidth

if __name__ == '__main__':

    # Загрузить данные
    X = np.loadtxt('clustering_k_means.txt', delimiter=',')

    # Оценить пропускную способность X; quantile - использование квантиля, n_samples - количество образцов для оценки
    bandwidth_X = estimate_bandwidth(X, quantile=0.1, n_samples=len(X))

    # Создать модель кластеризации методом сдвига среднего
    meanshift_model = MeanShift(bandwidth=bandwidth_X, bin_seeding=True)
    # Обучить
    meanshift_model.fit(X)

    # Извлечь центры кластеров
    cluster_centers = meanshift_model.cluster_centers_
    print('Центры кластеров:')
    print(cluster_centers)

    # Оценка количества кластеров
    labels = meanshift_model.labels_
    num_clusters = len(np.unique(labels))
    print('\nЧисло кластеров во входных данных:', num_clusters)

    # Создать график
    plt.figure()
    markers = 'o*xvs'

    # перебрать кластеры
    for i, marker in zip(range(num_clusters), markers):
        # точки, принадлежащие текущему кластеру
        plt.scatter(X[labels==i, 0], X[labels==i, 1], marker=marker, color='green')
        # Центры кластеров
        cluster_center = cluster_centers[i]
        # оркужность...
        plt.plot(cluster_center[0], cluster_center[1], marker='o',
                 markerfacecolor='yellow', markeredgecolor='red', markersize=12)
        # ...с точкой посредине
        plt.plot(cluster_center[0], cluster_center[1], marker='o', markerfacecolor='red', markersize=1)

    plt.title('Кластеры')
    plt.show()













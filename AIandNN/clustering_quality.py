# Оценка качества кластеризации с помощью силуэтных оценок

import numpy as np
import matplotlib.pyplot as plt
from sklearn import metrics
from sklearn.cluster import KMeans

if __name__ == '__main__':

    # Загрузить данные
    X = np.loadtxt('clustering_quality.txt', delimiter=',')

    # Вывести данные на графике
    plt.figure()
    plt.scatter(X[:, 0], X[:, 1], color='blue', s=80, marker='o', facecolors='none')
    x_min, x_max = X[:, 0].min() - 1, X[:, 0].max() + 1
    y_min, y_max = X[:, 1].min() - 1, X[:, 1].max() + 1
    plt.title('Входные данные')
    plt.xlim(x_min, x_max)
    plt.ylim(y_min, y_max)
    plt.xticks(())
    plt.yticks(())
    plt.show()

    # Инициализация переменных
    scores = []
    values = np.arange(2, 10)

    # Перебрать указанные диапазон
    for num_clusters in values:
        # Создать модель кластеризации методом k-средних
        kmeans = KMeans(init='k-means++', n_clusters=num_clusters, n_init=10)
        # обучить модель
        kmeans.fit(X)

        # средний коэффициент силуэта всех образцов
        score = metrics.silhouette_score(X, kmeans.labels_, metric='euclidean', sample_size=len(X))

        print('\nКоличество кластеров:', num_clusters)
        print('Оценка силуэта:', score)

        # Добавить текущую оценку в список оценок
        scores.append(score)

    # График оценки силуэта
    plt.figure()
    plt.bar(values, scores, width=0.7, align='center')
    plt.title('Оценка силуэта в зависимости от количества кластеров')
    plt.show()

    # Извлечь лучший результат и оптимальное количество кластеров
    num_clusters = np.argmax(scores) + values[0]
    print('\nОптимальное число кластеров:', num_clusters)









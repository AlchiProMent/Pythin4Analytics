# Классификатор на основе смешанной гауссовской модели

import numpy as np
import matplotlib.pyplot as plt
from matplotlib import patches

from sklearn import datasets
from sklearn.mixture import GaussianMixture as GMM
from sklearn.model_selection import StratifiedKFold

if __name__ == '__main__':

    # Загрузить набор данных Iris
    iris = datasets.load_iris()

    # Разделить набор данных на обучаемый и тестовый
    indices = StratifiedKFold(n_splits=5)
    # Получить первый обучающий и тестовый набор
    train_index, test_index = next(iter(indices.split(iris.data, iris.target)))

    # Извлечь обучающие данные и метки
    X_train = iris.data[train_index]
    y_train = iris.target[train_index]
    # Извлечь тестовые данные и метки
    X_test = iris.data[test_index]
    y_test = iris.target[test_index]

    # Получить количество кластеров
    num_classes = len(np.unique(y_train))

    # Создать GMM классификатор
    classifier = GMM(n_components=num_classes,      # Количество компонент в базовом распределении
                     covariance_type='full',        # Тип используемых ковариационных параметров
                     init_params='k-means++',       # Метод k-means++ для инициализации весов, средних значений и точности
                     max_iter=20,                   # Количество итераций EM-алогритма
                     random_state=0)

    # Инициализация средних GMM
    classifier.means_init = np.array([X_train[y_train == i].mean(axis=0) for i in range(num_classes)])
    # Обучение GMM классификатора
    classifier.fit(X_train)

    # Создать заготовку для графика
    plt.figure()
    # задать 3 цвета, поскольку в исходном наборе 3 субнабора
    colors = 'bgr'
    for i, color in enumerate(colors):
        # Получить собственные значения и собственные векторы
        eigenvalues, eigenvectors = np.linalg.eigh(classifier.covariances_[i][:2, :2])

        # Нормализовать первый собственный вектор
        norm_vec = eigenvectors[0] / np.linalg.norm(eigenvectors[0])

        # Расчет угла наклона эллипса для более точного отображения
        angle = np.arctan2(norm_vec[1], norm_vec[0])
        angle = 180 * angle / np.pi

        # Коэффициент масштабирования для увеличения эллипсов
        # (случайное значение, выбранное пробным путем)
        scaling_factor = 8
        eigenvalues *= scaling_factor

        # Вычертить эллипс
        ellipse = patches.Ellipse(xy=classifier.means_[i, :2],  # xy координаты центра эллипса
                                  width=eigenvalues[0],         # диаметр по горизонталти
                                  height=eigenvalues[1],        # диаметр по вертикали
                                  angle=180 + angle,            # Вращение в градусах против часовой стрелки
                                  color=color)                  # цвет

        axis_handle = plt.subplot(1, 1, 1)
        ellipse.set_clip_box(axis_handle.bbox)
        ellipse.set_alpha(0.6)
        axis_handle.add_artist(ellipse)

    # Поверх элипсов наложить данные
    for i, color in enumerate(colors):
        cur_data = iris.data[iris.target == i]
        plt.scatter(cur_data[:, 0], cur_data[:, 1], marker='o',
                    facecolors='none', edgecolors='black', s=40,
                    label=iris.target_names[i])

        test_data = X_test[y_test == i]
        plt.scatter(test_data[:, 0], test_data[:, 1], marker='s',
                    facecolors='black', edgecolors='black', s=40,
                    label=iris.target_names[i])


    print()
    # Вычисление прогнозов для данных обучения и тестирования
    y_train_pred = classifier.predict(X_train)
    accuracy_training = np.mean(y_train_pred.ravel() == y_train.ravel()) * 100
    print('Точность тренировочных данных:', accuracy_training)

    y_test_pred = classifier.predict(X_test)
    accuracy_testing = np.mean(y_test_pred.ravel() == y_test.ravel()) * 100
    print('Точность тестовых обучения:', accuracy_testing)

    plt.title('GMM классификатор')
    plt.xticks(())
    plt.yticks(())

    plt.show()























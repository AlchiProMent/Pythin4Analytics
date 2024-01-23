# Логический классификатор
import numpy as np
from sklearn import linear_model
import matplotlib.pyplot as plt

def show_class_res(classifier, X, y, title=''):
    # Визуализация работы классификатора на данных X с метками y
    # Определите минимальные и максимальные значения X и Y, которые будут использоваться в сетке
    min_x, max_x = X[:, 0].min() - 1.0, X[:, 0].max() + 1.0
    min_y, max_y = X[:, 1].min() - 1.0, X[:, 1].max() + 1.0

    # размер шага для построения сетки
    mesh_step_size = 0.01

    # Определите сетку для значений X и Y
    x_vals, y_vals = np.meshgrid(np.arange(min_x, max_x, mesh_step_size), np.arange(min_y, max_y, mesh_step_size))

    # Запустить классификатор
    output = classifier.predict(np.c_[x_vals.ravel(), y_vals.ravel()])

    # Изменить форму выходного массива
    output = output.reshape(x_vals.shape)

    # Создать график
    plt.figure()
    # заголовок графика
    plt.title(title)

    # Выбор цветовой гаммы
    plt.pcolormesh(x_vals, y_vals, output, cmap=plt.cm.gray)

    # Наложение тренировочных точек на график
    plt.scatter(X[:, 0], X[:, 1], c=y, s=75, edgecolors='black', linewidth=1, cmap=plt.cm.Paired)

    # Границы пространства
    plt.xlim(x_vals.min(), x_vals.max())
    plt.ylim(y_vals.min(), y_vals.max())

    # Метки по осячм X и Y
    plt.xticks((np.arange(int(X[:, 0].min() - 1), int(X[:, 0].max() + 1), 1.0)))
    plt.yticks((np.arange(int(X[:, 1].min() - 1), int(X[:, 1].max() + 1), 1.0)))

    # Вывести график в отдельном окне
    plt.show()



if __name__ == '__main__':
    # Входные данные (12 образцов)
    X = np.array([[3.1, 7.2],
                  [4, 6.7],
                  [2.9, 8],
                  [5.1, 4.5],
                  [6, 5],
                  [5.6, 5],
                  [3.3, 0.4],
                  [3.9, 0.9],
                  [2.8, 1],
                  [0.5, 3.4],
                  [1, 4],
                  [0.6, 4.9]])

    # метки (12 меток)
    y = np.array([0, 0, 0, 1, 1, 1, 2, 2, 2, 3, 3, 3])

    # Создать классификатор логистической регрессии
    classifier = linear_model.LogisticRegression(solver='liblinear', C=1)

    # Тренировать классификатор
    classifier.fit(X, y)

    # Визуализировать данные
    show_class_res(classifier, X, y)




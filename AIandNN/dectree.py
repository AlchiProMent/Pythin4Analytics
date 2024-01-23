# Создание классификатора на основе дерева принятия решений

import numpy as np
import matplotlib.pyplot as plt

# импортировать классификатор дерева решений (класс)
from sklearn.tree import DecisionTreeClassifier

from sklearn.metrics import classification_report
from sklearn import model_selection

from log_regress import show_class_res

if __name__ == '__main__':

    # входные данные
    input_file = 'dectrees.txt'
    data = np.loadtxt(input_file, delimiter=',')
    # массивы для обработки
    X, y = data[:, :-1], data[:, -1]

    # сепарация данных на два класса в зависимости от целевых меток
    class_0 = np.array(X[y == 0])
    class_1 = np.array(X[y == 1])

    # визуализация входных данных
    plt.figure()
    plt.scatter(class_0[:, 0], class_0[:, 1], s=75, facecolors='black', linewidth=1, marker='x')
    plt.scatter(class_1[:, 0], class_1[:, 1], s=75, facecolors='yellow', edgecolors='black', linewidth=1, marker='o')
    plt.title('Входные данные')
    plt.show()

    # разбиение данных на обучающий и тестовый наборы
    X_train, X_test, y_train, y_test = model_selection.train_test_split(X, y, test_size=.25, random_state=5)

    # параметры классификатора
    params = {'random_state': 0,   # Управляет случайностью оценки
              'max_depth': 4}      # Максимальная глубина дерева

    # Создать классификатор дерева решений
    classifier = DecisionTreeClassifier(**params)
    # Обучить на тренировочных данных
    classifier.fit(X_train, y_train)
    # предсказать выходной результат на основе тестового набора
    y_test_pred = classifier.predict(X_test)

    show_class_res(classifier, X_train, y_train, 'Тренировочный набор данных')
    show_class_res(classifier, X_test, y_test, 'Тестовый набор данных')

    # оценка работы классификатора

    class_names = ['Class-0', 'Class-1']

    print('\nРезультаты классификатора на тренировочном наборе\n')
    print(classification_report(y_train, classifier.predict(X_train), target_names=class_names))
    print()
    print('\nРезультаты классификатора на тестовом наборе\n')
    print(classification_report(y_test, y_test_pred, target_names=class_names))

    print('___________')
    print('Precision - точность')
    print('Recall - полнота (процентная доля количества извлеченных элементов к общему количеству)')
    print('f1-score - гармоническое среднее показателей точности и полноты')
















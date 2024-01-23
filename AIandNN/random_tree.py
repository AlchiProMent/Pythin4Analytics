# Создание классификаторов на основе случайных и предельно случайных лесов

import numpy as np
import matplotlib.pyplot as plt

from sklearn import model_selection
from sklearn.metrics import classification_report

from sklearn.ensemble import RandomForestClassifier, ExtraTreesClassifier

from log_regress import show_class_res


def input_code(menu_items:dict):
    # выбор пункта меню
    print('Введите номер модели:')
    print('--------------------')
    for key, item in menu_items.items():
        print(f'[ {key} ] {item}')
    return input('Ваш выбор: ')


if __name__ == '__main__':

    # сделать выбор из меню
    code_type = input_code({1:'Предельный лес', 2:'Предельно случайный лес'})

    # Загрузить данные
    input_file = 'randomtree.txt'
    data = np.loadtxt(input_file, delimiter=',')
    X, y = data[:, :-1], data[:, -1]

    # Разделить взодной массив данных на три класса в соответствии с метками
    class_0 = np.array(X[y==0])
    class_1 = np.array(X[y==1])
    class_2 = np.array(X[y==2])

    # Визуализировать взодные данные
    plt.figure()
    plt.scatter(class_0[:, 0], class_0[:, 1], s=75, facecolors='cyan', edgecolors='black', linewidth=1, marker='s')
    plt.scatter(class_1[:, 0], class_1[:, 1], s=75, facecolors='yellow', edgecolors='black', linewidth=1, marker='o')
    plt.scatter(class_2[:, 0], class_2[:, 1], s=75, facecolors='red', edgecolors='black', linewidth=1, marker='^')
    plt.title('Входные данные')
    plt.show()

    # Разделить данные на тренировочный и тестовый наборы
    X_train, X_test, y_train, y_test = model_selection.train_test_split(X, y, test_size=0.25, random_state=5)

    params = {'n_estimators': 100,  # количество создаваемых деревьев
              'max_depth': 4,       # максимальная глубина каждого дерева
              'random_state': 0}    # пусковое значение для генератора случайных чисел

    # Классификатор ансамблевого обучения
    if code_type == '1':
        # Случайнй лес
        classifier = RandomForestClassifier(**params)
    else:
        # Предельно случайный лес
        classifier = ExtraTreesClassifier(**params)

    print('\nОбучение классификатора...')
    # Обучение классификатора
    classifier.fit(X_train, y_train)

    # Показать результат обучения на тренировочных данных
    show_class_res(classifier, X_train, y_train, 'Тренировочные данные')

    # Сделать прогноз на тестовом наборе
    print('Прогноз на тестовом наборе...')
    y_test_pred = classifier.predict(X_test)
    # Показать результат прогноза
    show_class_res(classifier, X_test, y_test, 'Тестовый набор')

    # Оценка классификатора
    class_names = ['Class-0', 'Class-1', 'Class-2']
    print("\nОценка на тренировочных данных\n")
    print(classification_report(y_train, classifier.predict(X_train), target_names=class_names))

    print("\nОценка на тестовых данных\n")
    print(classification_report(y_test, y_test_pred, target_names=class_names))

    # Оценка достоверности прогнозов -------------------------------------------------

    # тестовые точки
    test_datapoints = np.array([[5, 5], [3, 6], [6, 4], [7, 2], [4, 4], [5, 2]])

    for datapoint in test_datapoints:
        # вызов метода для вычисления уровня доверительности
        probabilities = classifier.predict_proba([datapoint])[0]
        # argmax возвращает индекс максимального элемента
        predicted_class = f'Class-{np.argmax(probabilities)}'
        print('\nТочка:', datapoint)
        print('Прогнозируемый класс:', predicted_class)

    # Показать график с тестовыми точками
    show_class_res(classifier, test_datapoints, [0]*len(test_datapoints), 'Тестовые точки')











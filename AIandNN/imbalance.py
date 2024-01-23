# Обработка дисбаланса классов на основе  предельно случайного леса
import numpy as np
import matplotlib.pyplot as plt
from sklearn.ensemble import ExtraTreesClassifier
from sklearn import model_selection
from sklearn.metrics import classification_report

from log_regress import show_class_res

# импротировать функцию для вывода меню
from random_tree import input_code

import warnings
# игнорировать предупреждения
warnings.filterwarnings('ignore')

if __name__ == '__main__':

    # Загрузить данные
    input_file = 'imbalance.txt'
    data = np.loadtxt(input_file, delimiter=',')
    X, y = data[:, :-1], data[:, -1]

    # Разделить данные на классы
    class_0 = np.array(X[y==0])
    class_1 = np.array(X[y==1])

    # Визуализация входных данных
    plt.figure()
    plt.scatter(class_0[:, 0], class_0[:, 1], s=75, facecolors='black', linewidth=1, marker='x')
    plt.scatter(class_1[:, 0], class_1[:, 1], s=75, facecolors='yellow', edgecolors='black', linewidth=1, marker='o')
    plt.title('Входные данные')
    plt.show()

    # Разделить данные на тренировочные и тестовые
    X_train, X_test, y_train, y_test = model_selection.train_test_split(X, y, test_size=0.25, random_state=5)

    if input_code({1:'Учитывать дисбаланс классов', 2:'Не учитывать'}) == '1':
        params = {'n_estimators': 100, 'max_depth': 4, 'random_state': 0, 'class_weight': 'balanced'}
    else:
        params = {'n_estimators': 100, 'max_depth': 4, 'random_state': 0}

    # создать классификатор предельно случайного леса
    classifier = ExtraTreesClassifier(**params)
    print('Обучение модели...')
    classifier.fit(X_train, y_train)
    show_class_res(classifier, X_train, y_train, 'Тренировочные данные')
    show_class_res(classifier, X_test, y_test, 'Тестовые данные')

    print('Модель делает прогноз...')
    y_test_pred = classifier.predict(X_test)

    # Производительность классификатора
    class_names = ['Class-0', 'Class-1']
    print("\nПроизводительность классификатора в наборе обучающих данных\n")
    print(classification_report(y_train, classifier.predict(X_train), target_names=class_names))

    print("\nПроизводительность классификатора в наборе тестовых данных\n")
    print(classification_report(y_test, y_test_pred, target_names=class_names))








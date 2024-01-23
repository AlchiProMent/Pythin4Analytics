# Наивный байесовский классификатор
import numpy as np
from sklearn.naive_bayes import GaussianNB
from sklearn import model_selection

from log_regress import show_class_res

if __name__ == '__main__':
    file_name = 'data_nb.txt'

    # загрузить данные
    try:
        data = np.loadtxt(file_name, delimiter=',')
    except:
        print(f'Ошибка открытия файла "{file_name}"')
    else:
        X, y = data[:, :-1], data[:, -1]

        # создание наивного байесовского классификатора
        classifier = GaussianNB()
        # Обучение
        classifier.fit(X, y)
        # прогнозирование значение на
        y_pred = classifier.predict(X)

        # вычисление качества классификатора
        accuracy = 100.0 * (y == y_pred).sum() / X.shape[0]
        print(f'Точность наивного байесовского классификатора = {round(accuracy, 2)}%')

        # визуализация работы классификатора
        show_class_res(classifier, X, y)

        # попытка более точного предсказания ------------------------------

        # разбивка данных на обучающий и тестовый наборы
        X_train, X_test, y_train, y_test = model_selection.train_test_split(X, y, test_size=0.2, random_state=3)

        # создать новый гауссовский НБК
        classifier_new = GaussianNB()
        # тренировка
        classifier_new.fit(X_train, y_train)
        # прогноз
        y_test_pred = classifier_new.predict(X_test)

        # качества классификатора
        accuracy = 100.0 * (y_test == y_test_pred).sum() / X_test.shape[0]
        print(f'Точность нового наивного байесовского классификатора = {round(accuracy, 2)}%')

        # визуализация работы классификатора
        show_class_res(classifier, X_test, y_test)

        #
        # вычисление качества (accuracy), точности (precision) и полноты (recall) классификатора
        # на основании тройной перекрестной проверки
        #

        # трехкратная проверка (для значения cv=)
        num_folds = 3

        # вычисление качества (accuracy); scoring - тип оценки
        accuracy_values = model_selection.cross_val_score(classifier, X, y, scoring='accuracy', cv=num_folds)
        print(f'Качество = {str(round(100 * accuracy_values.mean(), 2))}%')

        # вычисление точности (precision)
        precision_values = model_selection.cross_val_score(classifier, X, y, scoring='precision_weighted', cv=num_folds)
        print(f'Точность = {str(round(100 * precision_values.mean(), 2))}%')

        # вычисление полноты (recall)
        recall_values = model_selection.cross_val_score(classifier, X, y, scoring='recall_weighted', cv=num_folds)
        print(f'Полнота = {str(round(100 * recall_values.mean(), 2))}%')

        # сбалансированный F-показатель или F-мера
        f1_values = model_selection.cross_val_score(classifier, X, y, scoring='f1_weighted', cv=num_folds)
        print(f'Cреднее гармоническое значение точности и полноты = {str(round(100 * f1_values.mean(), 2))}%')







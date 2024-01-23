# Многомерный регрессор

import numpy as np
from sklearn import linear_model
import sklearn.metrics as sm
from sklearn.preprocessing import PolynomialFeatures

if __name__ == '__main__':

    # входной файл данных
    input_file = 'multivar_regr_data.txt'

    # загрузка данных
    data = np.loadtxt(input_file, delimiter=',')
    X, y = data[:, :-1], data[:, -1]

    # разбивка данных на обучающий и тестовый наборы
    num_training = int(0.8 * len(X))
    num_test = len(X) - num_training

    # тренировочные данные
    X_train, y_train = X[:num_training], y[:num_training]
    # тестовые данные
    X_test, y_test = X[num_training:], y[num_training:]

    # создание модели линейного регрессора
    linear_regressor = linear_model.LinearRegression()
    # Обучение модели
    linear_regressor.fit(X_train, y_train)
    # Прогноз
    y_test_pred = linear_regressor.predict(X_test)

    # измерение метрических характеристик
    print('Метрики линейного регерссора:\n')

    # вычисляет среднюю абсолютную ошибку, как сумму абсолютных значений i-x ошибок, деленную на длину последовательности
    print('Средняя абсолютная ошибка =', round(sm.mean_absolute_error(y_test, y_test_pred), 2))

    # вычисляет среднеквадратичную ошибку, как сумму квадратов i-x ошибок, деленную на длину последовательности
    print('Среднеквадратическая ошибка =', round(sm.mean_squared_error(y_test, y_test_pred), 2))

    # медиана упорядоченной последовательности всех i-x ошибок
    print('Средняя (медиана) абсолютная ошибка =', round(sm.median_absolute_error(y_test, y_test_pred), 2))

    # Измеряет пропорцию, в которой математическая модель объясняет вариацию (дисперсию) данного набора данных
    print('Оценка объясненной дисперсии =', round(sm.explained_variance_score(y_test, y_test_pred), 2))
    # Наилучший возможный показатель — 1.0; чем ниже значение, тем хуже.

    # представляет собой долю дисперсии (у), которая была объяснена независимыми переменными в модели
    print('Коэффициент детерминации (функция оценки регрессии) =', round(sm.r2_score(y_test, y_test_pred), 2))

    # Полиномиальная регрессия
    polynomial = PolynomialFeatures(degree=10)
    X_train_transformed = polynomial.fit_transform(X_train)
    datapoint = [[7.75, 6.35, 5.56]]
    poly_datapoint = polynomial.fit_transform(datapoint)

    poly_liner_model = linear_model.LinearRegression()
    poly_liner_model.fit(X_train_transformed, y_train)

    print('\nЛинейная регрессия:\n', linear_regressor.predict(datapoint))
    print('\nПолиномиальная регрессия:\n', poly_liner_model.predict(poly_datapoint))







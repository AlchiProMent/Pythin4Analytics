# Создание регрессора одной переменной
import pickle

import numpy as np
from sklearn import linear_model
import sklearn.metrics as sm
import matplotlib.pyplot as plt

if __name__ == '__main__':

    # файл входных данных
    file_name = 'singlevar_regr_data.txt'
    # файл для сохранения модели
    output_model_file = 'model.pkl'

    # загрузка данных
    data = np.loadtxt(file_name, delimiter=',')
    # получить срезы для входных и выходных данных
    X, y = data[:, :-1], data[:, -1]

    # разбить данные на обучающий и тестовый набор
    num_training = int(0.8 * len(X))
    num_test = len(X) - num_training
    # тренировочные данные
    X_train, y_train = X[:num_training], y[:num_training]
    # тестовые данные
    X_test, y_test = X[num_training:], y[num_training:]

    # создание объекта линейного регрессора
    regressor = linear_model.LinearRegression()
    # обучение модели с использованием обучающего набора
    regressor.fit(X_train, y_train)

    # прогнозирование результата
    y_test_pred = regressor.predict(X_test)

    # построить и показать график
    plt.scatter(X_test, y_test, color='blue')
    plt.plot(X_test, y_test_pred, color='black', linewidth=4)
    plt.xticks()
    plt.yticks()
    plt.show()

    # вычисление метрических характеристик
    print('Метрики линейного регрессора:')

    # метрика ошибок между парными наблюдениями, выражающими одно и то же явление
    print('Средняя абсолютная ошибка =', round(sm.mean_absolute_error(y_test, y_test_pred), 2))

    # метрика риска, соответствующая ожидаемому значению квадратичной ошибки или потерь
    print('Среднеквадратичная ошибка =', round(sm.mean_squared_error(y_test, y_test_pred), 2))

    #  Потери рассчитываются путем взятия медианы всех абсолютных различий между целью и прогнозом
    print('Медиана ошибки =', round(sm.median_absolute_error(y_test, y_test_pred), 2))

    # функция оценки дисперсионной регрессии
    print('Дисперсия =', round(sm.explained_variance_score(y_test, y_test_pred), 2))

    # функция оценки регрессии (коэффициент детерминации) R в квадрате (1.0 - наилучший вариант)
    print('Коэффициент детерминации =', round(sm.r2_score(y_test, y_test_pred), 2))

    # Сохранение модели
    with open(output_model_file, 'wb') as f2:
        pickle.dump(regressor, f2)

    # здесь мог быть самый разный код . . .

    # загрузка модели
    with open(output_model_file, 'rb') as f3:
        regressor_model = pickle.load(f3)


    # получение прогноза на тестовом наборе данных с использованием загруженной модели
    y_test_pred_new = regressor_model.predict(X_test)

    print()
    print(f'Средняя абсолютная ошибка в новой модели = {round(sm.mean_absolute_error(y_test, y_test_pred_new), 2)}')




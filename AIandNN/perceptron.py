# Класс персептрона
import numpy as np

class Perceptron:
    def __init__(self, tempo=0.01, iter_count=10):
        # инициализация объекта; tempo - тем оубчения (от 0.0 до 1.0); iter_count - количество итераций
        self.eta = tempo
        self.iter_count = iter_count

    def net_input(self, X):
        # рассчитывает "чистый вход" через скалярное произведение двух массивов
        return np.dot(X, self.w[1:]) + self.w[0]

    def predict(self, X):
        # возвращает метку класса после единичного "скачка"
        return np.where(self.net_input(X) >= 0.0, 1, -1)

    def fit(self, X, y):
        # подгонка модели; X и y - массивы

        # создать массив "весов", первоначально заполненный нулями; размер массива w на 1 больше количества колонок X
        self.w = np.zeros(X.shape[1] + 1)
        # список для зранения числа ошибьок на каждой итерации выделения классов (первоначально - пустой)
        self.errors = []

        for i in range(self.iter_count):
            # счтчик числа ошибок на данной итерации
            errors = 0

            # расчитать веса
            for xi, target in zip(X, y):
                update = self.eta * (target - self.predict(xi))
                self.w[1:] += update * xi
                self.w[0] += update
                # увеличить число ошибок на единицу, если update не равно 0.0
                errors += int(update != 0.0)

            # добавить количество ошибок на данной итерации в список ошибок
            self.errors.append(errors)

        return self



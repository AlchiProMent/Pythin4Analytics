# Создание сверточной нейронной сети для распознования образов
# Множественная классификация с набором данных MNIST

from tensorflow import keras as krs
import matplotlib.pyplot as plt
import numpy as np

import os
# не отображать сообщения уровней INFO и WARNING для tensorflow
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'


def display_probabilities(prediction, ind):
    print(f'Вероятность для буквы с индексом {ind}')
    for index, probability in enumerate(prediction):
        print(f'{index}: {probability:.10%}')
    print()


if __name__ == '__main__':

    # классы сверточных нейронных уровней
    Conv2D = krs.layers.Conv2D
    Dense = krs.layers.Dense
    Flatten =  krs.layers.Flatten
    MaxPooling2D = krs.layers.MaxPooling2D

    # получить набор MINST
    # (70'000 помеченных образцов 28x28 px, разбитых в пропорции test/train - 60/10 тыс.)
    mnist = krs.datasets.mnist
    # загрузить тренировочные и тестовые наборы
    (X_train, y_train), (X_test, y_test) = mnist.load_data()

    print('Размерности наборов:')
    print(f'X_train:{X_train.shape}\ny_train: {y_train.shape}\nX_test {X_test.shape}\ny_test{y_test.shape}\n')

    # Генерация случайной выборки на 24 элемента из одномерного массива (без замены)
    index = np.random.choice(np.arange(len(X_train)), 24, replace=False)

    # визуализация набора
    fig, ax = plt.subplots(nrows=4, ncols=6)
    for item in zip(ax.ravel(), X_train[index], y_train[index]):
        axes, image, target = item
        axes.imshow(image, cmap=plt.cm.gray_r)
        axes.set_xticks([])
        axes.set_yticks([])
        axes.set_title(target)
    plt.tight_layout()
    plt.show()

    # Сверотчные нейронные сети Keras работают с массивами NumPy формата (ширина, высота, каналы)

    # переформатирование изображений
    X_train = X_train.reshape((60_000, 28, 28, 1))
    X_test = X_test.reshape((10_000, 28, 28, 1))

    # нормализация данных для изображений (масшабирование на интервал 0.0 - 1.0)
    X_train = X_train.astype('float32') / 255
    X_test = X_test.astype('float32') / 255

    # преобразование меток из целых чисел в категорийные данные (прямое унитарное кодирование)
    to_cat = krs.utils.to_categorical
    y_train = to_cat(y_train)
    y_test = to_cat(y_test)

    # создание нейронной сети
    cnn = krs.models.Sequential()

    # добавление первого скрытого сверточного уровня (функция активации relu - Rectified Linear Unit)
    cnn.add(Conv2D(filters=64, kernel_size=(3, 3), activation='relu', input_shape=(28, 28, 1)))
    # добавление объединяющего уровня для сокращения степени размерности для предотвращения "чрезмерной подгонки"
    cnn.add(MaxPooling2D(pool_size=(2, 2)))

    # добавление второго сверточного уровня
    cnn.add(Conv2D(filters=128, kernel_size=(3, 3), activation='relu'))
    # добавление второго объединяющего уровня
    cnn.add(MaxPooling2D(pool_size=(2, 2)))

    # одномерное преобразование результатов (трехмерный вход -> одномерный выход)
    cnn.add(Flatten())

    # Добавление уровня Dense для сокращения количества признаков
    cnn.add(Dense(units=128, activation='relu'))

    # Добавление второго уровня Dense для получения итогового результата
    cnn.add(Dense(units=10, activation='softmax'))

    # вывод информации о созданных слоях
    print(cnn.summary())

    # компиляция модели
    cnn.compile(optimizer='adam', loss='categorical_crossentropy', metrics=['accuracy'])

    # обучение модели
    cnn.fit(X_train, y_train, epochs=5, batch_size=64, validation_split=0.1)

    # оценка модели
    loss, accuracy = cnn.evaluate(X_test, y_test)

    print()
    print('Потеря:', loss)
    print('Точность:', accuracy)

    # построение прогнозов на тестовом наборе
    predictions = cnn.predict(X_test)

    print()
    print('Первый образец соответствует цифре:', y_test[0])

    print()
    # вероятности, для 0-го образца, предсказанного методом predict
    print('Оценка вероятностей 0-го образца')
    # рассматривается только 0-й образец
    for ind, probability in enumerate(predictions[0]):
        print(f'{ind}: {probability:.10%}')

    # поиск неправильных прогнозов

    images = X_test.reshape((10_000, 28, 28))
    incorrect_predictions = []
    incorrect_indexes = []

    for i, (p, e) in enumerate(zip(predictions, y_test)):
        # предсказанные и ожидаемые
        predicted, expected = np.argmax(p), np.argmax(e)

        # если предсказание не равно ожиданию
        if predicted != expected:
            incorrect_predictions.append((i, images[i], predicted, expected))
            if len(incorrect_indexes) < 5:
                # сохранение индекса очередного ошибчного прогноза для последующего анализа
                incorrect_indexes.append(i)


    print()
    print('Всего ошибочных прогнозов:', len(incorrect_predictions))
    print()

    print('Вероятности ошибочных прогнозов для нескольких образцов:\n')
    for i in incorrect_indexes:
        display_probabilities(predictions[i], i)

    # визуализация ошибочных предсказаний
    fig, ax = plt.subplots(nrows=4, ncols=6)
    for axes, item in zip(ax.ravel(), incorrect_predictions):
        index, image, predicted, expected = item

        axes.imshow(image, cmap=plt.cm.gray_r)
        axes.set_xticks([])
        axes.set_yticks([])
        axes.set_title(f'index: {index}\np: {predicted}; e: {expected}')

    plt.tight_layout()
    plt.show()

    print()
    print('Программа успешно завершила работу.')




































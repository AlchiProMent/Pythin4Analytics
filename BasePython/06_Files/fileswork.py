import os

file_name = 'datas/van_rossum.txt'

# проверить наличие файла
if os.path.exists(file_name):
    print('Файл "{}" найден.'.format(file_name))
else:
    print('Файл "{}" отсутствует'.format(file_name))

# открыть файл только для чтения
f = os.open(file_name, os.O_RDONLY)
# получить размер файла
f_size = os.path.getsize(f)
print('Размер файла: {} байт'.format(f_size))

# прочитать файл в буферную переменную
van_rossum_txt = os.read(f,f_size)

# print(type(van_rossum_txt))
# print(van_rossum_txt.decode())

# закрыть файл
os.close(f)

# вывести на консоль строку-разделитель
print('-'*80)
new_name = 'datas/bad_name.txt'
try:
    f = os.open(new_name, os.O_RDONLY)
except FileNotFoundError:
    print('Файл с именем "{}" отсутствует на диске!'.format(new_name))
else:
    # получить размер файла
    f_size = os.path.getsize(f)
    # прочитать файл в буферную переменную
    van_rossum_txt = os.read(f, f_size)
    # декодировать и вывести на консоль
    print(van_rossum_txt.decode())
    # закрыть файл
    os.close(f)

print('-'*80)
try:
    f = os.open(file_name, os.O_RDONLY)
    van_rossum_txt = os.read(f, -100)
except FileNotFoundError:
    print('Файл с именем "{}" отсутствует на диске!'.format(new_name))
except OSError:
    print('Ошибка при чтении файла!')
finally:
    os.close(f)

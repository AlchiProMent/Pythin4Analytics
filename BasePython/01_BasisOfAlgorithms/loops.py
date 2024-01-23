print('Цикл 1')
for i in range(10):
    print(i)

print('Цикл 2')
for i in range(5,11):
    print(i)

print('Цикл 3')
for i in range(5,21,3):
    print(i)

s = 'Цикл 4'
print(s)
for ind in range( len(s) ):
    print( s [ind] )

s = 'Цикл 5'
print(s)
for ch in s:
    print(ch)

alphabet = 'АБВГДЕЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ'
reverse_alphabet = ''
print(alphabet)
for ch in alphabet:
    reverse_alphabet = ch + reverse_alphabet
print(reverse_alphabet)


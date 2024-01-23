'''
count = 10
while (count > 0):
    print(count)
    count -= 1

print()
for count in reversed(range(1,11)):
    print(count)

print()
count = 1
while (count <= 10):
    print(count)
    count += 1
'''

s = input('Введите строку:')
# длина строки
len_s = len (s)
ind = 0
while ( ind < len_s ) and ( s[ind] != 'Ы' ):
    ind += 1

if (ind == len_s):
    print('Буква Ы не найдена')
else:
    print('Буква Ы найдена в позиции N', ind)
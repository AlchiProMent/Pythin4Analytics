s = 'Python - это высокоуровневый язык программирования общего назначения.'
s_mirror = ''
for ch in s:
    s_mirror = ch + s_mirror
    if (ch == '*'):
        s_mirror = 'ERROR!'
        break

print(s_mirror)

print()
without_space = ''
space = ' '
for ch in s:
    if (ch == space):
        continue
    without_space = without_space + ch

print(without_space)


without_space = ''
space = ' '
count = 0
for ch in s:
    if (ch == space):
        pass
        count += 1
    without_space = without_space + ch

print(without_space)
print('Убрано пробелов:',count)


print()
s = ''
for ch in s:
    print(ch)
else:
    print('Пустая строка')


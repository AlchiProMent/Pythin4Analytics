def hypotenuse(len1, len2):
    # расчет длины гипотенузы по длинам катетов len1 и len2
    hypo = len1*len1 + len2*len2
    hypo = hypo ** 0.5
    return hypo

print(hypotenuse(10,20))

# hypo = 'Это другая переменная с именем hypo'
# print(type(hypo))

def attent(msg='Нет сообщения'):
    print('ВНИМАНИЕ!', msg)

attent('Здесь может быть ошибка.')
attent('Не путайте имена переменных.')
attent('Дальше будет еще интереснее.')

attent()
# передача функции в качестве параметра в другую функцию

# универсальная йункция, выполняющая разные действия
def uniop (d1, d2, op='+'):
    # сложение
    if op == '+':
        return d1 + d2
    # вычитание
    elif op == '-':
        return d1 - d2
    # умножение
    elif op == '*':
        return d1 * d2
    # деление с остатком
    elif op == '/':
        return d1 / d2
    # инверсия знака первого параметра
    else:
        return -1 * d1

print( 'сложение:', uniop( 20, 10 ) )
print( 'вычитание:', uniop( 20, 10, '-' ) )
print( 'умножение:', uniop( 20, 10, '*' ) )
print( 'деление:', uniop( 20, 10, '/' ) )
print( 'инверсия:', uniop( 20, 10, '~' ) )

# еще более универсальная функия
def uniop2(funcname, x1, x2):
    return funcname (x1, x2)

def plus(d1, d2):
    # сложение
    return d1 + d2

def minus(d1, d2):
    # разность
    return d1 - d2

def mult(d1, d2):
    # произведение
    return d1 * d2

def divis(d1,d2):
    # деление
    return d1 / d2

def squaresum(d1,d2):
    # квадрат суммы
    return d1*d1 + 2*d1*d2 + d2*d2

def squaredif(d1,d2):
    # квадрат разности
    return d1*d1 - 2*d1*d2 + d2*d2

def difsquare(d1,d2):
    # разность квадратов
    return (d1 - d2) * (d1 + d2)

def cubesum(d1, d2):
    # куб суммы
    return d1*d1*d1 + 3*d1*d1*d2 + 3*d1*d2*d2 + d2*d2*d2

print('\n----------------------')
print( 'Сложение:', uniop2( plus, 14, 16 ))
print( 'Вычитание:', uniop2( minus, 14, 16 ))
print( 'Умножение:', uniop2( mult, 14, 16 ))
print( 'Деление:', uniop2( divis, 14, 16 ))
print( 'Квадрат суммы:', uniop2( squaresum, 14, 16 ))
print( 'Квадрат разности:', uniop2( squaredif, 14, 16 ))
print( 'Разность квадратов:', uniop2( difsquare, 14, 16 ))

print( '\nКуб суммы:', uniop2( cubesum, 14, 16 ))



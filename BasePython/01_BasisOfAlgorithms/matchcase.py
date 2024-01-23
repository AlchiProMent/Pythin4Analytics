# выбор из множества альтернатив

def color_choice(color_num):
    match color_num:
        case 1:
            print('красный')
        case 2:
            print('оранжевый')
        case 3:
            print('желтый')
        case 4:
            print('зеленый')
        case 5:
            print('голубой')
        case 6:
            print('сидит')
        case 7:
            print('фиолетовый')
        case _:
            print('неверный номер')

# выдать цвета по коду
color_choice(2)
color_choice(5)
color_choice(7)
color_choice(9)

def light_color(color):
    match color:
        case 1 | 2 | 3:
            print('теплый цвет')
        case 4 | 5 | 6 | 7:
            print('холодный цвет')
        case _:
            print('неверный номер')

light_color(2)
light_color(5)
light_color(7)
light_color(9)

def c_color(color, ret=False):
    match color:
        case 1 | 2 | 3 if not ret:
            print('теплый цвет')
        case 1 | 2 | 3 if ret:
            return 'теплый цвет'
        case 4 | 5 | 6 | 7 if not ret:
            print('холодный цвет')
        case 4 | 5 | 6 | 7 if ret:
            return 'холодный цвет'
        case _:
            if not ret:
                print('неверный номер')
            else:
                return 'неверный номер'

print()
c_color(3)
c_color(6)
c_color(9)

print()
print( 'Желтый - это', c_color(3, True) )
print( 'Синий - это', c_color(6, True) )
print( c_color(9, True) )
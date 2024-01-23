# класс Машины
class Machine:
    __human = not True
    __name = ''
    def __init__(self, name='Машина'):
        self.__name = name
    def __str__(self):
        return '\nКласс: ' + type(self).__name__ + '\nМашина:' + ('Да','Нет')[self.__human] + '\nНазвание: ' + self.__name
    def is_human(self):
        return self.__human
    def is_machine(self):
        return not self.__human
    def name(self):
        return self.__name

# класс Электрические машины
class ElectricMachine(Machine):
    __voltage = 220
    __mobile = False
    def __init__(self, name='Электрический механизм', voltage=220, mobile=False):
        super().__init__(name)
        self.__voltage = voltage
        self.__mobile = mobile
    def __str__(self):
        return super().__str__() + '\nВольтаж: ' + str(self.__voltage) + '\n' + ('Стационарный','Мобильный')[self.__mobile]
    def voltage(self):
        return self.__voltage
    def mobile(self):
        return self.__mobile

# константы для типов устройств
E_LAMPS = 1         # устройства на лампах
E_SOLID_STATE = 2   # устройства на твердотельных элементах
E_MICRO = 3         # устройства на микросхемах

class Electronics(ElectricMachine):
    def __init__(self,name='Электроника',voltage=220,mobile=True,etype=E_MICRO):
        super().__init__(name,voltage,mobile)
        self.__e_type = etype
    def GetType(self):
        return self.__e_type
    def name(self):
        full_name = super().name()
        if (self.__e_type == E_LAMPS):
            full_name = full_name + ' (ламповый)'
        elif (self.__e_type == E_SOLID_STATE):
            full_name = full_name + ' (транзисторный)'
        else:
            full_name = full_name + ' (на микросхемах)'
        return full_name


machine = Machine()
catapult = Machine('Катапульта')
water_mill = Machine('Водяная мельница')

print(machine.name())
print(catapult.name())
print(water_mill.name())

print(machine)
print(catapult)
print(water_mill)
# print(water_mill.__str__())

vacuum_cleaner = ElectricMachine('Пылесос',220,True)
electric_motor = ElectricMachine('Электромотор',380)

print(vacuum_cleaner)
print(electric_motor)

# print( dir(vacuum_cleaner) )

vacuum_cleaner.brand = 'AlchiPro'
vacuum_cleaner.price = 10_000.00

# discount = 0.15
#print('На пылесосы ' + vacuum_cleaner.brand + ' при покупке от 10 штук действует скидка ' + str(round(discount*100))+
#      '%. 10 пылесосов этой марки обойдутся в ' + str (10*vacuum_cleaner.price*(1-discount)) + ' рублей')

# print(electric_motor.price)

class Discount: pass
discount = Discount()
discount.proc15 = 0.15
discount.proc10 = 0.1
discount.proc25 = 0.25

print('На пылесосы ' + vacuum_cleaner.brand + ' при покупке от 10 штук действует скидка ' + str(round(discount.proc15*100))+
      '%. 10 пылесосов этой марки обойдутся в ' + str (10*vacuum_cleaner.price*(1-discount.proc15)) + ' рублей')


tube_amplifier = Electronics('Ламповый усилитель', 127, True, E_LAMPS)
transistor_amplifier = Electronics('Транзисторный усилитель', 220, True, E_SOLID_STATE)

# ламповый усилитель
amplifier_lamp = Electronics('Fezz Audio Titania Big calm',220,True,E_LAMPS)
# транзисторный усилитель
amplifier_semi = Electronics('iFi Audio Pro iDSD 4.4',220,True,E_SOLID_STATE)

print()
print(tube_amplifier.name())
print(transistor_amplifier.name())
print(amplifier_lamp.name())
print(amplifier_semi.name())
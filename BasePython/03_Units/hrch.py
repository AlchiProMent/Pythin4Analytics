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

import hrch
from . import const

class Screen(hrch.Electronics):
    __screen_type = const.TV
    __width = 640
    __height = 480
    def __init__(self,name='Экран',screen_type=1,w=800,h=600):
        super().__init__(name,220,True,hrch.E_MICRO)
        # инициализировать дополнительные свойства
        self.__screen_type = screen_type
        self.__width = w
        self.__height = h
    def GetType(self):
        return self.__screen_type
    def __str__(self):
        name_screen = ''
        if (self.__screen_type==const.TV):
            name_screen = 'Телевизор'
        elif (self.__screen_type==const.SMART_TV):
            name_screen = 'Смарт-телевизор'
        elif (self.__screen_type==const.SMARTPHONE):
            name_screen = 'Смартфон'
        elif (self.__screen_type==const.I_PHONE):
            name_screen = 'Айфон'
        elif (self.__screen_type==const.PLANCHETEE):
            name_screen = 'Планшет'
        elif (self.__screen_type==const.DISPLAY):
            name_screen = 'Дисплей для компьютера'
        return '{0} "{1}" с размером экрана {2}x{2} пикселей'.\
            format(name_screen,
                   super(hrch.ElectricMachine,self).name(),
                   self.__width,
                   self.__height
                   )

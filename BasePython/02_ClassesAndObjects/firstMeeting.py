class Machine:
    # human = not True
    __human = not True
    def is_human(self):
        return self.__human
    def is_machine(self):
        return not self.__human

catapult = Machine()
water_mill = Machine()

# water_mill = catapult
if (catapult == water_mill):
    print('Катапульта равна водяной мельнице')
else:
    print('Катапульта - это не водяная мельница!')

# water_mill.human = True
# print(catapult.__human)
# print(water_mill.__human)

print(catapult.is_human(),catapult.is_machine())
print(water_mill.is_human(),water_mill.is_machine())

print( dir (catapult) )
print( dir (water_mill) )

# catapult._Machine__human = True
# print(catapult.is_human())

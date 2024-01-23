# from hrch import Machine, ElectricMachine as eMach, Electronics
from hrch import Machine, ElectricMachine, Electronics, E_MICRO

machine = Machine()
e_machine = ElectricMachine()
micro = Electronics()

calculator = Electronics('Калькулятор',220,True,E_MICRO)

print(machine)
print(e_machine)
print(micro)


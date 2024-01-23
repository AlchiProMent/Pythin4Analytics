import hrch

amplifier = hrch.Electronics('Стереоусилитель AMC XIA100se',220,True,hrch.E_SOLID_STATE)

print(amplifier.name())
print(amplifier)

# экземпляр класса Machine
machine = hrch.Machine()
print(machine)

# экземпляр класса ElectricMachine(
e_machine = hrch.ElectricMachine()
print(e_machine)
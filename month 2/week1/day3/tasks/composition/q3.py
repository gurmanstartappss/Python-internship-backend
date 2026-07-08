class CPU:
    def __init__(self):
        self.name = "Intel i7"


class Computer:
    def __init__(self):
        self.cpu = CPU()

    def show(self):
        print(self.cpu.name)


c1 = Computer()
c1.show()
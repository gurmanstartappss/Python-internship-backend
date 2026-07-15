class Engine:
    def __init__(self):
        self.power = "200 HP"


class Car:
    def __init__(self):
        self.engine = Engine()

    def show(self):
        print(self.engine.power)


c1 = Car()
c1.show()
class Driver:
    def __init__(self, name):
        self.name = name

    def drive(self, car):
        print(self.name, "drives", car.name)


class Car:
    def __init__(self, name):
        self.name = name


d1 = Driver("Gurman")
c1 = Car("BMW")

d1.drive(c1)
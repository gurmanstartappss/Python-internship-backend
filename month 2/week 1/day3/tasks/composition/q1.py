class Room:
    def __init__(self, name):
        self.name = name


class House:
    def __init__(self):
        self.room1 = Room("Bedroom")
        self.room2 = Room("Kitchen")

    def show(self):
        print(self.room1.name)
        print(self.room2.name)


h1 = House()
h1.show()
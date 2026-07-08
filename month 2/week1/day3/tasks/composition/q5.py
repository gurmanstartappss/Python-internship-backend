class Keyboard:
    def __init__(self):
        self.type = "Backlit Keyboard"


class Laptop:
    def __init__(self):
        self.keyboard = Keyboard()

    def show(self):
        print(self.keyboard.type)


l1 = Laptop()
l1.show()
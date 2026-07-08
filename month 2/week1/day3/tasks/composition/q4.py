class Battery:
    def __init__(self):
        self.capacity = "5000 mAh"


class Mobile:
    def __init__(self):
        self.battery = Battery()

    def show(self):
        print(self.battery.capacity)


m1 = Mobile()
m1.show()
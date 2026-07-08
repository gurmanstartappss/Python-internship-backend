class MyList:
    def __init__(self, items):
        self.items = items

    def __getitem__(self, index):
        return self.items[index]
obj = MyList([10, 20, 30])
print(obj[0])
class Father():
    def paps(self):
        print("i love papa ")
class Mother():
    def mama(self):
        print("i love mama ")
class Child(Father,Mother):
    def me(self):
        print("i love myself ")

x=Child()
x.me()
x.paps()
x.mama()

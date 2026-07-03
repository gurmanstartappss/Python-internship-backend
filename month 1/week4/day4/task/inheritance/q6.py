class Employee:
    def payment(self):
        print("Employee attendance is logged in so proceed with payment ")

class Developer(Employee):
    def devwork(self):
        print("devs are working  ")

class Tester(Employee):
    def testwork(self):
        print("tester are testing websites  ")
    
class Hr(Employee):
    def hrwork(self):
        print("hr are hiring  ")

x=Developer()
y=Tester()
z=Hr()

x.devwork()
x.payment()
y.testwork()
y.payment()
z.hrwork()
z.payment()

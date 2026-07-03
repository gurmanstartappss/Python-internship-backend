class Animal():
    def __init__(self,name):
        self.name=name
        print("Animal called ")
        
        
class Dog(Animal):
    def __init__(self,name,breed):
        super().__init__(name)
        self.breed=breed
        print("dog called")
                
    def display(self):
        print("name:",self.name )
        print("breed:",self.breed )
        
        
x=Dog("phoebe","pitbull")
x.display()

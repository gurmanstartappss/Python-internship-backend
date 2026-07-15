class Player():
    def __init__(self,name):
        self.name=name
        
class Team():
    def __init__(self,players):
        self.players=players
        
    def show(self):
        for players in self.players:
            print(players.name)
            
x=Player("gurman")
x1=Player("hahaha")
x2=Player("avantika")
t1=Team([x,x1,x2])
del t1
print(x.name)
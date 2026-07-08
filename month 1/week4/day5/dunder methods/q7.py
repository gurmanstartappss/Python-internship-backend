class Team:
    def __init__(self, members):
        self.members = members

    def __contains__(self, name):
        return name in self.members


team = Team(["Aman", "Rahul", "Priya"])

print("Rahul" in team)   # True
print("Rohan" in team)   # False
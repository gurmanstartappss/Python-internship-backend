from collections import defaultdict
Input=[("Rahul","IT"),("Aman","HR"),("Rohit","IT")]
z=defaultdict(list)

for name,department in Input:
    z[department].append(name)

print(dict(z))
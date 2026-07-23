from collections import defaultdict
from collections import Counter
input=[
("Rahul","IT"),
("Aman","HR"),
("Rohit","IT")
]

group=defaultdict(list)
count=0
for name,dept in input:
    group[dept].append(name)
    
    count+=1
print(group)
print(count)
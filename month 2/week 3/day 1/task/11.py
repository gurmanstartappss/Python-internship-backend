from collections import defaultdict
d=defaultdict(list)
listt=[("gurman",101,465678),("avantika",102,10),("hasha",102,50001)]
for name,roll,paisa in listt:
    if 20000> paisa>0:
        d["0-20000"].append((name,roll,paisa))
    elif paisa>20000:
        d["20000+"].append((name,roll,paisa))
    elif paisa>50000:
        d["50000+"].append((name,roll,paisa))
print(d)

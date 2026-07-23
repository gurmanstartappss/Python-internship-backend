from collections import OrderedDict
od=OrderedDict()
od["a"]=1
od["b"]=2
od["c"]=3
od["d"]=6
print(od)
od.move_to_end("a")
print(od)
od.popitem("a")
print(od)
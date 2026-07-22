"""collection module:it provides specialised container data types that are faster and more convenient than normal python data structure for many use cases
1) defaultdict:Default dict is a special dictionary that automatically creates a default value for missing keys so you don't get an error.

defaultdict(default_factory)
"""

from collections import defaultdict

dict1= {
    "a":"apple",
    "b":"ball"
}
# print(dict1["c"]) this will bring error 

students = defaultdict(int) #0 missing key, automatically starts with 0

for name in ["A", "B", "C", "A"]:
    students[name] += 1

print(students)

from collections import defaultdict

department = defaultdict(list)  # Missing key automatically starts with an empty list

department["IT"].append("gurman")
department["sales"].append("pranjali")
department["IT"].append("arya")
department["sales"].append("avantika")

print(department)
"""faster then normal dict because  default dict check values one by one as list default value is [] and int default value is 0"""

"""
2) counter-count the number of times (frequency) of the elements automatically 
"""

from collections import Counter

nums = [1, 2, 3, 4, 6, 3, 1, 4, 2, 1, 4, 5, 6, 3, 7, 9, 4]
c = Counter(nums)
for k, v in c.items():
    if v > 1:
        print(k)

# str1 = "banana"
# print(Counter(str1))

# from collections import defaultdict
# words=["apple","ant","ball","cat"]
# d=defaultdict(list)
# for word in words:
#     d[word[0].append(word)]
    
"""3) dequeue:unlike queue which allows onl/y one side append and deletion,dequeue allows fast insertion and deletion from both ends and is faster then a list
queue=FIFO
stack=Last in first out
"""

from collections import deque
que= deque()
que.append(10)
que.appendleft(20)
que.appendleft(40)
que.popleft()
que.pop()
print(que)


"""
4)namedtuple: a nameduple is like a tuple but it has values that can be accessed using field names
student[4]=value
student[2]=value
"""
from collections import namedtuple
Student = namedtuple("Student", ["name", "age"])
s = Student("gurman", 20)
s1 = Student("pranjali", 20)
print(s.name)
print(s.age)
print(s1.name)
print(s1.age)

"""5) ChainMap=combines multiple dictionaries into a single dict"""
from collections import ChainMap
d1={"A":10}
d2={"B":20}
dict1=ChainMap(d1,d2)
print(dict1["B"])

"""6)OrderedDict:orderedDict explicitly mantains insertion order now but before 3.7 dict was unoredered and no fixed insertion order so it was used but now not that much used but used for custom ordered like 
"""
from collections import OrderedDict

dict1 = OrderedDict()

dict1["A"] = 1
dict1["B"] = 2
dict1["C"] = 3

dict1.move_to_end("A")#order specific 

print(dict1)
"""
data structure       use                                     time complexity
dict                 fast key look up                        O(1)
defaultdict          mising keys with default values         O(1)avg per update 
deque                insert/delete at both ends              O(1)
list                 append at end                           O(1)
list.insert(0,x)     insert at beginning                     O(n)

"""
from collections import Counter
c=[1,2,4,5,33,2,2,43,3,5,6,4,3,2,12,3,45,65,6,4,3,2,2,4,5,6,67]
h=Counter(c)
print(h.most_common(5))
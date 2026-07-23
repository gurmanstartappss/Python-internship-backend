from collections import Counter
text="apple"
c=Counter(text)
for ch in text:
    if c[ch]==1:
        print(ch)
        break
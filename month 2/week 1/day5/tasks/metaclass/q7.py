"""
7. How can a metaclass add methods to a class?
A metaclass can add methods to a class by inserting a function into the attrs (or namespace) dictionary before the class is created.
A metaclass can validate a class definition by examining the attrs dictionary inside its __new__() method before the class is created. If the class doesn't meet certain rules, the metaclass can raise an exception such as TypeError or ValueError.
"""
"""

5. What are the parameters of the __new__() method in a metaclass?
The para meters of new dunder method are :

`mcls`       The metaclass itself (similar to `cls` in a normal class method).                   
`name`       The name of the class being created (a string).                                     
`bases`      A tuple containing the base (parent) classes.                                       
`namespace`  A dictionary containing the class attributes and methods defined in the class body. 

"""
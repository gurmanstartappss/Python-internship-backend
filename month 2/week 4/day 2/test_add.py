import unittest
from demo import add,sub

class TestMath(unittest.TestCase):
    
    def test_add(self):
        self.assertEqual(add(2,4),6)
        self.assertEqual(add(3,7),10)
        self.assertEqual(add(6,5),11)
    
    def test_sub(self):
        self.assertEqual(sub(7,3),4)
        self.assertEqual(sub(3,1),2)
        self.assertEqual(sub(7,3),4)
if __name__=="__main__":
    unittest.main()
    
    
    
# Parameterized tests: test multiple inputs

import pytest

@pytest.mark.parametrize(
    "a,b,result",
    [
        (2, 4, 6),
        (3, 4, 7),
        (4, 4, 8),
        (5, 4, 9),
        (6, 4, 10),
    ]
)
def test_add(a, b, result):
    assert add(a, b) == result
    
#run using pytest in terminal
#if run pytest -x := stops after 1st failure
#pytest --lf := run failed tests again
#fixtures:=fixtures provide reusable setup code before test executes
 


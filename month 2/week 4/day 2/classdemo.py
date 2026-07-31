"""testing
1)unit test:=it is the process of testing the smallest unit of code (usually a function or method)independently to ensure it works correctly
2)Integration testing:=test multiple modules/files together
3)system testing:=whole application
4)End to End testing:= from start to end test

# Common Assertions:

# 1. AssertEqual: compare two values are equal
self.assertEqual(a, b)

# 2. AssertNotEqual
self.assertNotEqual(a, b)

# 3. AssertTrue
self.assertTrue(condition)

# 4. AssertFalse
self.assertFalse(condition)

# 5. AssertIs
self.assertIs(obj1, obj2)

# 6. AssertIsNot
self.assertIsNot(obj1, obj2)

# 7. AssertIn
self.assertIn(item, container)

# 8. AssertNotIn
self.assertNotIn(item, container)

# 9. AssertRaises: check whether a specific exception is raised
with self.assertRaises(ExceptionType):
    # code that should raise the exception
    pass

# 10. Comparison assertions
self.assertGreater(a, b)
self.assertLess(a, b)
self.assertGreaterEqual(a, b)
self.assertLessEqual(a, b)

# 11. Regular expression assertion
self.assertRegex(text, pattern)
pytest=library install, its a powerful 3rd party testing framework that allows simple readable and feature-rich testing with minimal code

#parameterised tests: test multiple inputs 

def test_add(a,b,result):
    assert add(a,b)==result
"""
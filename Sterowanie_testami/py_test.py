import unittest

class MyTestCase(unittest.TestCase):
    def test_one(self):
        pass

    def notest(self):
        pass
class MySeconTestCase(unittest.TestCase):
    def test_two(self):
        pass

    if __name__ == "main":
        unittest.main()

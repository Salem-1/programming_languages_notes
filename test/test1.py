import unittest # importing the unittest library which will automate the test for us

from prime import is_prime

class Tests(unittest.TestCase):
    def test_1(self):
        """check that 1 is not a prime number""" # the """ descripe what the function do in the unit test shell besides it works as comment
        self.assertFalse(is_prime(1)) # make sure that the output is False


class Tests(unittest.TestCase):
    def test_1(self):
        """check that 1 is not a prime number"""
        self.assertTrue(is_prime(13))

class Tests(unittest.TestCase):
    def test_1(self):
        """check that 1 is not a prime number"""
        self.assertFalse(is_prime(7))

class Tests(unittest.TestCase):
    def test_1(self):
        """check that 1 is not a prime number"""
        self.assertTrue(is_prime(5))

class Tests(unittest.TestCase):
    def test_1(self):
        """check that 1 is not a prime number"""
        self.assertFalse(is_prime(9))


if __name__=='__main__':
    unittest.main()

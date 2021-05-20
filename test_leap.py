import unittest
import pytest
import leap_year

#unittest
class test_leap(unittest.TestCase):
    def test_is(self):
        self.assertEqual(leap_year.leap_year(4000), "yes")
    def test_isNot(self):
        self.assertEqual(leap_year.leap_year(3011), "no")
    def test_error(self):
        self.assertEqual(leap_year.leap_year("hello"), "error: input must be an integer")

if __name__ == "__main__":
    unittest.main()

#pytest
def test_is():
    assert leap_year.leap_year(2012) == "yes"
def test_isNot():
    assert leap_year.leap_year(5051) == "no"
def test_Typeerror():
    assert leap_year.leap_year("hello") == "error: input must be an integer"
def test_fail():
    assert leap_year.leap_year(5050) == "yes"
        
        

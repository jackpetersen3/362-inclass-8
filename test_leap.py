import unittest
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
        
        

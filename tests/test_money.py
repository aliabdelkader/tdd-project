import unittest

from LearnTdd.money import Dollar

class TestMoney(unittest.TestCase):
    def testMultipication(self):
        fiver = Dollar(5)
        tenner = fiver.times(2)
        self.assertEqual(10, tenner.amount)
    

if __name__ == "__main__":
    unittest.main()
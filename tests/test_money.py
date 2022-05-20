from locale import currency
import unittest

from LearnTdd.money import Money

class TestMoney(unittest.TestCase):
    def testMultipicationInDollars(self):
        fiver = Money(amount=5, currency="USD")
        tenner = Money(amount=10, currency="USD")
        self.assertEqual(fiver.times(2), tenner)
    
    def testMultiplicationInEuros(self):
        tenEuros = Money(amount=10, currency="EUR")
        twentyEuros = Money(amount=20, currency="EUR")
        self.assertEqual(tenEuros.times(2), twentyEuros)
    
    def testDivision(self):
        originalMoney = Money(amount=4002, currency="KRW")
        expectedMoneyAfterDivison = Money(amount=1000.5, currency="KRW")
        self.assertEqual(originalMoney.divide(4), expectedMoneyAfterDivison)

if __name__ == "__main__":
    unittest.main()
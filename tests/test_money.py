from locale import currency
import unittest

from LearnTdd.money import Money, Portfolio

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
    
    def testAddition(self):
        fiveDollars = Money(5, "USD")
        tenDollars = Money(10, "USD")
        fifteenDollars = Money(15, "USD")
        portfolio = Portfolio()
        portfolio.add(fiveDollars, tenDollars)
        self.assertEqual(fifteenDollars, portfolio.evaluate("USD"))

if __name__ == "__main__":
    unittest.main()
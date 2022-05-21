from cmath import exp
from locale import currency
import unittest

from LearnTdd.money import Money, Portfolio, Bank

class TestMoney(unittest.TestCase):
    def setUp(self) -> None:
        self.bank = Bank()
        self.bank.addExchangeRate("USD", "USD", 1)
        self.bank.addExchangeRate("EUR", "USD", 1.2)
        self.bank.addExchangeRate("USD", "KRW", 1100)
        
        return super().setUp()
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
        self.assertEqual(fifteenDollars, portfolio.evaluate(self.bank, "USD"))
    
    def testAdditionDollarsAndEuro(self):
        fiveDollars = Money(5, "USD")
        tenEuros = Money(10, "EUR")
        p = Portfolio()
        p.add(fiveDollars, tenEuros)
        expectedValue  = Money(17, "USD")
        actualValue = p.evaluate(self.bank, "USD")
        self.assertEqual(expectedValue, actualValue, f"expected: {expectedValue} != {actualValue}")
    
    def testAdditionOfDollarsAndWon(self):
        oneDollar = Money(1, "USD")
        elevenHundredWon = Money(1100, "KRW")
        p = Portfolio()
        p.add(oneDollar, elevenHundredWon)
        expectedValue = Money(2200, "KRW")
        actualValue = p.evaluate(self.bank, "KRW")
        self.assertEqual(expectedValue, actualValue, f"{expectedValue} != {actualValue}")

    def testConversion(self):
        bank = Bank()
        bank.addExchangeRate("EUR", "USD", 1.2)
        tenEuros = Money(10, "EUR")
        self.assertEqual(Money(12, "USD"), bank.convert(tenEuros, "USD"))
    
    def testConversionWithMissingExchange(self):
        tenEuros = Money(10, "EUR")
        with self.assertRaisesRegex(Exception, "EUR->Kalganid"):
            self.bank.convert(tenEuros, "Kalganid")

    # def testAdditionWithMultipleMissingExchangeRates(self):
    #     oneDollar = Money(1, "USD")
    #     oneEuro = Money(1, "EUR")
    #     oneWon = Money(1, "KRW")
    #     portfolio = Portfolio()
    #     portfolio.add(oneDollar, oneEuro, oneWon)
    #     with self.assertRaisesRegex(
    #         Exception,
    #         "Missing exchange rate \(s\): \[USD->Kalganid,EUR->Kalganid,KRW->Kalganid]"):
    #         portfolio.evaluate("kalganid")
if __name__ == "__main__":
    unittest.main()
from typing import List
import functools
import operator

class Money():
    def __init__(self, amount: float, currency: str) -> None:
        self.amount = amount
        self.currency = currency
    
    def times(self, multiplier):
        return Money(amount= self.amount * multiplier, currency=self.currency)
    
    def divide(self, dividor):
        return Money(amount= self.amount / dividor, currency= self.currency)
    
    def __eq__(self, __o: object) -> bool:
        return (self.amount == __o.amount) and (self.currency == __o.currency)

    def __str__(self) -> str:
        return f"{self.currency} {self.amount: 0.2f}"

class Portfolio:
    def __init__(self) -> None:
        self.portfolio = [] # type: Money

    def add(self, *p):
        self.portfolio.extend(p)

    
    def __convert(self, aMoney, aCurrency):
        exchangeRates = {'EUR->USD': 1.2, 'USD->KRW': 1100}
        if aMoney.currency == aCurrency:
            return aMoney.amount
        else:
            key = f"{aMoney.currency}->{aCurrency}"
            exchange = exchangeRates[key]
            return aMoney.amount * exchange
            
    
    def evaluate(self, currency: str):
        total = 0.0
        failure = []
        for m in self.portfolio:
            try:
                total += self.__convert(m, currency)
            except KeyError as ke:
                failure.append(ke)

        if len(failure) == 0:
            return Money(amount=total, currency=currency)
        else:
            failureMessage = ",".join(str(f.args[0]) for f in failure)
            raise Exception("Missing exchange rate \(\s\):\[" + failureMessage + "]")

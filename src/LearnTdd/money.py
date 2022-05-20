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
        self._euro_to_usd = 1.2

    def add(self, *p):
        self.portfolio.extend(p)

    
    def __convert(self, aMoney, aCurrency):
        if aMoney.currency == aCurrency:
            return aMoney.amount
        
        else:
            return aMoney.amount * self._euro_to_usd 
    
    def evaluate(self, currency: str):
        # total = sum([p.amount for p in self.portfolio])
        total = functools.reduce(
            operator.add, map(lambda p: self.__convert(p, currency), self.portfolio), 0
        )
        return Money(amount=total, currency=currency)

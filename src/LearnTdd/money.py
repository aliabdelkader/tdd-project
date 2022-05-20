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

class Portfolio:
    def __init__(self) -> None:
        self.portfolio = [] # type: Money

    def add(self, *p):
        self.portfolio.extend(p)
    
    def evaluate(self, currency: str):
        # total = sum([p.amount for p in self.portfolio])
        total = functools.reduce(
            operator.add, map(lambda p: p.amount, self.portfolio), 0
        )
        return Money(amount=total, currency=currency)

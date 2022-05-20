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
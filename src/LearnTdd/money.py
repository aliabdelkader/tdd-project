class Dollar():
    def __init__(self, amount) -> None:
        self.amount = amount

    def times(self, multiplier):
        return Dollar(amount = self.amount * multiplier)

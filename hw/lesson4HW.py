rates = {
   "KGS": 1,
   "USD": 89,
   "EUR": 96,
   "RUB": 1.2
}

class Money:
    def __init__(self, amount, currency):
        self.amount = amount
        self.currency = currency

    def convert_to_kgs(self):
        return self.amount * rates[self.currency]

    def __add__(self, other):
        self_in_kgs = self.convert_to_kgs()
        other_in_kgs = other.convert_to_kgs()
        total_kgs = self_in_kgs + other_in_kgs
        return Money(total_kgs, "KGS")

    def __sub__(self, other):
        self_in_kgs = self.convert_to_kgs()
        other_in_kgs = other.convert_to_kgs()
        total_kgs = self_in_kgs - other_in_kgs
        return Money(total_kgs, "KGS")

    def __mul__(self, other):
        new_amount = self.amount * other
        return Money(new_amount, self.currency)

    def __truediv__(self, other):
        new_amount = self.amount / other
        return Money(new_amount, self.currency)

    def __str__(self):
        return f"{self.amount} {self.currency}"


money1 = Money(100, "USD")
money2 = Money(5000, "KGS")

result = money1 + money2
print(result)
import random


class Product():
    """Things sold by Acme"""
    def __init__(self, name, price=10, weight=20, flammability=0.5):
        self.name = name
        self.price = price
        self.weight = weight
        self.flammability = flammability
        self.identifier = random.randint(1000000, 9999999)

    def stealability(self):
        """Rating of the ratio of price to weight"""
        ratio = self.price / self.weight
        if ratio < .5:
            return "Not so stealable..."
        if ratio >= .5 and ratio < 1:
            return "Kinda stealable."
        return "Very stealable!"

    def explode(self):
        """Rating of the product of flammability and weight"""
        result = self.flammability * self.weight
        if result < 10:
            return "...fizzle."
        if result >= 10 and result < 50:
            return "...boom!"
        return "...BABOOM!!"


class BoxingGlove(Product):
    """A specific Product for punching"""
    def __init__(self, name, price=10, weight=10, flammability=0.5):
        self.name = name
        self.price = price
        self.weight = weight
        self.flammability = flammability
        self.identifier = random.randint(1000000, 9999999)

    def explode(self):
        return "...it's a glove."

    def punch(self):
        """Rating of how bad a punch from this glove is"""
        if self.weight < 5:
            return "That tickles."
        if self.weight >= 5 and self.weight < 15:
            return "Hey that hurt!"
        return "OUCH!"

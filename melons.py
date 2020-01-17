from random import randint
from datetime import datetime

"""Classes for melon orders."""
class AbstractMelonOrder:
    """An abstract base class that other Melon Orders inherit from."""

    shipped = False

    def __init__(self, species, qty):
        self.species = species
        self.qty = qty

    def get_base_price(self):
        """Return random base price from 5 to 9."""

        day = datetime.now()

        base_price = randint(5, 9)

        if day.weekday() != 5 and day.weekday() != 6 and day.hour in range(8, 11):
            base_price += 4

        return base_price

    def get_total(self):
        """Calculate price, including tax."""
        base_price = self.get_base_price()
        print(base_price)

        if self.species == 'Christmas melon':
            base_price = base_price * 1.5

        total = (1 + self.tax) * self.qty * base_price

        return total

    def mark_shipped(self):
        """Record the fact than an order has been shipped."""

        self.shipped = True



class DomesticMelonOrder(AbstractMelonOrder):
    """A melon order within the USA."""

    order_type = "domestic"
    tax = 0.08

   

class InternationalMelonOrder(AbstractMelonOrder):
    """An international (non-US) melon order."""

    order_type = "international"
    tax = 0.17

    def __init__(self, species, qty, country_code):
        super().__init__(species, qty)
        self.country_code = country_code
        

    def get_country_code(self):
        """Return the country code."""

        return self.country_code

    def get_total(self):
        total = super().get_total()
        if self.qty < 10:
            total += 3
       
        return total


class GovernmentMelonOrder(AbstractMelonOrder):
    """A government melon order that must pass security inspection."""

    order_type = 'government'
    passed_inspection = False
    tax = 0

    def mark_inspection(self, passed):

        self.passed_inspection = passed
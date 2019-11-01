import unittest
from acme import Product
from acme_report import generate_products, ADJECTIVES, NOUNS


class AcmeProductTests(unittest.TestCase):
    """Making sure Acme products are the tops!"""
    def test_default_product_price(self):
        """Test default product price being 10."""
        prod = Product('Test Product')
        self.assertEqual(prod.price, 10)

    def test_default_product_weight(self):
        """Test default weight being 20"""
        prod = Product('Test Product')
        self.assertEqual(prod.weight, 20)

    def test_explosion(self):
        """Test all possible outcomes of explode()"""
        splody = Product("TNT", weight=10, flammability=5)
        self.assertEqual(splody.explode(), "...BABOOM!!")
        splutty = Product("water", weight=10, flammability=.1)
        self.assertEqual(splutty.explode(), "...fizzle.")
        boom = Product("gun", weight=2, flammability=10)
        self.assertEqual(boom.explode(), "...boom!")

    def test_theft(self):
        """Test all possible outcomes of stealability()"""
        stealy = Product("batteries", price=1, weight=1)
        self.assertEqual(stealy.stealability(), "Very stealable!")
        no_stealy = Product("big rock", price=1, weight=100)
        self.assertEqual(no_stealy.stealability(), "Not so stealable...")
        maybe_stealy = Product("The Orb", price=4, weight=5)
        self.assertEqual(maybe_stealy.stealability(), "Kinda stealable.")


class AcmeReportTests(unittest.TestCase):
    def test_default_num_products(self):
        """Test default number of products produced by generate_products"""
        self.assertEqual(len(generate_products()), 30)

    def test_legal_names(self):
        """Test all generated names are legal"""
        for prod in generate_products():
            split = prod.name.split()
            self.assertIn(split[0], ADJECTIVES)
            self.assertIn(split[1], NOUNS)

    # it looks like the best option for testing inventory_report
    # involves redirect_stdout -- would like to try later!


if __name__ == '__main__':
    unittest.main()

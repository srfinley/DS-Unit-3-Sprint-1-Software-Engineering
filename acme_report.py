from random import randint, uniform, sample
from acme import Product

ADJECTIVES = ['Awesome', 'Shiny', 'Impressive', 'Portable', 'Improved']
NOUNS = ['Anvil', 'Catapult', 'Disguise', 'Mousetrap', '???']


def generate_products(num=30):
    """makes a list of random Products"""
    prods = []
    for _ in range(0, num):
        name = sample(ADJECTIVES, 1)[0] + ' ' + sample(NOUNS, 1)[0]
        prods.append(Product(name,
                             randint(5, 100),
                             randint(5, 100),
                             uniform(0.0, 2.5)))
    return prods


def inventory_report(li):
    """Prints summary of a list of Products"""
    names = []
    prices = []
    weights = []
    flams = []
    for prod in li:
        names.append(prod.name)
        prices.append(prod.price)
        weights.append(prod.weight)
        flams.append(prod.flammability)
    avg_price = sum(prices) / len(prices)
    avg_weight = sum(weights) / len(weights)
    avg_flam = sum(flams) / len(flams)
    unique_names = []
    for n in names:
        if n not in unique_names:
            unique_names.append(n)

    print('ACME CORPORATION OFFICIAL INVENTORY REPORT')
    print(f'Unique product names: {len(unique_names)}')
    print(f'Average price: {avg_price}')
    print(f'Average weight: {avg_weight}')
    print(f'Average flammability: {avg_flam}')

if __name__ == '__main__':
    inventory_report(generate_products())

# Building three functions: sort, reverse sort, and print list

pizza_toppings = [
    'Hawaiian',
    'Champagne Ham & CheeseBeef & Onion',
    'Pepperoni',
    'Simply Cheese',
    'Bacon & Mushroom',
    'Italiano',
    'The Deluxe',
    'Ham, Egg & Hollandaise',
    'Americano',
    'Mr Wedge',
    'BBQ Meatlovers'
]

print(pizza_toppings)

def sort_list():
    print(sorted(pizza_toppings))
sort_list()

def sort_reverse_list():
    print(reversed(sorted(pizza_toppings)))
sort_reverse_list()
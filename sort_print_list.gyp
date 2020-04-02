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
#
#print(pizza_toppings)
#
#def sort_list():
#    return sorted(pizza_toppings)
#print(sort_list())
#
def sort_reverse_list():
    return [ele for ele in reversed(sorted(pizza_toppings))]
print(sort_reverse_list())
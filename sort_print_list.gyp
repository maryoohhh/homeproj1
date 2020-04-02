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

def sort_list(lst):
   lst = [(i.casefold()) for i in lst]
   return sorted(lst)
print(sort_list(pizza_toppings))
#
#def sort_reverse_list(lst):
#    return [ele for ele in reversed(sorted(lst))]
#print(sort_reverse_list(pizza_toppings))
#
#def print_list(lst):
#    for i in sorted(lst):
#        print (i)
#print_list(pizza_toppings)
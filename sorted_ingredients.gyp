# Sorting items in a list

chicken_ingredients = ['chicken wings', 'salt', 'pepper', 'potato starch', 'oil', 'soy sauce', 'mirin', 'sugar', 'sake', 'garlic']

print("Ingredients in ascending order:")
for i in sorted(chicken_ingredients):
    print(i)

print("\nIngredients in descending order:")
for i in reversed(sorted(chicken_ingredients)):
    print(i)

# Create a list and print items in list

chicken_ingredients = ['chicken wings', 'salt', 'pepper', 'potato starch', 'oil', 'soy sauce', 'mirin', 'sugar', 'sake', 'garlic']

print ("All ingredients:\n[", end = "") #end= - to omit creating new line
for i in range(len(chicken_ingredients)-1): #fencepost algorithm
    print("'{}'".format(chicken_ingredients[i]), end = ", ")
print("'" + chicken_ingredients[9] + "']")

fave = chicken_ingredients[0]
print ("Favorite ingredients:")
print (fave)
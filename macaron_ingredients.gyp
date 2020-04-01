# Creating a list of ingredients to bake french macarons

macaron_ingredients = "almond flour", "confectioners sugar", "salt", "egg whites", "sugar", "vanilla extract", "food coloring"
filling_ingredients = "butter", "confectioners sugar", "vanilla extract", "heavy cream"

file = open('macaron_ingredients', 'w') # w indicates open file for writing only, if file exists then overwrite, otherwise create
for item in macaron_ingredients:
  file.write(item + '\n')
file.close()

file = open('filling_ingredients', 'w')
for item in filling_ingredients:
  file.write(item + '\n')
file.close()
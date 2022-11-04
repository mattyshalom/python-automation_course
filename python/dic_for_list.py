#In Python, a dictionary can only hold a single value for a given key. To workaround this, our single value can be a lis#t containing multiple values. Here we have a dictionary called "wardrobe" with items of clothing and their colors. the #example below print a line for each item with their color, for example: "red shirt", "blue shirt", and so on.

wardrobe = {"shirt":["red","blue","white"], "jeans":["blue","black"]}
for cloth in wardrobe:
	for color in wardrobe[cloth]:
		print("{} {}".format(color, cloth))

#  iterate through the keys and values of the cool_beasts dictionary.

cool_beasts = {"octopuses":"tentacles", "dolphins":"fins", "rhinos":"horns"}
for animals, feature in cool_beasts.items():
    print("{} have {}".format(animals, feature))

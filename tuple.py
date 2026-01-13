# countries = ("Spain", "Italy", "India", "England", "Germany")
# #tuples are immutable, so we convert to list to modify
# temp = list(countries)
# temp.append("Russia")       #add item 
# temp.pop(3) tuple(temp)
# print(countries)


countries = ("Pakistan", "Afghanistan", "Bangladesh", "ShriLanka")
countries2 = ("Vietnam", "India", "China")
southEastAsia = countries + countries2
print(southEastAsia)

countries3 = list(countries)

print(countries3)
southEastAsia = countries3 + list(countries2)
print(southEastAsia)
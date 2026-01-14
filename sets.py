set = set()

print(type(set))

s1 = {1, 2, 3, 4}
s2 = {4, 5, 6 , 7}

s3 = s1.union(s2)
s4 = s1.intersection(s2)

print (f"Union = {s3} \n Intersection = {s4} ")
set = set()

print(type(set))

s1 = {1, 2, 3, 4}
s2 = {4, 5, 6 , 7}

print(f"S1 = {s1} \nS2 = {s2} ")


s3 = (s1.union(s2))
s4 = (s1.intersection(s2))
s5 = (s1.symmetric_difference(s2))

print(f"S3 = {s3}\nS4 = {s4} \nS5 = {s5}")
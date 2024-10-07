# Set
# --------------------------------------------
# Set is an unordered collection of unique elements

# to define an empty set

s = set()

# to define a set with values

s = {1, 2, 3, 3, 4, 5, 6}
print(s)
# add a new element to the set
s.add(9)
print(s)

# to search an element exists in set or not

print(3 in s)

# set union
s1 = {4, 6, 9, 0, 10}
print(s)
print(s1)
print("union", s1.union(s))

# set intersection
print(s)
print(s1)
print("intersection", s1.intersection(s))

# set difference
print(s)
print(s1)
print("difference", s1.difference(s))

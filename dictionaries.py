# dictionary
# ---------------------------------------------------
# dictioary is essentially like a key value pair

x = {"key": "value"}
print(x["key"])

# to add a new key value pair to the dictionary
x[2] = 5
x[3] = (3, 4, 5)
print(x)

# to search for a key in the dictionary
print(3 in x)

# to get list of values
print(list(x.values()))

# to get list of keys
print(list(x.keys()))

# to remove a key from the dictionary
del x["key"]
print(x)

# iterating over the dictionary

for key, value in x.items():
    print(key, value)

for key in x.keys():
    print(key, x[key])

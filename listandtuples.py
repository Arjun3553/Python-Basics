# collections are unordered or ordered group of elements
# list and tuple
# list
# -------------------------------------------------------------------
x = []  # empty list
y = ["hi", 7, True]
print(x, y)
print(x)
x.append(False)  # to add the element to the end of the list
print(x)
y.extend(x)  # to extend the list by appending the elements of the list to another list
print(y)
print(x.pop())  # to remove the element from the end of the list
print(y.pop(1))  # to remove the element from the specified index

# tuples
# tuples is an immutable list
# ----------------------------------------------------------------
z = (0, 2, 4, 6, 8, 10)

# Slice Operator is used to slice a portion of a string

x = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
y = ["hi", "hello", "goodbye", "sure"]
z = "world"

# sliced = [start:stop:step]
sliced = x[:4]
print(sliced)

# to reverse a list
reversed = x[::-1]
print(reversed)

# to reverse a string
reverse_string = z[::-1]
reverse_string_manual = z[len(x) :: -1]
print(reverse_string)
print(reverse_string_manual)

# to reverse a tuple
tuple = (2, 4, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15)

sliced_tuple = tuple[: len(tuple) : 2]
print(sliced_tuple)

# reverse the tuple

reversed_tuple = tuple[::-1]
print(reversed_tuple)

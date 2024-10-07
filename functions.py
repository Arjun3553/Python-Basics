# functions
# syntax
"""
def function(parameters):
    # function body
"""


def print_apple_5_times():
    for i in range(5):
        print(i, "apple")


print_apple_5_times()


# function with parameters
def demo(x, y, z=None):
    print("run", x, y, z)
    return x * y, y / x


# to get the results as tuple
print(demo(5, 6, 8))

# to get the results as separate
result1, result2 = demo(
    5,
    6,
)
print(result1, result2)

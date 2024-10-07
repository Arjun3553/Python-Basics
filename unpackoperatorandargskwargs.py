# advanced functions


def func(x):
    def fun2():
        print(x)

    return fun2


print(func(3)())
x = func(3)
x()


# unpack operator [*variable]
# unpack operator will seperate the collections of elements into individual elements

y = [1, 57849, 34, 2]
print(y)  # without unpack operator
print(*y)  # with unpack operator

# how to pass seperate elements from unpack operator


def func1(x, y):
    print(x, y)


pairs = [(1, 2), (3, 4)]
for pair in pairs:
    func1(*pair)

# *args and **kwargs


def func4(*args, **kwargs):
    print(args, kwargs)
    print(*args)


func4(1, 2, 3, name="John", age=30)

# lambda function

x = lambda x: print(x)
x(2)

# map function
number = [1, 24, 46, 4, 5, 6, 3, 225, 6, 89, 9, 1]
mp = map(lambda x: x * 2, number)
print(list(mp))

# filter function
fp = filter(lambda x: x % 2 == 0, number)
print(list(fp))

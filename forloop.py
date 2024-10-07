# for loops

x = [1, 45, 25, 29, 0, 2]
for i in range(0, 10, 1):
    print(i)

for i in range(len(x)):
    print(x[i])

for i, element in enumerate(x):
    print(i, element)

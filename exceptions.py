# raise is a keyword used to raise an exception
raise Exception("Invalid")

# exception handling
try:
    x = 1 / 0
except Exception as e:
    print(e)
finally:
    print("inside finally block")

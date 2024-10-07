# if elif and else conditions

num1 = int(input("enter the number 1 : "))
num2 = int(input("enter the number 2 : "))
num3 = int(input("enter the number 3 : "))

if num1 > num2 and num1 > num3:
    print("number 1 is greater :", num1)
elif num2 > num3 and num2 > num1:
    print("number 2 is greater :", num2)

else:
    print("number 3 is greater :", num3)

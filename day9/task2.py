# WAP to take three numbers input and print the greatest number


num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))
num3 = int(input("Enter third number: "))


if all([num1 > num2, num1 > num3]):
    print(f"first input number {num1} is the greatest")
elif num2 > num1 and num2 > num3:
    print(f"second input number {num2} is the greatest")
else:
    print(f"third input number {num3} is the greatest")
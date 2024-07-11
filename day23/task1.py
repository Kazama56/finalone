"""
Take two numbers as input and add those numbers. Handle the possible exceptions.
"""

num1 = input("Enter a number ")
num2 = input("Enter another number ")

try:
    num1 = int(num1)
    num2 = int(num2)
except ValueError:
    print("Please input a valid number")
else:
    result = num1 + num2
    print(result)

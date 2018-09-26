"""
Write a program that will take a number (integers only) and return a statement that will let the user know if it is even or odd
"""

x = int(input("enter a number: "))
if (x%2==0):
    print("wow, an even number")
if (x%2==1):
    print("wow, an odd number")


x = float(input("enter a number: "))
if (x%2==0):
    print("wow, an even number")
elif (x%2==1):
    print("wow, an odd number")

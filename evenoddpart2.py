"""
write a program that will ask the user for a number (integers only) and return a statement that the number is even or odd
square root of 5 is 5**(1/2)\
7%2=1
8%6=2
10%2=0

"""

num=int(input("enter a number: "))
if (num%2==0):
    print("cool, an even number")
if (num%2==1):
    print("wow, an odd number")
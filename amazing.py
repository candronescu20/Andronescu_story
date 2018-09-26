"""
this program demonstrates IMPORT statements
"""

#import statements got first (top of your code)
import time

#for variable name in range (start, stop, step)
#OR
# for vaiable name in range (stop): *This will start at 0 and stop by 1
#that i can be anything you want

for i in range (1, 11):
    print("Hello " + str(i))
    
#count to 100 by 5's
for a in range (0, 105, 5):
    print("Hola " + str(a))

#count down from (START AT 20) by 2's and stop at -4
for b in range (20, -6, -2):
    print("Bonjour " + str(b))

#print out a random number btwn -5 and 5 (see amazing.py)
import random
x=random.randint(-5,5)
print(x)
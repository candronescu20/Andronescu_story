#1. print out a random number btwn -5 and 5

import random
for x in range (1):
    print random.randint(-5,5)
    
    #or

import random
a=random.randint(-5,5)
print(a)

#2. print out a random integer btwn 0 and 100 500 times
import random
for b in range(500):
    print random.randint(0, 100)
    
#3. print a random number and determine if its even or odd
x = random.randint(0,100)
if (x%2==0):
    print("the number " + str(x) + " is even.")
else: (x%2==1)
print("the number " + str(x) + " is odd.")
    
#4. print 10 random numbers and determine if they are even or odd along the way
for x in range(10):
    x = random.randint(0,100)
    if (x%2==0):
        print("the number " + str(x) + " is even.")
    else: (x%2==1)
    print("the number " + str(x) + " is odd.")
    
#5. Modify the code in part 4 that will ADD up the number of EVEN numbers and print those results. *hint: use an accumulator variable
acc = 0
for x in range(10):
    x = random.randint(0,100)
    if (x%2==0):
        acc +=1    #this is the same as "acc = acc +1"
        print("the number " + str(x) + " is even.")
    else: (x%2==1)
    print("the number " + str(x) + " is odd.")
print("the number of evens was " + str(acc) + ".")


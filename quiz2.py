#New topic! write the same block of code in a function and call that function 10 times
import random  #try to keep imports outside of loop to not have needless imports

def EvenOdd():     #can call it (funtionName) anything you want EXCEPT for predefined imports/terms (i.e. print, random, etc)
    acc = 0
    for x in range(10):
        x = random.randint(0,100)
        if (x%2==0):
            acc +=1    #this is the same as "acc = acc +1"
            print("the number " + str(x) + " is even.")
        else: (x%2==1)
        print("the number " + str(x) + " is odd.")
    print("the number of evens was " + str(acc) + ".")

EvenOdd()   #this is "calling" a function

def greeting():
    name = input("Hello, human. What arbitrary collection of sounds has been assigned to your arbitrary collection of cells? ")
    print("Duly noted" + name + ".")
    
def age():
    age = int(input("How many revolutions about the Sun have you endured? "))
    return age  #function will not if something is not returned, HOWEVER returning will not store it - msut be saved

"""
this is all about how functions work
"""

def greeting():  # this function does NOT return anything
    print("Hello world")
    
def askName():
    name = input("What is your name? ")   # function can not have the same name as variable
    return name
    
def askAge():  # asks AND returns age
    age = int(input("How old are you? "))
    return age
    
def canVote(age): # age is a local variable  #function takes age IN and responds if they can or can not vote
    if (age >=18):
        print("Hey you can vote.")
        canVote = True 
    else:
        print("Sorry you can't vote.")
        canVote = False
    return canVote

# call the function
greeting()
x = askName() # save the output of askName() to a variable 
print("Hello, " + x)
y = askAge() # y = age
z = canVote(y) # z = ifthey can vote or not (T/F)
print(z)

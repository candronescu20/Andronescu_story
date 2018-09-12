#write a program that will ask the user what their age is and then determine if they are old enough to vote or not and respond appropiately

age = int(input("Hello, how old are you? "))
if age >= 18:
    print("Get out there and vote you geezer! Our democratic process depends on it.")
if age < 18:
    print("Well that sucks. Guess you gotta watch a handful of old men make all the decisions for us like everyone else.")
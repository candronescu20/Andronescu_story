import quiz2    #can import already written functions/files from within package/folder/repository (basically the same thing)
quiz2.EvenOdd()
quiz2.greeting()
x = quiz2.age() #stores the return value of the fuction age()

if (x >=18):
    print("you are old enough to vote.")
else:
    print("in " + str(18 - x) + " years, you will be able to vote.")
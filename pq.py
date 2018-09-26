#program counts down from whatever number the user decides and delays 1 second using the package "time" and the method time.sleep(1) inside the loop.

import time

x = int(input("Please enter an integer: "))
for x in range (x, 0, -1):
    time.sleep(1)
    print(str(x-1))

    
     
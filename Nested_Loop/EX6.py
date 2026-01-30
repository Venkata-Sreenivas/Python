'''To print

*
**
***
****

block '''

import time

for o in range(1,5):
    for i in range(1,o+1):
        time.sleep(0.02)
        print("*", end=" ")

    print(" ")

'''To print Square root and Cube root for the given number'''

import time

n=int(input("Enter a number: "))

for i in range(1,2):
    time.sleep(.02)
    print(n,"Square=",n*n,"Cube=",n*n*n)

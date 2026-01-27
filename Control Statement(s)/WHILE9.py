''' Sum of Natural Numbers'''

import time

s=0
'''n=5'''
n=int(input("Enter a number: "))
i=1
while i<=n:
    time.sleep(.2)
    s=s+i
    print(s)
    i=i+1

print("Sum is: ", s)

''' Find Factorial Values '''

import time

#n=5
n=int(input("Enter a number: "))
i=f=1
while i<=n:
    time.sleep(.2)
    print(i)
    f=f*i
    i=i+1
    
print("Factorial is: ", f)

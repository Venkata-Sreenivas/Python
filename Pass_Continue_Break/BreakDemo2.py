'''To print whether the given number is found or not found in the list'''

import time

lst=[10,30,50,60,70,20,40]

print("List: ",lst)

found=0
sno=int(input("Enter SNo: "))
for i in lst:
    time.sleep(.02)
    if i==sno:
        print("Found")
        found=1
        break

if found==0:
    print("Not Found")

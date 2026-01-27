'''range(stop)-> range object | iterable '''

import time

r=range(10)
print("Tyepe is: ", type(r))
print("Range Object: ", r)

for i in r:
    time.sleep(.02)
    print(i)
print("============================")

'''range(start,stop,step=1)-->range | iterabel
Step value should be positive or negative but not 0'''

r=range(1,11)

for i in r:
    time.sleep(.02)
    print(i)

print("==============================")

r=range(2,22,2)

for i in r:
    time.sleep(.02)
    print(i)

print("=======================================")

#reverse

for i in range(10,0,-1):
    time.sleep(.02)
    print(i)

print("==================================")

'''Error because the step value is 0 it either be positive or negative but no 0'''

for i in range(1,10,0):
    time.sleep(.02)
    print(i)


print("==============================================")

n = int(input("Enter a number: "))

for i in range(1, 11):
    print(n, "x", i, "=", n * i)



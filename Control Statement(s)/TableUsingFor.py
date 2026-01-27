'''To print Table using for loop'''

import time

n = int(input("Enter a number: "))

for i in range(1, 11):
    time.sleep(.02)
    print(n, "x", i, "=", n * i)

print('============================================')

'''To print table in reverse'''

for i in range(10,0,-1):
    time.sleep(.02)
    print(n, "x", i, "=", n * i)


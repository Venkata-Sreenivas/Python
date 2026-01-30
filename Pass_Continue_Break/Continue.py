import sys
import time

i=1
for i in range(1,11):
    time.sleep(.02)
    if i in [5,8,9]:
        continue
    print(i)

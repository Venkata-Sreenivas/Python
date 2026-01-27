'''To print table'''
import time

'''n=2'''
n=int(input("Enter a number: "))
i=1
while i<=10:
    time.sleep(.2)
    print(n, "x", i, "=", n*i)
    i=i+1


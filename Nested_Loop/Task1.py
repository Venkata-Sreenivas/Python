'''To print
*
22
***
4444
*****

 using nested loop'''

for i in range(1, 6):
    for j in range(i):
        if i % 2 == 1:
            print("*", end="")
        else:
            print(i, end="")
    print()

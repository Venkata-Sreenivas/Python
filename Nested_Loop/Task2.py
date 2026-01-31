'''To print

1
1 *
1 * 3
1 * 3 *
1 * 3 * 5

 using nested loop'''

for i in range(1, 6):
    num = 1
    for j in range(1, i + 1):
        if j % 2 == 1:
            print(num, end=" ")
            num += 2
        else:
            print("*", end=" ")
    print()

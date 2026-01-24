''' Enter number or year
Main Menu
============
1. Odd or Even
2. Leap or Not
3. Positive or Negative
4. Exit
==================
Enter ur choice:
'''


import sys

num = int(input("Enter a number or year: "))

print("Main Menu")
print("===========")
print("1. Odd or Even")
print("2. Leap or Not")
print("3. Positive or Negative")
print("4. Exit")
print("====================")

ch = int(input("Enter your choice: "))

match ch:
    case 1:
        if num % 2 == 0:
            print("Even Number")
        else:
            print("Odd Number")

    case 2:
        if (num % 4 == 0 and num % 100 != 0) or (num % 400 == 0):
            print("Leap Year")
        else:
            print("Not a Leap Year")

    case 3:
        if num > 0:
            print("Positive Number")
        elif num < 0:
            print("Negative Number")
        else:
            print("Zero")

    case 4:
        sys.exit()

    case _:
        print("Invalid Choice")

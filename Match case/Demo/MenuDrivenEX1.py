import sys

a=int(input("Enter a number: "))
b=int(input("Enter b number: "))

print("Main Menu")
print("===========")
print("1.Add\n2.Sub\n3.Mul\n4.Exit")
print("========================")

ch=int(input("Enter choice: "))

match ch:
    case 1:
        c=a+b
        print("Result is: ", c)
    case 2:
        if a>b:
            c=a-b
        else:
            c=b-a
            print("Result is: ", c)
    case 3:
        c=a*b
        print("Result is: ", c)
    case 4:
        sys.exit()
    case _:
        print("Invalid Choice: ")

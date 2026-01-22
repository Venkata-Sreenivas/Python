''' Accept numbers from the user and findout and print the number if even else odd'''

n=int(input("Enter a Number: "))

#Conditional Statement
if n%2==0:
    print("Even")
else:
    print("Odd")

#Conditional Operator
print("Even") if n%2==0 else print("Odd")

#Another Aproach
if n%2:
    print("Odd")
else:
    print("Even")


n=int(input("Enter a number: "))

#Conditional Statement
if n==1:
     print("One")
elif n==2:
    print("Two")
elif n==3:
    print("Three")
else:
    print("Invalid")

#Conditional Operator
print("One") if n==1 else print("Two") if n==2  else print("Three") if n==3 else print("Invalid")

'''Accept age from the user print major if age>=21 else print minor '''

age=int(input("Enter age: "))

#Conditional Statement
if age>=21:
    print("Major")
else:
    print("Minor")

#Conditional Operator
print("Major") if age>=21 else print("Minor")

''' Accept char from the user print male if the given char is m else print female'''

ch=input("Enter any char: ")

#Conditional Statement
if ch=='m' or ch=='M':
    print("Male")
else:
    print("Female")

#Conditional Operator
print("Male") if ch=='m' or ch=='M' else print("Female")

##Accept present reading , previous reading calculate no. of unit and find bill

present=int(input("Enter Present Reading: "))
previous=int(input("Enter Previous Reading: "))
number=present-previous
bill=number*2
print("No. of units: ", number)
print("Bill amount is: ", bill)

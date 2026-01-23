''' Accept gender and age from the user findout status of the candidate

if gender is m or M then check the age
if age>=21 print Major else print Minor

if gender is f or F then check the age
if age>=18 then print Major else print Minor

else third-Gender
'''

age=int(input("Enter age: "))
gender=input("Enter any char: ")

if gender in 'mM':
    print("Gender is: Male")
    if age>=21:
        print("Major")
    else:
        print("Minor")
        
elif gender in'fF':
    print("Gender is: Female")
    if age>=18:
        print("Major")
    else:
        print("Minor")
else:
    print("Thrid Gender")

#Aproach 2
lst=['M', 'm', 'f', 'F']

if gender in lst[0:2:1]:
    print("Gender is: Male")
    if age>=21:
        print("Major")
    else:
        print("Minor")
        
elif gender in lst[2:4:1]:
    print("Gender is: Female")
    if age>=18:
        print("Major")
    else:
        print("Minor")
else:
    print("Thrid Gender")

#Aproach 3

if gender in lst[0:2:1]:
    print("Gender is: Male")
    print("Major")if age>=21 else print("Minor")
        
elif gender in lst[2:4:1]:
    print("Gender is: Female")
    print("Major")if age>=18 else print("Minor")
else:
    print("Thrid Gender")
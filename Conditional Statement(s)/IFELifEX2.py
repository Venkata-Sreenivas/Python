''' Accept Service number from the user print service name
if sno is 100 print police
if sno is 101 print fire
if sno is 104 print medical
if sno is 108 print emergency
else print invalid service number
'''
sno = int(input("Enter Service Number: "))

if sno == 100:
    print("Police")
elif sno == 101:
    print("Fire")
elif sno == 104:
    print("Medical")
elif sno == 108:
    print("Emergency")
else:
    print("Invalid Service Number")

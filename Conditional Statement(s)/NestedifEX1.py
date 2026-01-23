''' Nested if
defining the if inside if.....

Accept m1, m2, m3 calculate total, avg and findout rest and grade

result is pass if marks>34 in all subjects
else result is fail
if the result is pass then check the avg marks
if avg>=70 print Grade A
if avg>=60 prrint Grad B
if avg>=50 print Grade C
else Grade D
'''

m1=int(input("Enter m1: "))
m2=int(input("Enter m2: "))
m3=int(input("Enter m3: "))

total=m1+m2+m3
avg=total/3

print("Total is: ", total)
print("Avg is: ", avg)

if m1>=34 and m2>=34 and m3>=34:
    print("Result is Pass")
    if avg>=70:
        print("Grade A")
    elif avg>=60:
        print("Grade B")
    elif avg>=50:
        print("Grade C")
    else:
        print("Grade D")
else:
    print("Result is Fail")
    

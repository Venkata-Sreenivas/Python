''' To find smallest in 5 '''

a = int(input("Enter a number: "))
b = int(input("Enter b number: "))
c = int(input("Enter c number: "))
d = int(input("Enter d number: "))
e = int(input("Enter e number: "))

if a < b and a < c and a < d and a < e:
    print("a is smallest")

elif b < a and b < c and b < d and b < e:
    print("b is smallest")

elif c < a and c < b and c < d and c < e:
    print("c is smallest")

elif d < a and d < b and d < c and d < e:
    print("d is smallest")

else:
    print("e is smallest")

#Aproach 2

if a < b and a < c and a < d and a < e:
    print("a is smallest")

elif b < c and b < d and b < e:
    print("b is smallest")

elif c < d and c < e:
    print("c is smallest")

elif d < e:
    print("d is smallest")

else:
    print("e is smallest")
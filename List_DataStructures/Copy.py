'''L.copy()--->Shallow copy of list
process of creating alternative for exsisted collection is known as reference copy
Process of creating Duplicate collection is known as shallow copy
'''

a=[10,20,30]
print("List a: ",a)

b=a #ref.copy
print("List b: ",b)
print("=======================================")
a[1]=99
print("After modification")
print("List a: ",a)
print("List b: ",b)
print("=====================================")


c=[11,22,33]
print("List c: ",c)

d=c.copy()
print("List d: ", d)
print("=====================================")

c[1]=99
print("After modification")
print("List c: ",c)
print("List d: ",d)

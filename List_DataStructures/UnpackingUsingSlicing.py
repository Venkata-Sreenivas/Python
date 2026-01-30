'''To print Possible Values from list'''

#Unpacking Using Slicing

lst=[10,"Sreenivas","Hyd",40,50,60]
print("List: ",lst)

m1,m2,m3=lst[3:6:1]
print(m1,m2,m3,sep='-')
print("=========================")

#While
import time
index=0
while index<len(lst):
    time.sleep(.02)
    print( lst[index] )
    index=index+1
print("=========================")

#For
for i in lst:
    time.sleep(.02)
    print(i)


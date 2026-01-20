sno=101
sname="Sreenivas"
sage=19
#indexbased
print("sno is : {2} sname is :{0} and age is {1}" .format(sname,sage,sno))

print("sno is : {0} sname is :{1} and \n {1} is awesome" .format(sno,sname))

#namebased
print("sno is : {n} sname is :{na} and \n age is {a}" .format(na=sname,a=sage,n=sno))
print("sno is : {n} sname is :{na} and \n {na} is awesome" .format(n=sno,na=sname))

#error
print("sno is : {2} sname is :{} and age is {1}" .format(sname,sage,sno))

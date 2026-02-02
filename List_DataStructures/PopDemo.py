'''L.pop(index=-1)--->Value'''

a=[10,20,10,30,50]
print("List a: ",a)

item=a.pop()#if not mentioned last item is deleted
print("Deleted item: ",item)
print("List after pop: ",a)

item=a.pop(2)
print("Deleted item: ",item)
print("List after pop: ",a)

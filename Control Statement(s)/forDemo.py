''' Syn:
for<variable>int<iterable>:
....stmt(s)

iterable: is the sequence or collection with countable no.of objects from where we can read one by one object from it

eg: list , tuple, set , str, dict, frozenset, ordereddict, dict_keys, dict_values, dict_items, map, filter, zip, file, cursor......
'''

import time

lst=[10,12.12,"Sreenivas", "Janradhan","Satish", "Rajesh","Reddy"]
print("List: ",lst)

for i in lst:
    time.sleep(.2)
    print(i)
print("====================================================")

t=(10,12.12,"Sreenivas", "Janradhan","Satish", "Rajesh","Reddy")
print("Tuple: ",tuple)

for i in t:
    time.sleep(.2)
    print(i)

s={10,12.12,"Sreenivas", "Janradhan","Satish", "Rajesh","Reddy"}
print("Set: ",s)

for i in s:
    time.sleep(.2)
    print(i)
    
print("=========================")

st="Welcome"

stu={"Sno":101,"Sname":"Sreenivas","Sage":20}
print("Stu: ",stu)

for i in stu:
    time.sleep(0.2)
    print(i)
    
print("===========================================")
Python 3.14.0 (tags/v3.14.0:ebf955d, Oct  7 2025, 10:15:03) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
>>> 
==== RESTART: C:\Users\venka\OneDrive\Desktop\Python\Operators\IdentityOP.py ===
>>> x=10
>>> id(x)
140713723143576
>>> y=20
>>> id(y)
140713723143896
>>> id(x)==id(y)
False
>>> x is y
False
>>> z=x
>>> id(z)
140713723143576
>>> x is z
True

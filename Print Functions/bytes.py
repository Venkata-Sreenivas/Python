Python 3.14.0 (tags/v3.14.0:ebf955d, Oct  7 2025, 10:15:03) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
>>> a="sreenivas"
>>> type(a)
<class 'str'>
>>> b="venkata"
>>> type(b)
<class 'str'>
>>> lst=[10,20,30]
>>> b=bytes(lst)
>>> type(b)
<class 'bytes'>
>>> print(b)
b'\n\x14\x1e'
>>> b[1]=12
Traceback (most recent call last):
  File "<pyshell#8>", line 1, in <module>
    b[1]=12
TypeError: 'bytes' object does not support item assignment
>>> lst=[10,30,20, 40,50]
>>> ba=bytearray(lst)
>>> type(ba)
<class 'bytearray'>
>>> print(ba)
bytearray(b'\n\x1e\x14(2')
>>> ba[1]=22
>>> print(ba)
bytearray(b'\n\x16\x14(2')

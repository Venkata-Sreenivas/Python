Python 3.14.0 (tags/v3.14.0:ebf955d, Oct  7 2025, 10:15:03) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
>>> r=range(10)
>>> type (r)
<class 'range'>
>>> 
>>> r=range(1,10)
>>> type(r)
<class 'range'>
>>> print(r)
range(1, 10)
>>> r=range(1,10,2)
>>> type(r)
<class 'range'>
>>> print(r)
range(1, 10, 2)
>>> 
>>> range(10,20,30,40)
Traceback (most recent call last):
  File "<pyshell#10>", line 1, in <module>
    range(10,20,30,40)
TypeError: range expected at most 3 arguments, got 4
>>> 
>>> 
>>> 
>>> 

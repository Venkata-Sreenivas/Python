Python 3.14.0 (tags/v3.14.0:ebf955d, Oct  7 2025, 10:15:03) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
>>> x="12.12"
>>> int(x)
Traceback (most recent call last):
  File "<pyshell#1>", line 1, in <module>
    int(x)
ValueError: invalid literal for int() with base 10: '12.12'
>>> str(x)
'12.12'
>>> float(x)
12.12
>>> x=0b10
>>> type(x)
<class 'int'>
>>> print(x)
2
>>> type(x)
<class 'int'>
>>> x=0b10
>>> x=0o10
>>> type(x)
<class 'int'>
>>> print(x)
8

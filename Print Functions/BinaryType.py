Python 3.14.0 (tags/v3.14.0:ebf955d, Oct  7 2025, 10:15:03) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
>>> 
= RESTART: C:/Users/venka/OneDrive/Desktop/Python/Print Functions/StringDatatypes.py
>>> fs=open
>>> fs=open("D:\\WhatsApp Image 2025-10-18 at 11.00.07_e45e3184.jpg","rb")
>>> b=fs.read()
>>> type(b)
<class 'bytes'>
>>> ft=open("D:\\WhatsApp Image 2025-10-18 at 11.00.07_e45e3184.jpg", "wb")
>>> ft=open("D:\\WhatsApp Image 2025-10-18 at 11.00.07_e45e3184.jpg", "wb")
>>> ft=open("C:\Users\venka\OneDrive\Desktop\Python\Print Functions", "wb")
SyntaxError: (unicode error) 'unicodeescape' codec can't decode bytes in position 2-3: truncated \UXXXXXXXX escape
>>> ft.write(b)
235278
>>> fs.close()
>>> ftclose()
Traceback (most recent call last):
  File "<pyshell#9>", line 1, in <module>
    ftclose()
NameError: name 'ftclose' is not defined
>>> ft.close()

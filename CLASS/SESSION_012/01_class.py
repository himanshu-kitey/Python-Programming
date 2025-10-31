Python 3.13.7 (tags/v3.13.7:bcee1c3, Aug 14 2025, 14:15:11) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
>>> s = 'Himanshu'
>>> print(s)
Himanshu
>>> type(s)
<class 'str'>
>>> s1 = s.upper()
>>> print(s1)
HIMANSHU
>>> print(s)
Himanshu
>>> 
>>> u = 'PYTHON'
>>> print(u)
PYTHON
>>> type(u)
<class 'str'>
>>> u1 = u.lower()
>>> print(u)
PYTHON
>>> print(u1)
python
>>> 
>>> s = 'Himanshu:Sanjay:Kitey'
>>> L = s.split(':')
>>> print(s)
Himanshu:Sanjay:Kitey
>>> print(L)
['Himanshu', 'Sanjay', 'Kitey']
>>> 
>>> v = 'Himanshu:Sanjay:Kitey'
>>> L = str.split(v, ':')
>>> print(L)
['Himanshu', 'Sanjay', 'Kitey']

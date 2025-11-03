Python 3.13.7 (tags/v3.13.7:bcee1c3, Aug 14 2025, 14:15:11) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
b2 = False
b1 = True
type(b1)
<class 'bool'>
type(b2)
<class 'bool'>
int("1")
1
int(1.0)
1
int(0)
0
int("0")
0
int(False)
0

#Not Operator
print('b1:', b1)
b1: True
c = not b1
>>> print('c:', c)
c: False
>>> b2 = False
>>> print('c:', c)
c: False
>>> 
>>> print('Himanshu')
Himanshu
>>> print('b1',b1,'b2',b2)
b1 True b2 False
>>> c = b1 and b2
>>> print(c)
False
>>> c = b1 and b1
>>> print(c)
True
>>> c = b2 and b1
>>> print(c)
False
>>> c = b2 and b2
>>> print(c)
False
>>> 
>>> #OR Operator
>>> print(b1, b2)
True False
>>> c = b1 or b2
>>> print(c)
True
>>> c = b2 or b1
>>> print(c)
True
>>> c = b1 or b1
>>> print(c)
True
>>> c = b2 or b2
>>> print(c)
False

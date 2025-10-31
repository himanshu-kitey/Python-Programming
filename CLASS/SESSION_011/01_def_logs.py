Python 3.13.7 (tags/v3.13.7:bcee1c3, Aug 14 2025, 14:15:11) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
#Function with 0 or no formal Parameter
def testFunction():
    print('This is a testFunction() which dose nothing apart from printing this msg')

    
testFunction()
This is a testFunction() which dose nothing apart from printing this msg

#Function with 1 formal Paramater
def testFunction(param_1):
    print('Value of Param_1:', param_1)
    print('Type of Param_1:', type(param_1))
    print('Id of param_1:', id(param_1))

    
testFunction(1500)
Value of Param_1: 1500
Type of Param_1: <class 'int'>
Id of param_1: 2426436918960
testFunction(13.45)
Value of Param_1: 13.45
Type of Param_1: <class 'float'>
Id of param_1: 2426427472176
testFunction('Himanshu')
Value of Param_1: Himanshu
Type of Param_1: <class 'str'>
Id of param_1: 2426438110256
#Function with 2 formal Paramter
def testFunction(x, y):
    print('Value of x:', x)
    print('Value of y:', y)
    print('id of x:', id(x))
    print('id of y:', id(y))
    print('type of x:', type(x))
    print('type of y:', type(y))

    
testFunction(100, 200)
Value of x: 100
Value of y: 200
id of x: 140736637992968
id of y: 140736637996168
type of x: <class 'int'>
type of y: <class 'int'>
>>> testFunction(12.34, 45.67)
Value of x: 12.34
Value of y: 45.67
id of x: 2426398299376
id of y: 2426427472496
type of x: <class 'float'>
type of y: <class 'float'>
>>> testFunction('Himnshu', 'Kitey')
Value of x: Himnshu
Value of y: Kitey
id of x: 2426438039088
id of y: 2426438040768
type of x: <class 'str'>
type of y: <class 'str'>
>>> testFunction(True)
Traceback (most recent call last):
  File "<pyshell#27>", line 1, in <module>
    testFunction(True)
TypeError: testFunction() missing 1 required positional argument: 'y'
>>> testFunction(True, False)
Value of x: True
Value of y: False
id of x: 140736637104560
id of y: 140736637104592
type of x: <class 'bool'>
type of y: <class 'bool'>
>>> testFunction('Himanshu', 12)
Value of x: Himanshu
Value of y: 12
id of x: 2426438110256
id of y: 140736637990152
type of x: <class 'str'>
type of y: <class 'int'>
>>> testFunction(12,12.34)
Value of x: 12
Value of y: 12.34
id of x: 140736637990152
id of y: 2426427472176
type of x: <class 'int'>
type of y: <class 'float'>

Python 3.13.7 (tags/v3.13.7:bcee1c3, Aug 14 2025, 14:15:11) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
>>> 
= RESTART: C:\Users\HimanshuKitey\OneDrive\HIMANSHU_2025\HIMANSHU_2025_2026\EMBEDDED_SYSTEM_2025_2026\PYTHON_PROGRAMMING\GIT-REPO\CLASS\SESSION_005\01_sys.getrefcount.py
>>> import sys
>>> a = 10
>>> a = 34567890
>>> sys.getrefcount(a)
2
>>> b = 1
>>> b = a
>>> sys.getrefcount(a)
3
>>> c = b
>>> sys.getrefcount(a)
4
>>> b = 2394735932759872
>>> sys.getrefcount(b)
2
>>> c = 34779827852
>>> sys.getrefcount(a)
2
>>> del a

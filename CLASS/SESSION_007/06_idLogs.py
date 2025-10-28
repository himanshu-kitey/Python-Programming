Python 3.13.7 (tags/v3.13.7:bcee1c3, Aug 14 2025, 14:15:11) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
>>> m  = 17
>>> n = 15
>>> id(m)
140718468003240
>>> id(n)
140718468003176
>>> m = 17
>>> n = 17
>>> id(m)
140718468003240
>>> id(n)
140718468003240
>>> m = 1234567890
>>> n = 1234567890
>>> id(n)
1897634143600
>>> id(m)
1897634136208

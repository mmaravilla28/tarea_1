Python 3.7.2 (tags/v3.7.2:9a3ffc0492, Dec 23 2018, 22:20:52) [MSC v.1916 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> import math
>>> PI = str(math.pi)
>>> PI
'3.141592653589793'
>>> valor = '%s %.9s %s %.8s %s %.7s %s %.6s %s %.5s %s %.4s' % ('*',PI,'**',PI,'***',PI,'****',PI,'*****',PI,'******',PI)
>>> print(valor)
* 3.1415926 ** 3.141592 *** 3.14159 **** 3.1415 ***** 3.141 ****** 3.14
>>> 

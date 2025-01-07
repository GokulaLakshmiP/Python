Python 3.13.1 (tags/v3.13.1:0671451, Dec  3 2024, 19:06:28) [MSC v.1942 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
#Type this in python shell window - Strings
a="me"
b='you'
c=a+b
c
'meyou'
c=a+" "+b
c
'me you'
silly=a*3
silly
'mememe'
b=":"
c=")"
s1=b+2*c
s1
':))'
f="a"
g="b"
h="3"
s2=(f+g)*int(h)
s2
'ababab'
#String operations
s="abc"
len(s)
3
char=len(s)
char
3
#Slicing
s="abc"
s[0]
'a'
s[1]
'b'
s[2]
'c'
s[-1]
'c'
s[-2]
'b'
s[-3]
'a'
>>> #Slicing to get substring
>>> s="abcdefgh"
>>> s[3:6]
'def'
>>> s[3:6:2]
'df'
>>> s[:]
'abcdefgh'
>>> s[::-1]
'hgfedcba'
>>> s[4:1:-2]
'ec'
>>> s="ABC d3f ghi"
>>> s[3:len(s)-1]
' d3f gh'
>>> s[4:0:-1]
'd CB'
>>> s[6:3]
''
>>> s[4:-1:-1]
''
>>> #Strings are immutable
>>> s="car"
>>> s[0]
'c'
>>> s[0]='b'
Traceback (most recent call last):
  File "<pyshell#46>", line 1, in <module>
    s[0]='b'
TypeError: 'str' object does not support item assignment
>>> s='b'+s[1:len(S)]
Traceback (most recent call last):
  File "<pyshell#47>", line 1, in <module>
    s='b'+s[1:len(S)]
NameError: name 'S' is not defined
>>> s="car"
>>> s="b"+s[1:len(s)]
>>> s
'bar'

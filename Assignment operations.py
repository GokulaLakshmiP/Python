Python 3.13.1 (tags/v3.13.1:0671451, Dec  3 2024, 19:06:28) [MSC v.1942 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
#Type this in python shell window - Which of these are allowed in python?
#Assignment - (variable=value)
x=6
6=x
SyntaxError: cannot assign to literal here. Maybe you meant '==' instead of '='?
x*y=3+4
SyntaxError: cannot assign to expression here. Maybe you meant '==' instead of '='?
xy=3+4
xy
7
xy+1
8
pi=355/113
radius=2.2
area=pi*(radius*2)
>>> circumference=pi*(radius*2)
>>> #Best code style
>>> a=355/133 *(2.2*2)
>>> c=355/133 *(2.2*2)
>>> #Instead of reusing
>>> a=c
>>> #Executed in order - what are the values of meters and feet variables at each line in the code
>>> meters=100
>>> feet=3.2802*meters
>>> meters=200
>>> feet
328.02
>>> meters
200
>>> #Swap values of x and y without binding the numbers directly
>>> x=1
>>> y=2
>>> y=x
>>> y
1
>>> x=y
>>> x
1
>>> y=2
>>> y=x
>>> x=temp
Traceback (most recent call last):
  File "<pyshell#32>", line 1, in <module>
    x=temp
NameError: name 'temp' is not defined
>>> x=1
>>> y=2
>>> temp=y
>>> y=x
>>> x=temp
>>> x
2
>>> y
1

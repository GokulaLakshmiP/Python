Python 3.13.1 (tags/v3.13.1:0671451, Dec  3 2024, 19:06:28) [MSC v.1942 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> #Type this in the python shell window - Try Newton Raphson for cube root
... 
>>> x=int(input('What x to find the cube root of?'))
What x to find the cube root of?3
>>> g=int(input('What guess to start with?'))
What guess to start with?4
>>> print('Current estimated cubed =', g**3)
Current estimated cubed = 64
>>> next_g=g-((g**3-x)/(3*g**2))
>>> print('Next guess to try=',next_g)
Next guess to try= 2.729166666666667

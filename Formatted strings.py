Python 3.13.1 (tags/v3.13.1:0671451, Dec  3 2024, 19:06:28) [MSC v.1942 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> #Type this in the python shell window - F Strings
>>> num=3000
>>> fraction=1/3
>>> print(num*fraction,'is', fraction*100, '% of', num)
1000.0 is 33.33333333333333 % of 3000
>>> print(num*fraction,'is', str(fraction*100) + '% of', num)
1000.0 is 33.33333333333333% of 3000
>>> #Expressions in curly braces evaluated at  runtime, automatically converted to strings, and concatenated to the string preceding them
>>> print(f'{num*fraction} is {fraction*100}% of {num}')
1000.0 is 33.33333333333333% of 3000

>>> #Type this in the python shell window - Comparison operators
>>> 'a'=='A'
False
>>> 2<3
True
>>> not (2<3)
False
>>> #Comparison with logical operator
>>> (2<3) and (3<4)
True
>>> (2<3) and (3>4)
False
>>> pset_time=15
>>> sleep_time=8
>>> print(sleep_time>pset_time)
False
>>> derive=True
>>> drink=False
>>> both=drink and derive
>>> print(both)
False
>>> #Write a program that 1.Savesa secret number in a variable 2.Asks the user for a number guess 3.Prints a bool False or True depending on whether the guess matches the secret
>>> secret=5
>>> guess=int(input("Please guess a number: "))
Please guess a number: 4
>>> print(secret==guess)
False
>>> #Another method
>>> e=print(secret==guess)
False
>>> 5
5


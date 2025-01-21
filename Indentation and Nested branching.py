x = float(input("Enter a number for x: "))  
y = float(input("Enter a number for y: "))  

if x == y:
    print("x and y are equal")
    if y != 0:
        print("Therefore, x/y is", x / y)
elif x < y:
    print("x is smaller")
else:
    print("y is smaller")

print("Thanks!")



#You try it(Write a program that 1.Saves a secret number. 2.Asks the user for a number guess. 3.Prints whether the guess is too low, too high, or the same as the secret.
secret = 5
guess = int(input("Guess a num: "))

if guess > secret:
    print("too high")
elif guess == secret:
    print("Equal")
else:
    print("too low")
         
                

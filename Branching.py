pset_time = 22
sleep_time = 1

if (pset_time + sleep_time) > 24:
    print("impossible!")
elif (pset_time + sleep_time) == 24:
    print("full schedule!")
else:
    leftover = abs(24 - (pset_time + sleep_time))
    print(leftover, "h of free time!")

print("end of day")

#You try it!
x=int(input("Enter a number for x: "))
y=int(input("Enter a different number for y:"))
if x == y:
      print(x,"is the same as",y)
      print("These are equal!")
      

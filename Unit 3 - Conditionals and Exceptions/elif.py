# the if statement has two buddies
# the first little buddy is the the else statement

x = 10

if x > 0:   # not every if needs an else
    print("x is a postiive number")

# the second little buddy is the elif (else if)
elif x < 0:
    print("x is a negative number")

else:       # else always needs an if
    print("x is zero")



light = input("What color is the light?\n>")

if light.lower() == "green":
    print("GO")

elif light.lower() == "yellow":
    print("STOP IF SAFE")

elif light.lower() == "red":
    print("STOP")

else:
    print("YIELD")



x = 10

if x > 5:
    print("x is greater than 5")

if x > 8:
    print("x is greater than 8")

####################################
if x > 5:
    print("x is greater than 5")

elif x > 8:
    print("x is greater than 8")
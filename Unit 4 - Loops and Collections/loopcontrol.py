# Loop control statements
# Allow you to change how loops operate
# They do things like quit the loop early, skip the current loop, or even do nothing at all
# break, continue, pass

# break
# exits a loop prematurely, before it was supposed to end
# happens immediately when ran
# program continues where the loop ended

# example

bag_of_fruit = ["apple", "orange", "bug", "kiwi", "watermelon", "mango"]

for fruit in bag_of_fruit:
    if fruit == "bug":
        print("You found a nasty bug...")
        break   # the break statement exits the loop immediately and continues on
    else:
        print("You ate a " + fruit)

print("All done!")

# Continue
# skips the current loop
# it does exit the entire loop, just moves on to the next iteration

# Example
orders = [19, 30, 35, 23, 100, 3, 10, 22]

# Discount applying program
# Only apply discount for orders above $20

for order in orders:
    if order < 20:
        continue
    print("$" + str(order) + " order discounted 5% to $" + str(order * 0.95))

# Pass
# does nothing!!!
# usually used as a placeholder while writing code
# Text-Adventure project

if True:
    pass

def enter_forest():
    pass

def swim_river():
    pass

def eat_icecream():
    pass
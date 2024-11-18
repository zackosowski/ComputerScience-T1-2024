import random

r = random.randrange(0,10)
# First number is INCLUSIVE, second is EXCLUSIVE
# 0 <= result < 10
print(r)

print("You have a 25 percent chance to win!")
p = random.random()
# random.random generates a random float between 0 and 1
print(p)
if p <= 1/8000:
    print("YOU WIN!!")
else:
    print("YOU LOOSE")


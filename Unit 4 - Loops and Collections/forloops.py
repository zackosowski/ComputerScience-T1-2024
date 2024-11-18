#For loops
#This is BIG deal
#For loops allow the programmer to REPEAT, or what we call LOOP

#Write a program that prints the numbers 1 through 10
#Each on a new line

fav_foods = ["Eggs Bennedict", "Fried Chicken", "Mac n Cheese"]

#for <var> in <list>:

for i in range(90,101):
    print(i)

for f in fav_foods:
    print(f)
    #Runs all of the lines inside the for loop
    #When it reaches the bottom the list, it runs again
    #And moves on to the next item in the list
    #It ends when there are no list items left


#**Print a Countdown**: Create a countdown from 10 to 1 using a for loop. Print each number on a new line.

for i in range(10, 0, -1): #START, STOP, STEP
    print(i)

#Sum of a List
nums = [68, 70, 419, 421, 665]
sum = 0
for n in nums:
    sum = sum + n

print(sum)

#Square of Each Number
ints = [3,2,5,4,1]
newlist = []

for i in ints:
    newlist.append(i*i)

print(newlist)

#Character Count

stringy = input("Please enter a string\n>")
numvowels = 0
for s in stringy: 
    if s.lower() in ["a", "e", "i", "o", "u"]:
        numvowels = numvowels + 1

print(numvowels)

#Print Multiplication Table
try:
    multi = int(input("Gimme an int yo!\n>"))
except:
    print("womp womp")

for i in range(0,multi+1):
    print(str(multi) + " x " + str(i) + " = " + str(multi*i))


#Lsit of Names
names = ["Peter", "John", "Paul", "Luke"]
for name in names:
    print("Hello, " + name + "!")


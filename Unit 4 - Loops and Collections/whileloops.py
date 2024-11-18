# There'a couple types of loops in python
# The for loop  lets you iterate through a list
# -great for looping a set number times
# BUT WHAT IF we need to loop an uncertain number of times???
# ex. Entering your password
# You could get it right the first time
# It could could you a million tries
# Or anything in between


real_pass = "ninjalowtaper"
entered_pass = ""

attempts = 0

while entered_pass != real_pass:
    #Ask for the password
    entered_pass = input("Please enter the password\n>")
    attempts = attempts + 1
    #Check if password is correct
    if entered_pass == real_pass:
        print("ACCESS GRANTED")
    else:
        print("ACCESS DENIED")
        print(str(attempts) + " attempts")
        print("try again...")

print("Welcome!")

# With while loops, you need to be careful for infinite loops
# When you put your computer into rest mode, it has nightmares about infinite loops /joke
# An infinite loop happens when you enter a loop that can never be escaped
# Like black holes
# Don't create a black hole
# Let's create a black hole


#Real world example

user_input = ""

while user_input != "exit":
    user_input = input("Enter something!")
    print("type 'exit' to quit")
    print("You typed: " + user_input)

print("All done!")



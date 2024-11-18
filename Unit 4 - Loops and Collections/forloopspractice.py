#For loops review
#For loops allow us to iterate through a list!
#Iterate: perform repeatedly
# to do something repeatedly
# to look at every item in a list, one by one

#Basic Syntax
#Syntax: The "grammar" of the code

pokemon_cards = ["Squirtle", "Bidoof", "Zigzagoon", "Charizard"]

for card in pokemon_cards:
    print("The next card is...")
    print(card)

route = ["Home", "Taco Bell", "The Park", "Goodwill", "Home"]
#Changing your mind can sometimes be the most difficult thing you ever do

#If you need to look at multiple list items during the same iteration,
# Doing "for item in list", doesnt really work...
# "for item in list" only allows you to access one list item per iteration
for location in route:
    print("You are traveling from " + location + " to " + location[1])
    #This doesnt work!!

#If you need to access multiple list items during the same iteration,
# using "for variable in range()" is preferred
for i in range(0, len(route)): #Creates a list [0, 1, 2, 3, 4]
    #Use a try/except block to handle index out of range error
    #Error will happen on the last iteration
    #Because i+1 would be larger than there are items in the list
    try:
        print("You are traveling from " + route[i] + " to " + route[i+1])
    except:
        print("Route finished!")




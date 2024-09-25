animal = input("What is your favorite animal?\n>") # Ask for animal
why = input("What is the " + animal + " your favorite?\n>") #Ask why
color = input("What color is the " + animal + "?\n>")   #Ask about color
location = input("Where does the " + animal + " live?\n>")  #Ask about location
diet = input("What does the " + animal + " eat?\n>")    #Ask about what it eats

#Print the summary
print("Your favorite animal is the " + animal + " because " + why + ". It is " + color + ", eats " + diet + ", and lives in " + location + "!")

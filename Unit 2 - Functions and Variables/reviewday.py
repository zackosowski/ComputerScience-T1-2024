#2 functions
print("Hello, World!")          # "Hello, World!" is the parameter
input("Please enter your username\n>")  # \n is called an escape character
# \n starts a new line (linebreak)
# input is never required

# variables
#Syntax
# <name> = <value>
x = 5

# Snake naming convention - all lowercase, underscore for spaces
# CONCISE: Short and descriptive
username = "osowski"        #Define string ("string" of characters)
fav_animal = "Calugo"       #Define string  ("string" of characters)
total_poptarts = 12         #Define integer (whole number)
percent_complete = 23.52    #Define float (decimal numeber)
is_cool = True              #Define Boolean (True/False)
first_letter = 'c'          #Define Character (single symbol)

total_poparts = 8           #Reassign


# Arithmetic Operators
#   +   -   *   /   **  %   //
print(4 + 4)            #> 8
print("4" + "4")        #> 44
print("cat" + "dog")    #> catdog
print("cat" * 3)        #> catcatcat
print("cat" + 3)        #> ERROR: Cannot use + for string and int

#Make some working programs
# 1. add two numbers using input
x = int(input("What is x?\n>"))     # input() always returns a string                      
y = input("What is y?\n>")          # even if you type in a number
y = int(y)                          # convert from string to int
print(x + y)

# 2. Converts celcius to farenheight using input
temp_celcius = input("What is the temperature in Celcius?\n>")
temp_celcius = int(temp_celcius)                    #convert to integer
temp_farenheight = (temp_celcius * 1.8) + 32    
print(temp_celcius + " degrres C equals " + temp_farenheight + " degrees F")


#Some conversion functions
str()
int()
float()
bin()
bool()

#The stuff that goes between the parenthesis is called PARAMETERS
#Parameters are the values that the function needs to run


# Fuctions
# Functions are a lot like variables
# They have names
# They can be recalled from memory by calling their name
# Store information
# Variables store values, functions store code
def potato():           #def keyword + name + () + :
    print("potato")     #lines indented underneath are "inside" the function

# functions are not ran when they are defined
# they must be called by their name to run
potato()    # Every function call needs open and closed parenthesis
            # even if it has no parameters

def jump(how_high):
    print("You jumpped " + str(how_high) + " inches!")

jump(14)

def make_a_word(a, b, c, d, e, f, g, h, i, j, k):
    print(a + b + c + d + e + f + g + h + i + j + k)

make_a_word("Z", "a", "c", "k", "O", "s", "o", "w", "s", "k", "i")

#Functions can have many many lines
def top_ten_games():
    print("1. Elden Ring")
    print("2. Shadow of the Colossus")
    print("3. Minecraft")
    print("4. Diablo 3")
    print("5. Gran Turismo 7")
    print("6. Overwatch")
    print("7. Rachet & Clank: Up Your Arsenal")
    print("8. World of Warcraft")
    print("9. Path of Exile")
    print("10. Enter the Gungeon")

#Scope: Global and Local Variables!!
#Scope refers to the context in which the variable was defined
#GLOBAL- defined at no indentation level
#LOCAL- defined inside of a function

#Global variables can be used anywhere
todd = "cool guy"       #Global variable- no indentation level

#Local variables only exist in the scope they were defined
def my_function():
    smith = "not cool guy"  #Local variable- define in a function
    todd = "strange guy"    #Local variable even though it has the same name
    print(todd)             #Prints "strange guy" - local variable
    # When you call a variable in a function
    # It searches local variables first, then global variables

#If you want to reassign a global variable inside of a function
todd = "cool guy"
def my_function2():
    global todd             # In this function, whenever I call todd
                            # I mean the global todd, not the local
    todd = "strange guy"    # Reassign todd - global
    print(todd)             # print todd - global

#Return functions
#Fuctions can also return values
#The value that is returned is sent back to where the function was called
#This is very similar to how a variable works
#The function does its work and returns an answer back
def add2(x, y):
    return x + y    #returns the sum of x and y to where the function was called

print(add2(2, 10))  

# 2 basic functions
# You know something is a function because is has () at the end
# The stuff that goes in those () are called parameters
# Parameters are informatio the function needs to run
# I say jump, you say how high? How high is the parameter
print("Hello World!")   # "Hello World!" is the parameter
input("What is your favorite animal?\n>")
# \n is called an escape character (linebreak)
# input is never required, only use it when necessary

# Variables
# Variables are a way to store data for later use in the program
# Syntax (grammar)
# <name> = <value>
x = 5       # x is the variable name, 5 is the value
# Snake naming convention - all lowercase, underscores for spaces
# CONCISE: Short and descriptive
username = "Osowski"            #Define string (string of characters)
fav_animal = "Calugo"           #Define string  
total_poptarts = 12             #Define integer (whole numbers)
percent_complete = 23.52        #Define float (decimal numbers)
is_cool = True                  #Define Boolean (True/False values)
first_letter = 'c'              #Define character (single keyboard symbol)

total_poptarts = 8              #Reassigning variable

# Arithmetic operators (sounds scary, just basic math)
#   +   -   *   /   **  %   //
print(2 + 2)            #>8
print("2" + "2")        #>22
print("cat" + "dog")    #>catdog
print("cat" * 3)        #>catcatcat
print("cat" + 3)        #>ERROR: Cannot use + for string and int
print("cat" * "dog")    #>ERROR: Cannot use * for string and string

my_variable = 2 + 3     # Arithmetic operations can be done anywhere

# Make some working programs
#1. add two numbers using input
x = input("What is x?\n>")  #input function always returns a string
x = int(x)                  #Convert string ot int

y = input("What is y?\n>")  
y = int(y)                  #Convert string to int

print(x + y)                #Print result

#2. Convert Celcius to Farenheight using input
temp_celcius = input("What is the tmeperature in Celcius?\n>")
#Input always returns a string, even if you enter a number
temp_celcius = int(temp_celcius)
temp_farenheight = (temp_celcius * 1.8) + 32
print(temp_celcius + "° C is " + temp_farenheight + "° F")

# Conversion functions
str()
int()
float()
bool()
bin()

# Functions
# Functions are lot like variables
# They have names
# They can be recalled from memory by calling their name
# Store information
# Variable store a value, functions store code
# def <name> ():
def potato():
    print("tomato")

potato()        # Every function call needs parenthesis
                #Even if it has no parameters

def jump(how_high):
    how_high = str(how_high)        #Convert to string for concatentation
    print("You jumped " + how_high + " inches high.")

jump(14)

# Scope
# Global vs Local variables
#GLOBAL: defined at no indentation level
#LOCAL: defined inside of functions, also parameters are local vars

#Global variables can be used anywhere
todd = "cool guy"       #GLOBAL VARIABLE - no indentation level

#Local variables only exist in the context the y were defined in
def my_function():
    global todd     #In this function, todd is referring to the global version
    smith = "not cool guy"
    todd = "strange guy"
    print(todd)         # strange guy
    print(smith)        # not cool guy

print(todd)             # strange guy
print(smith)            #ERROR: using a local varible out of scope

#Return functions
# Functions can also return values
# The value that is returned is sent back to where the function was called
# This is very similar to how variables work
# The function does it work, and returns an answer back
def add_two_numbers(x, y):
    solution = x + y
    return solution      

print(add_two_numbers(10, 5))
answer = add_two_numbers(10, 16)
print(answer)

x = "5"
x = int(x)

# String functions
# String functions are a group of functions that modify strings
# .lower()
# .lower() changes the string to be all lowercase
# .upper() changes the string to uppercase

# .captialize() changes the entire string to lowercase, then capilizes the first letter
# "Hello World!" > "Hello world"

# .title()  changes the entire string to titlecase (capital first letter on each word)
# "hello world" > "Hello World"

# .swapcase() inverts the capitalization of each character
# "Hello World!" > "hELLO wORLD!"

a1 = input("What is Mr. Osowski's favorite game?\n>")
a2 = input("What is Mr. Osowski's favorite movie?\n>")
a3 = input("What is Mr. Osowski's favorite color\n>")

def tally_score():
    score = 0
    if a1.lower() == "elden ring":
        score = score + 1
        
    if a2.lower() == "lord of the rings":
        score = score + 1
        
    if a3.lower() == "black":
        score = score + 1

    print(str(score) + "/5")

tally_score()
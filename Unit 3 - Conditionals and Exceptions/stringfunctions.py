# String functions1
# A group of like-functions that manipulate strings
# The modify strings
# SUPER easy and convenient to use
# Python would really not be fun without them

#   .lower()
# converts a string to all lowercase
# no matter what the input casing is, it is converted to lowercase
# and the answer is lowercase
input_answer = "Lord of The Rings"
input_answer = input_answer.lower() # Converts to "lord of the rings"
real_answer = "lord of the rings"
print(input_answer == real_answer)

# .upper()
# Converts a string to uppercase!
x = "hello world".upper()
print(x)    # prints "HELLO WOLRD"

# .capitalize()
# converts to lowercase, then capitalizes the first letter
y = "HeLlO wOrLd".capitalize()
print(y)    # print "Hello world"

# .title()
# converts a string to titlecase
#capital first letters of words
z = "HeLlO wOrLd".title()
print(z)    # print "Hello World"

# .swapcase()
# it inverts the casing of eac character
q = "Hello World!".swapcase()
print(q)    #prints "hELLO wORLD!"
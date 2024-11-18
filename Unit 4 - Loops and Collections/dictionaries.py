# Dictionary is a type of collection like a list
# A list is a collection of items in a sequence
# A Dictionary is different
# Dictionaries store data in key-value pairs
# You can retreive data quickly by using a unique key
# instead of retreiving it by index (position)

# Example
# Lists use brackets [], dictionaries use braces {}

osowski = {
    "name": "Osowski",
    "age": 31,
    "city": "St. Michael",
    "pets": 2,
    "height": 6.5
}

# Each key must be unique

# Retrieving values from a dictionary
print(osowski["name"])  # Prints the name
print(osowski["age"])   # Prints the age

# This will error if you give a key that doesnt exist!
#print(osowski["country"]) This errors!

# .get allows you to retrieve a calue without erroring
# when the key doesn't exist
# the second parameter is what is given if the value is not found
print(osowski.get("height"))
print(osowski.get("country", "Country not found"))

# You can add new values to an existing dict
osowski["country"] = "USA"

# You can modify existing values
osowski["age"] = 32

# You can remove existing values
osowski.pop("pets")

# Iterate through a dictionary using a for loop!
for key, value in osowski.items():
    print(key + " = " + str(value))

# Dictionary Functions
print(osowski.keys())   #returns all keys
print(osowski.values()) #returns all values
print(osowski.items())  #returns all key-value pairs
print(osowski.clear())  #removes all items from the dict



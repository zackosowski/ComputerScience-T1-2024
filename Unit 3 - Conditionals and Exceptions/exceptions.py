# Exception Handling
# Write a program that asks for two numbers and divides them

# if    =   try
# elif  =   except with error type
# else  =   except
def divide_two_numbers():
    try:    # We always enter the try block, there is no condition
        x = int(input("What is the first number?\n>"))
        y = int(input("What is the second number?\n>"))
        print(x / y)

    except ZeroDivisionError:
        print("Cannot divide by zero, try again.")
        divide_two_numbers()   

    except ValueError:
        print("Please enter a valid numerical symbol, try again.")
        divide_two_numbers()   

    except: # If anything in the try block causes an error,
            # the try block stops immediately and the except is ran instead
            # The rest of the try block never finishes running, its skipped
            # If the try block executes without an error, the except is skipped
            # the only way to get into the except is to "throw" an error
        print("IDK what you did, but you broke it... Try again.")
        divide_two_numbers()    # Tell the function to run again

divide_two_numbers()


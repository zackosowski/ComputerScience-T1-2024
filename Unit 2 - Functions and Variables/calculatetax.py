def calculate_tax(item, price, rate):   #Define function
    print("A " + item + " that costs $" + str(price) + " has a tax of " + str(price * rate))

    
calculate_tax("Baseball", 4.99, 0.06875)    #Run the function
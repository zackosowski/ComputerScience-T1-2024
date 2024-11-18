#Import random tools
import random

#Generate a list of five random numbers
numbers = [random.randint(0,101),random.randint(0,101),random.randint(0,101),random.randint(0,101),random.randint(0,101)]


print("BUBLE SORT")
#Print the list before it is sorted
print(numbers)

#Define the function
def bubble_sort(n): #Take the list as a parameter

    #Create a local variable to record number of steps
    steps = 0

    #Sort the list as many times as their are items in the list- Overkill
    for j in range(0, len(n)-1):

        #Iterate through every item in the list
        for i in range(0, len(n)-1):

            #Check if the current list item is greater than the next list item
            if n[i] > n[i+1]:

                #Swap their values
                n[i], n[i+1] = n[i+1], n[i]

            #Add a step
            steps += 1

    #Print the sorted list
    print(n)

    #Print the number of steps
    print(str(steps) + " steps to complete.")

#Run the function
bubble_sort(numbers)

print("--------------------------------------------")
print("QUICK SORT")
#Generate a list of five random numbers
numbers = [random.randint(0,101),random.randint(0,101),random.randint(0,101),random.randint(0,101),random.randint(0,101),random.randint(0,101),random.randint(0,101),random.randint(0,101),random.randint(0,101),random.randint(0,101),random.randint(0,101),random.randint(0,101)]
print(numbers)
def quicksort(arr):
    if len(arr) <= 1:
        return arr
    else:
        pivot = arr[0]
        less_than_pivot = [x for x in arr[1:] if x <= pivot]
        greater_than_pivot = [x for x in arr[1:] if x > pivot]
        return quicksort(less_than_pivot) + [pivot] + quicksort(greater_than_pivot)
    
print(quicksort(numbers))


    
        
    




# Task 1
def find_first_negative(lst):
    y = 0 # Initialize the while counter
    while (y < len(lst)): # Set the count according to the length of the list
        if  lst[y] < 0: # Check each number in the list if it is negative
            return print (f"First negative number found in {lst} is  {lst[y]}") # Negative found
        else:
            y += 1
    return print (f"No negatives found in {lst}") # No negative found



# Task 2
# Invoke the function "find_first_negative" using the following scenario:
# - [3, 5, -1, 7, -2, 8]
# - [2, 10, 7, 0]
find_first_negative([3, 5, -1, 7, -2, 8]) # Expected result -1
find_first_negative([2, 10, 7, 0]) # Expected result No negatives found
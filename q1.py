# Task 1
def swap(x, y):
    if type (x) == str or type (y) == str: #checking if variable "x" or "y" is of "string" variable type
        return print (-1) # if any of "x" or "y" is "string", return -1
    else:
        print ("Before swapping, x=" + str(x), "and y=" + str(y))
        x = x + y # swapping by adding two variables together and flushing out old value of "y" and "x" with new values
        y = x - y
        x = x - y
        print ("After swapping, x=" + str(x), "and y=" + str(y))

# Task 2
swap ("Apple", 10) # Invoking swap function with a string "apple" and number "10", expected outcome "-1"
swap (9, 17) # Invoking swap function with two numbers "9" and "17", expected outcome "17 9"




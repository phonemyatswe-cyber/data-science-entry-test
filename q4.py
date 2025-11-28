
# Task 1
def string_reverse(original_string):

    if type (original_string) != str: #Checking if the original string is "string" type
        return -1

    else:
        a = len(original_string) - 1 #First index is "0", need to reduce the end index by 1 from total length
        reversed_string = "" #Initialize the reversed_string
        for i in original_string:
            reversed_string += original_string[a] #Slice from the end index of original_string and add to reversed_string
            a -= 1 #Index decreasement towards "0" to the start of original_string
        print("Original String : " + original_string)
        print("Reversed String : " + reversed_string)
        return reversed_string


# Task 2
# Invoke the function "string_reverse" using the following scenarios:
# - "Hello World"
# - "Python"
string_reverse("Hello World")
string_reverse("Python")




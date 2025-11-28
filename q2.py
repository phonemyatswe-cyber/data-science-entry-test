# Task 1
def find_and_replace(lst, find_val, replace_val):
    if type (lst) != list: # Checking if the "lst" argument is "list" type
        print ("It's not a list")
        return -1
    else:
        print ("Original list: " + str(lst))
        new_lst = [] # Initializing new list
        for x in lst:
            if x == find_val: #Checking each item in the "lst" list if equal to "2"
                new_lst.append(replace_val) #Replace all "2" with "5"
            else:
                new_lst.append(x) #Append original value if not "2" to new_lst
        print ( "Replaced '" + str (find_val) + "' with '" + str (replace_val) + "' :" + str (new_lst))

    return new_lst
# Task 2
# Invoke the function "find_and_replace" using the following scenarios:

find_and_replace([1, 2, 3, 4, 2, 2], 2, 5) #Expected result [1, 5, 3, 4, 5, 5]
find_and_replace(["apple", "banana", "apple"], "apple", "orange") #Expected result ['orange', 'banana', 'orange']


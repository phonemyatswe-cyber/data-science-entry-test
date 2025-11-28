def update_dictionary(dct, key, value):

 #   Task 1

    if key in dct: #Checking if "key" exists in "dct"
        print ("Existing key '" + key + "' is in dct, original value : " + str (dct[key])) # Original key - value
        dct[key] = value # Update new value to the key
        print("New value of '" + key + "' is : " + str(dct[key])) # Print new value of the key
        return dct
    else:
        dct[key] = value # Add new key - value pair to dictionary
        print("New entry '" + key + "': " + str(dct[key])) # Print new entry key - value pair
        return dct


# Task 2
# Invoke the function "update_dictionary" using the following scenarios:
# - {}, "name", "Alice"
# - {"age": 25}, "age", 26

update_dictionary ({}, "name", "Alice") # Expected result: New entry 'name': Alice
update_dictionary ({"age": 25}, "age", 26) # Existing key 'age' is in dct, original value : 25  New value of 'age' is : 26
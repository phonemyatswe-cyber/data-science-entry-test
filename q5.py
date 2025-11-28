
# Task 1
def check_divisibility(num, divisor):
    if type (num) == str or type (divisor) == str: # Checking if the Dividend or Divisor is numeric
        return print ("Divisor or Dividend is invalid ")
    elif (num % divisor) == 0: # Checking if dividend is divisible by divisor by using modulus function
         print (str ((num % divisor) == 0) + "\n" + str (num) + " is divisible by " + str(divisor)+ "\n")# True if divisible
    else:
        print (str ((num % divisor) == 0) + "\n" + str (num) + " is not divisible by " + str(divisor)+ "\n")# False if not divisible
    return

# Task 2
# Invoke the function "check_divisibility" using the following scenarios:
# - 10, 2
# - 7, 3

check_divisibility(10, 2) #Expected output: True, Divisible
check_divisibility(7, 3) #Expected output: False, Not Divisible
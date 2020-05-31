# Component 1C: Check for integers, decimals and strings (with variations)

# To do
# Add testing for float variations: integers hidden in floats (34.0), decimal numbers (45.78) and out of range values
# Add testing for in-range values, between specified low and high
# Develop component into Part D: turn into a function, with low and high values specified with each time the function
#       is called for use in all three inputs at the beginning of the program
# Remove unnecessary 'valid = False' statements where it is the pre-existing condition - no need to redeclare it

low = 0.01
high = 1000000

valid = False
while not valid:
    user_input = input("Enter a keyword or the number of items you wish to proceed with: ")
    try:
        val = int(user_input)
        if val <= high:
            print("Input is an integer. You entered {}".format(val))
            valid = True
        else:
            print("You input is too high (has to be equal or less than $1,000,000) - Try again\n")
    except ValueError:
        try:
            val = float(user_input)
            if low > val:
                print("You input is too low (has to be equal or more than $0.01) - Try again\n")
            else:
                if int(val) == float(val):
                    print("Your input is an integer disguised as a decimal.")
                    valid = True
                else:
                    print("Input is a decimal. You entered {} - Please try again.\n".format(val))
        except ValueError:
            print("Input is a string. Each letter will be recorded as a separate item. ")
            valid = True

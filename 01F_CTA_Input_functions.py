# Component 1F: Abbreviate function and make efficient

# To do
# Create a function for each type of input/checking conditions


def num_check(statement):
    valid = False
    while not valid:
        user_input = input(statement)
        try:
            # try converting to a decimal number
            item = float(user_input)
            # if the remainder (modulo) when dividing by 1 is equal to zero it is an integer number (int type)
            if item % 1 == 0:
                print("You entered: {} - this will be processed as a number of items".format(user_input))
                valid = True
            # if the modulo 1 value of the user_input is not 0, it's a decimal (float type)
            else:
                print("You did not enter a valid value (integer/key word).\n")
        # If there's an error converting to numeric values (float and int), then it's a series of letters/number (str)
        except ValueError:
            print("You entered {} - each character will be processed as an individual item".format(user_input))
            valid = True


# Main routine
num_check("Please enter a number of items/key letters and push <enter>")
str_check()

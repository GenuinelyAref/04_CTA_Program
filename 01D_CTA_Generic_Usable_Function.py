# Component 1D: Turn complex input checker into a function, with low and high being parameters when calling function


def type_check(statement, low, high):
    valid = False
    while not valid:
        user_input = input(statement)
        try:
            val = int(user_input)
            if val <= high:
                print("Input is an integer. You entered {}".format(val))
                valid = True
            else:
                print("You input is too high (has to be equal to or less than {}) - Try again\n".format(high))
        except ValueError:
            try:
                val = float(user_input)
                if low > val:
                    print("You input is too low (has to be equal to or more than {}) - Try again\n".format(low))
                else:
                    if int(val) == float(val):
                        print("Your input is an integer disguised as a decimal.")
                        valid = True
                    else:
                        print("Input is a decimal. You entered {} - Please try again.\n".format(val))
            except ValueError:
                print("Input is a string. Each letter will be recorded as a separate item. ")
                valid = True


user_input = type_check("Enter a keyword or the number of items you wish to proceed with: ", 1, 1000000)

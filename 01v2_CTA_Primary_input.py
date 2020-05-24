# Component 1v2: All inputs

low = 0.01
high = 1000000

valid = False
while not valid:
    user_input = input("Enter a keyword or the number of items you wish to proceed with: ")
    try:
        val = int(user_input)
        if low <= val <= high:
            print("Input is an integer. You entered {}".format(val))
            valid = True
        else:
            print("You input is out of the permitted range ($0.01 to $1,000,000)\nTry again: ")
    except ValueError:
        try:
            val = float(user_input)
            if int(val) == float(val):
                print("Your input is an integer disguised as a decimal.")
                valid = True
            else:
                print("Input is a decimal. You entered {} - Please try again.\n".format(val))
                valid = False
        except ValueError:
            print("Input is a string. Each letter will be recorded as a separate item. ")
            valid = True

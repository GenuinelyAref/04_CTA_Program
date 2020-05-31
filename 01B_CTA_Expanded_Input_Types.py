# Component 1B: Input type (simple - expanded)

# To do
# Trialling...
# Expand try/except loop by nesting one inside another

user_input = input("Enter a keyword or the number of items you wish to proceed with: ")
try:
    val = int(user_input)
    print("Input is an integer. You entered {}".format(val))
except ValueError:
    try:
        val = float(user_input)
        print("Input is a float. You entered {}".format(val))
    except ValueError:
        print("Input is a string")

# Component 1E: Input checking with individual functions

# To do
# Create a function for each type of input/checking conditions


# Check for numeric/input
def basic_type_check(statement):
    value = input(statement)
    try:
        num = float(value)
        print("It's a number")
        if num == int("{:.0f}".format(num)):
            print("It's an integer")
        else:
            print("It's a decimal")
    except ValueError:
        try:
            float(value)
            print("\n\nIt's a decimal")
        except ValueError:
            print("It's not a decimal")
        print("It's a string")


# Main routine
user_input = basic_type_check("Enter something: ")

# Component 1: Input type

# To do
# Get input
# Copy input (to avoid altering the main value)
# Determine input type using ValueError True/False status

# Get user input
user_input = input("Enter a keyword or the number of items you wish to proceed with: ")

try:
    # Copy 'user_input' to 'val'
    val = int(user_input)
    # If ValueError = False, then 'val' is int type
    print("Input is a number")
except ValueError:
    # If ValueError = True, then 'val' is not int type
    print("Input is a string")

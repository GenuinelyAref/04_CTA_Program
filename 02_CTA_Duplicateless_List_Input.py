# Component 2: NO duplicates in input

# To do
# Take input (manually insert for testing)
# Check for present copies of letter/value before inserting
# Ensure that all letters (values) in the list are unique - no duplicates at all

user_input = list(input("Enter a series of letters (word) with repeated letters: "))

values = []
for i in range(1, len(user_input)+1):
    item = user_input[0]
    if item not in values:
        values.append(item)
    del user_input[0]
print(values)

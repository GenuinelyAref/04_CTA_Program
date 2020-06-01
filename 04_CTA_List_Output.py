# Component 4: Repeat list generation for number of trials

# To do
# Loop list generation

import random

# Manually insert letters of word
letters = ['a', 'r', 'e', 'f']
TRIALS = 20

for something in range(1, TRIALS+1):
    # Define lists
    indexes = []
    random_list = []
    random_indexes = []

    # Copy item values (index value in list + 1) to a new list called indexes
    for item in range(1, len(letters)+1):
        indexes.append(item)

    # Keep generating random numbers from the indexes list until all numbers are present at least once
    while not all(i in random_indexes for i in range(1, len(letters)+1)):
        # Choose random value in the indexes list
        num = random.choice(indexes)
        # Add the corresponding item (letter) with that item number (index # + 1) to the output list
        random_list.append(letters[num-1])
        # Add value to another list, which will be used to tell when there is at least one of every item (letter/number)
        random_indexes.append(num)
    length = len(random_list)
    number = 120-(length*5)
    print("{}{}==> Length = {}".format(random_list, " "*number, length))

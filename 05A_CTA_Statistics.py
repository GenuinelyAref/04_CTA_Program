# Component 3: Take statistics from printed lists

# To do
# Add cost of purchase next to each printed list
# Take min/max values
# Find average list length
# Give user summary stats, min/max/avg items, with cost values

import random

# Manually insert letters of word
letters = ['a', 'r', 'e', 'f']
TRIALS = 20
length = 0
MAX = 0
MIN = len(letters)+10
cost = 3
total = 0

for something in range(1, TRIALS+1):
    # Define lists & variables
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
    total += length
    # Min/Max statistics
    if length > MAX:
        MAX = length
    elif length < MIN:
        MIN = length

    number = 80-(length*5)
    print("{}{}==> Length = {}".format(random_list, " "*number, length))
avg_length = float("{:.2f}".format(total/TRIALS))
print("Maximum length: {}\nMinimum length: {}\nMaximum cost: ${}\nMinimum cost: ${}\nAverage length: {}"
      "\nAverage cost: ${:.2f}\nTotal items: {}\nTotal cost: ${}"
      .format(MAX, MIN, MAX*cost, MIN*cost, avg_length, avg_length*cost, total, total*TRIALS))

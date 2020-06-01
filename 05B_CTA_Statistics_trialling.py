# Component 5: Trial different method for collecting statistics

# To do
# Trial :)))

import random

# Manually insert letters of word
letters = ['a', 'r', 'e', 'f']
TRIALS = 20
single_cost = 3
total_cost = 0
results = []

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
    results.append(length)
    cost = length*single_cost
    total_cost += cost
    number = 120-(length*5)
    print("{}{}  {} items = ${}".format(random_list, " "*number, length, cost))
results.sort()
average = int("{:.0f}".format(sum(results)/TRIALS))
MIN = results[0]
MAX = results[-1]
print("\nTotal cost: ${:.2f}\n".format(total_cost))
print("Average: {} items = ${:.2f}\nAverage savings/discount: {:.2f}%\n"
      .format(average, average*single_cost, 100/(average+1),))
print("Minimum: {} items = ${:.2f}\nMinimum savings/discount: {:.2f}%\n\nMaximum: {} items = ${:.2f}\nMaximum "
      "savings/discount: {:.2f}%".format(MIN, MIN*single_cost, 100/(MIN+1), MAX, MAX*single_cost, 100/(MAX+1)))

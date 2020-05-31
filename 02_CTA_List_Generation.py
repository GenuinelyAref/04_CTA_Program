# Component 2: Generate List of tokens

# To do
# Generate a random token from a provided list repeatedly until 1 of each item has been generated

import random
list1 = []

letters = ['b', 'i', 'o', 'l', 'o', 'g',' y']


item = 0
try:
    random_num = random.randint(0, 6)
    token = letters[random_num]
    list1.index(letters[item])
    item += 1
except ValueError:
    list1.append(letters[random_num])
print(list1)
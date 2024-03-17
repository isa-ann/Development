''' Lists '''


# Indexing
planets = ['mercury', 'venus', 'earth', 'mars', 'jupiter']


# Update with indexing
colors = ['red', 'green', 'yellow', 'blue', 'orange']



# Iterate with for loop
animals = ['dog', 'cat', 'lion', 'tiger', 'eagle']



# Len function gives us the amount of items in a list
modes_of_travel = ['car', 'plane', 'truck', 'train', 'boat']


'''
Exercise

Create a for loop that goes through a list and prints each item in the list, along with its index. (Hint: Create a separate counter variable to keep track of the index.)

Example:
planets = ["mercury", "venus", "earth", "mars"]
0: mercury, 1: venus, 2: earth, 3: mars

'''
# planets = ["mercury", "venus", "earth", "mars"] # define the list of planets
# index = 0  # initialize the variable called index o keep track of the index as we iterate through the list

# for planet in planets:
#     print(f"{index}: {planet}", end=" ")
#     index += 1


# planets = ["mercury", "venus", "earth", "mars"]
# index = 0

# for planet in planets:
#     print(f"{index}: {planet}", end=", ")
#     index += 1
# # 
# Output: 0: mercury, 1: venus, 2: earth, 3: mars,
# planets = ["mercury", "venus", "earth", "mars"]
# counter = 0

# for p in planets:
#     print(f"{counter}: {p}", end=", ")
#     counter += 1

# Output: 0: mercury, 1: venus, 2: earth, 3: mars,



# Output: 0: mercury, 1: venus, 2: earth, 3: mars,





''' Exercise
Write some code that takes one list and creates a second list that has the type for each entry in the list. Hint: Use the type() function and a for loop

Optional:
Make sure you filter out any repeats.

data = ['car', 3, True, False, 4.09, 'Tuesday']

'''



# data = ['car', 3, True, False, 4.09, 'Tuesday']
# types_list = [] # This list will hold our types

# for d in data:
#     # print(d)
#     # print(type(d))
#     item_type = type(item)
#     if item_type not in types_list:
#         types_list.append(item_type) # grabbing the types from data, appending to empty list

# print("Our Types List which contains duplicates", types_list)


# data = ['car', 3, True, False, 4.09, 'Tuesday']
# types_list = []

# for d in data:
#     item_type = type(d)
#     if item_type not in types_list:
#         types_list.append(item_type)

# print("Our Types List which contains duplicates", types_list)


# Our collections


# Looping through for types



# Optional, remove repeats using sets
# data = ['car', 3, True, False, 4.09, 'Tuesday']
# types_set = set()

# for item in data:
#     types_set.add(type(item))

# print(types_set)


''' List Methods '''

'''
append() Adds an element at the end of the list
clear() Removes all the elements from the list
copy() Returns a copy of the list
count() Returns the number of elements with the specified value
extend() Add the elements of a list (or any iterable), to the end of the current list
index() Returns the index of the first element with the specified value
insert() Adds an element at the specified position
pop() Removes the element at the specified position
remove() Removes the first item with the specified value
reverse() Reverses the order of the list
sort() Sorts the list

'''

# food = ['ice cream', 'pizza', 'apple', 'burger', 'cookies']

# lets add salad with append



# lets remove all items with clear



# let create a copy


# How many times does pizza appear?


# Lets add items of a list to our food list, extend method
# vegetables = ['carrots', 'asparagus', 'broccoli']


# lets find the index value for apple

# Lets add cereal to the 3rd spot in our list


# Lets remove a food by index position
#

# Lets remove an item with a specified value


# Lets reverse our list



# Lets sort our list


# Sort versus sorted()

# Sorted returns a newer sorted list
##########################################################
# Original list
food = ['ice cream', 'pizza', 'apple', 'burger', 'cookies']

# Add salad with append
food.append('salad')

# Remove all items with clear
food.clear()

# Create a copy
food_copy = food.copy()

# Add items of a list to our food list
vegetables = ['carrots', 'asparagus', 'broccoli']
food.extend(vegetables)

# How many times does pizza appear?
pizza_count = food.count('pizza')
print(pizza_count)

# Find the index value for apple
apple_index = food.index('apple')

# Add cereal to the 3rd spot in our list
food.insert(2, 'cereal')

# Remove a food by index position
food.pop(1)

# Remove an item with a specified value
food.remove('cookies')

# Reverse our list
food.reverse()

# Sort our list
food.sort()

# Sorted returns a newer sorted list
sorted_food = sorted(food)

# Printing results
print("Food list after operations:", food)
print("Copy of food list:", food_copy)
print("Number of times 'pizza' appears:", pizza_count)
print("Index of 'apple':", apple_index)
print("Sorted food list:", sorted_food)

########################################################################

'''
Exercise: List of Pets

You want to make a list containing the types of pets that the user has. Keep prompting the user for a pet until they enter "stop". If it's a new pet, add it to the list. If the list already has that pet, don't add it.

'''



''' Removing duplicates from a list, but leaving 1'''

colors = ['blue', 'blue', 'blue', 'green', 'red', 'blue', 'blue']

# Option 1 


# Option 2 - Using Sets




'''
Example: Removing Values
You have a list of numbers, but it contains multiple of the number 2. Remove the number 2 until it only appears in the list once.

num_values = [2, 3, 4, 3, 2, 2, 2, 4, 1, 3, 4, 5]
'''
num_values = [2, 3, 4, 3, 2, 2, 2, 4, 1, 3, 4, 5, 2, 2, 2, 2] # removes an item based on its value. If there are multiple, it removes the first item with that value.


# Option 1


# Option 2





'''
You have a list storing important data for your company, but it contains some duplicate entries. Go through your list and remove all the duplicates. When you're done, each item should appear in the list exactly once.
Hint: How would you expand our previous example, which removed duplicates of one value, to remove duplicates of all values?
Hint 2: You might want to make a copy of the original list to use as reference. You may want to use more than one loop.

transaction_dates = []
'''

transaction_dates = ['3/5/2024', '3/5/2024', '5/4/2019', '2/23/2023', '5/4/2019','5/2/2023', '2/23/2023', '2/23/2024', '8/6/2019', '5/4/2019','3/5/2024','5/2/2023']




# Using sets


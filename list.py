"""
lists are single dimensional arrays that can hold multiple values
lists are mutable, meaning their values can be changed after creation
lists can hold values of different data types
lists are defined using square brackets [].

"""

# Example of creating a li
my_list = [1, 2, 3, "four", "five", 6.0]

# Accessing elements in a list
first_element = my_list[0]  # Accessing the first element
last_element = my_list[-1]  # Accessing the last element

# Modifying elements in a list
my_list[1] = "two"  # Changing the second element

# Adding elements to a list
my_list.append(7)  # Adding an element at the end
my_list.insert(0, 0)  # Adding an element at the beginning

# Removing elements from a list
my_list.remove("four")  # Removing a specific element
popped_element = my_list.pop()  # Removing the last element

# Slicing a list
sub_list = my_list[1:4]  # Getting a sub-list from index

# Iterating through a list
for item in my_list:
    print(item)

# Getting the length of a list
list_length = len(my_list)
print("Length of the list:", list_length)

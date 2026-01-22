#! /usr/bin/python3
import sys

sys.version_info[0]

lab_exercise = "Tuples"
lab_type = "lab-code"
python_version = "%s.%s.%s" % (
    sys.version_info[0],
    sys.version_info[1],
    sys.version_info[2],
)
print("Exercise: %s" % (lab_exercise))
print("Type: %s" % (lab_type))
print("Python: %s\n" % (python_version))

# ====================================

# CODE1: Create an empty TUPLE
empty_tuple = ()
print(empty_tuple)
print()

# CODE2: Create TUPLE with 1 item
tuple_1 = "Greetings"
print(tuple_1)
print()

# CODE3: Create TUPLE with multiple items of the same type
tuple_2 = (1, 2, 3, 4)
print(tuple_2)
print()

# CODE4: Create TUPLE with multiple items of different types
tuple_3 = (1, 2.0, "Soccer")
print(tuple_3)
print()

# CODE5: Iterate over TUPLE with multiple items
for item in tuple_3:
    print(item)
print()

# CODE6: Search in TUPLE
print(1 in tuple_3)
print(3 in tuple_2)
print()

# CODE7: Retrieve item from TUPLE
item_1 = tuple_2[0]
print(item_1)

item_2 = tuple_3[1]
print(item_2)
print()

# CODE8: Attempt to change immutable TUPLE
try:
    tuple_3[2] = "Football"
except TypeError:
    print("Tuples are immutable!!")
print()

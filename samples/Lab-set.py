#!/usr/bin/python3
import sys

lab_exercise = "Sets"
lab_type = "lab-code"
python_version = "%s.%s.%s" % (
    sys.version_info[0],
    sys.version_info[1],
    sys.version_info[2],
)

print("Exercise: %s" % lab_exercise)
print("Type: %s" % lab_type)
print("Python: %s\n" % python_version)

# ====================================

# CODE1: Create an empty SET
set_1 = set()
print(set_1)
print(f"Data type: {type(set_1)}")
print(f"Length: {len(set_1)}")
print()

# CODE2: Create SET with 1 item
set_2 = set("Charleston")
print(set_2)
print(f"Length: {len(set_2)}")
print(f"Data type: {type(set_2)}")
print()

# CODE3: Create SET with multiple items of the same type
set_3 = {11, 12, 13, 14, 15}
print(set_3)
print(f"Data type: {type(set_3)}")
print(f"Length: {len(set_3)}")
print()

# CODE4: Create SET with multiple items of different types
set_4 = {1, 2.0, "Cooking", True}
print(set_4)

# CODE5: Iterate over SET with multiple items
for item in set_4:
    print(item)
print()

# CODE6: Search in SET
print("Cooking" in set_4)
print(4 in set_4)
print()

# CODE7: Attempt to retrieve item from SET
try:
    item0 = set_4[0]
    item1 = set_4[1]
    print(f"item0 = {item0}")
    print(f"item1 = {item1}")
except TypeError:
    print("Sets do not support indexing!!")
print()

# CODE8: Add new unique item to SET
set_4.add("Baking")
print(set_4)
print()

# CODE9: Add new non-unique item to SET
set_4.add("Baking")
print(set_4)
print()

# CODE10: Remove item from SET
set_4.remove(1)
print(set_4)
print()

"""
Pythonic Programming Examples.
"""
import logging
import re

# Configure string format for consumption into logging platforms.
logging.basicConfig(
level=logging.DEBUG, format="%(asctime)-15s %(levelname)-8s %(message)s"
)

# Initialize
logger = logging.getLogger("python-template")

# Pythonic vs. Non-Pythonic code

# Non-Pythonic
logger.info("Non-Pythonic for loop")
numbers  = [1,2,3,4,5,6,7,8,9,10]

for i in range(0, len(numbers)):
    squared = numbers[i] * numbers[i]
    numbers[i] = squared

logger.info(numbers)

# Pythonic via "list comprehension"
# For each item in a list, perform a certain action (square it).
logger.info("Pythonic list comprehension")

numbers  = [1,2,3,4,5,6,7,8,9,10]
numbers = [x**2 for x in numbers]

logger.info(numbers)

logger.info("### Data Types ###")

# Tuples
# A collection of related data. Values are not all the same type. Indexed by integers.
# It is read-only and immutable. A "struct" or "record" in other languages.
# 
# To create, use a comma-separated list of objects.
# Parentheses are not required unless nested in a larger data structure.
#
# While tuples and lists can be used for any data
#   => Use a list when you have a collection of SIMILAR objects
#   => use a tuple when you have a collection of related objects, which may not be similar

logger.info("Tuples")

# Related strings and integers
person = ('bellanov', 'apilli', 40)

logger.info(person)
logger.info(type(person))

# Lists
# Lists vs Tuples => lists created with brackets [], tuples created with parentheses ()

logger.info("Lists")

cars = ['ford','toyota','ferrari']

logger.info(cars)
logger.info(type(cars))

# Dictionaries

logger.info("Dictionaries")

developer = {
    "name": "bellanov",
    "surname": "apilli",
    "age": "20"
}

logger.info(developer)
logger.info(type(developer))

# Data Types Summary
dataTuple = ('val1','val2')  # Immutable / Read-only, CANNOT reassign elements within a tuple
dataList = ['val1','val2']
dataDict = {
    "key1": "val1",
    "key2": "val2"
}

logger.info("### Iterable Unpacking: Lists / Tuples ###")

# When you have an iterable such as tuple or list, you can access individual elements by index.
# However, spam[0] and spam[1] are not readable compared to first_name and company.
#
# You may be thinking "why not just assign to the variables in the first place?". For a single
# tuple or list, this would be true.
# 
# The power of unpacking comes in the following areas:
#   => looping over a sequence of tuples
#   => passing tuples (or other iterables) into a function
#   => can have one wildcard

logger.info("Birthday")
birthday = ('April',5,1978)

# Unpack Tuple based on index / positioning. Use this as often as possible!@!
month, day, year = birthday

logger.info(month)
logger.info(day)
logger.info(year)

logger.info("People => List of Tuples")

people = [
    ('Melinda','Gates','Gates Foundation'),
    ('Steve','Jobs','Apple'),
    ('Larry','Wall','Perl'),
    ('Paul','Allen','Microsoft'),
    ('Larry','Ellison','Oracle'),
    ('Bill','Gates','Microsoft'),
    ('Mark','Zuckerberg','Facebook'),
    ('Sergey','Brin','Google'),
    ('Larry','Page','Google'),
    ('Linus','Torvalds','Linux'),
]

logger.info(people)
logger.info(type(people))
logger.info(type(people[0]))
logger.info(type(people[0][0]))

# Unpack tuples while iterating over a list of tuples...Pythonic
for first_name, last_name, org in people:
    print("{} {}".format(first_name, last_name))

logger.info("Unpacking Function Arguments")

# Sometimes you need the other end of iterable unpacking. What do you do if you have a list
# of three values, and you want to pass them to a method that expects three positional
# arguments? 
#
# One approach is to use the individual items by index. The more Pythonic approach is to use the *
# to unpack the iterable into individual items.
#
# Use a single asterisk (*) to unpack a list or tuple. Use two asterisks (**) to unpack a dictionary
# or similar.

people = [
    ('Joe','Schmoe','Burbank','CA'),
    ('Marry','Rattburger','Madison','WI'),
    ('Jose','Ramirez','Ames','IA')
]

def person_record(first_name, last_name, city, state):
    print("{} {} lives in {}, {}".format(first_name, last_name, city, state))

for person in people:
    # Unpack tuple at each index
    person_record(*person)

logger.info("### The sorted() function ###")

# The sorted() function returns a sorted copy of ANY collection.
# The sorted() function returns a sorted copy of its argument, which can be any iterable.
# You can customize the sorted with the "key" parameter, also "reverse".

fruit = ["pomegranate", "cherry", "apricot", "date", "Apple", "lemon", "Kiwi", "ORANGE",
         "lime", "Watermelon", "guava", "papaya", "FIG", "pear", "banana", "Tamarind",
         "persimmon", "elderberry", "peach", "BLUEberry", "lychee", "grape"]

logger.info("Fruit: {}".format(fruit))

sorted_fruit = sorted(fruit)

# Sorts uppercase words first then lower, doesn't ignore case
logger.info("Sorted Fruit: {}".format(sorted_fruit))

logger.info("### Custom Sort Keys ###")

# You can specify a function with the "key" parameter of the sorted() function. This function will
# be used once for each element of the list being sorted, to provide the comparison value.
# Thus, you can sort a list of strings case-insensitively, or sort a list of zip codes by the number
# of Starbucks within the zip code.
#
# The function must take exactly one parameter (which is one element of the sequence being sorted)
# and return either a single value or a tuple of values. The returned values will be compared in order.
#
# For the fruits example, the str.lower() method can be called, or you can define your own function, for
# the Starbucks within zip codes case, for instance.

# Function that takes EXACTLY one parameter, the element to be sorted at each index
def ignore_case(item):
    return item.lower()

sorted_fruit = sorted(fruit, key=ignore_case)
logger.info("Ignoring case!@!")
logger.info(" ".join(sorted_fruit))

logger.info("Sort by length, then name => tuple")

# Sort by multiple items, in the order defined within the tuple
def by_length_then_name(item):
    return (len(item), item.lower())

sorted_fruit = sorted(fruit, key=by_length_then_name)
logger.info("By length, then name!@!")
logger.info(" ".join(sorted_fruit))

# Numbers sorted numerically, automatically
nums = [800, 80, 1000, 32, 255, 400, 5, 5000]
sorted_nums = sorted(nums)
logger.info("Numbers sorted numerically!@!")

for num in sorted_nums:
    logger.info("{}".format(num))

sorted_nums = sorted(nums, key=str)
logger.info("Numbers sorted by string value!@!")

for num in sorted_nums:
    logger.info("{}".format(num))

logger.info("### Sort via Regular Expression ###")

# Specify a custom sort function that strips the element of unwanted string elements
#
# 1) compile regex to match leading articles
# 2) create function which takes element to compare and returns comparison key
# 3) strip off article and convert title to lowercase
# 4) sort using custom function

# Compile a regular expression to match preceding the, a, or an, ignoring case
rx_article = re.compile(r'^(the|a|an)\s+', re.I)    # re.I => ignore case

def strip_articles(title):
    # Substitute occurences matching the regex within the given string
    stripped_article = rx_article.sub('', title.lower())
    return stripped_article

books = [
    'The Adventures of Sherlock Holmes',
    'The Case-Book of Sherlock Holmes',
    'His Last Bow',
    'The Hound of the Baskervilles',
    'The Memoirs of Sherlock Holmes',
    'The Return of Sherlock Holmes',
    'The Sign of the Four',
    'A Study in Scarlet',
    'The Valley of Fear'
]

for book in sorted(books, key=strip_articles):
    logger.info(book)

logger.info("### Lambda Functions ###")

# A lambda function is a brief function definition that makes it easy to create a function on
# the fly. This can be useful for passing functions into other functions, to be called later.
# Functions passed in this way are referred to as "callbacks". Normal functions can be callbacks
# as well. The advantage of a lambda function is solely the programmer's convenience. There is no
# speed or other advantage.
#
# One IMPORTANT use of lambda function sif ro providing sort keys; another is to provide event handlers
# in GUI programming.
#
# The basic syntax for creating a lambda function is => lambda parameter-list: expression
# Where parameter-list is a list of function parameters, and expression is an expression involving the
# parameters. The expression is the return value of the function.
#
# A lambda function could also be defined in the normal manner
#
#   def function-name(param-list):
#       return expr
#
# But it is not possible to use the normal syntax as a function parameter, or as an element in a list.

addFive = lambda x : x + 5

logger.info(addFive(2))
logger.info(addFive(100))

addTwoNums = lambda x,y : x + y
logger.info(addTwoNums(20,40))
logger.info(addTwoNums(10,20))

# The power of lambda functions is passing functions to other functions.
printResult = lambda func, val: func(val)

logger.info(printResult(addFive, 20))

# Using lambdas in accordance with the sorted function. Prevents us from having to officially define
# a custom function.

logger.info(fruit)

# Sort via lambda function, good for one-liners it seems. Very concise.
sorted_fruit = sorted(fruit, key=lambda e: e.lower())

logger.info(sorted_fruit)

logger.info("### List Comprehension ###")

# A list comprehension is a Python idiom that creates a shortcut for a for loop. It returns a copy of
# a list with every element transformed via an expression, also referred to as a "mapping function".
#
# A loop like this:
#
#   results = []
#   for var in sequence:
#       results.append(expr) # where expr involves var
#
# can be rewritten as
#
#   results = [expr for var in sequence]
#
#   A conditional may be added to filter values:
#
#   results = [expr for var in sequence if expr]

numbers = [1,2,3,4,5,6,7,8,9,10]

# Square all numbers within a list
squared = [x**2 for x in numbers]
logger.info("Squared Numbers: {}".format(squared))

# First 20 even numbers
evens = [x * 2 for x in range(1,20)]
logger.info("First 20 even numbers: {}".format(evens))

# A very constructive way to construct lists dynamically using very little code!@!

# Capitalize elements of a list
fruits = ['watermelon', 'apple', 'mango', 'kiwi', 'apricot', 'lemon', 'guava']

ufruits = [fruit.upper() for fruit in fruits]
logger.info("Uppercase Fruits: {}".format(ufruits))

# Different elements within a list
values = [2, 42, 18, 92, "boom", ['a', 'b', 'c']]
logger.info(values)

doubles = [value * 2 for value in values]
logger.info(doubles)

double_integers = [v * 2 for v in values if (type(v) == int)]
logger.info(double_integers)

logger.info("### Dictionary Comprehension ###")

# A dictionary comprehension has syntax similar to a list comprehension. The expression is a
# key:value pair, and is added to the resulting dictionary. If a key is used more than once,
# it overrides any previous keys. 
#
# This can be handy for building a dictionary from a sequence of values. Transform an interable
# into a dictionary.
#
# Uses curly braces {} instead of brackets [].

# Convert a list of animals into a dictionary
animals = ['OWL', 'badger', 'bushbaby', 'Tiger', 'Wombad', 'GORILLA', 'AARDVARK']
logger.info("Animals : {}".format(animals))

comprehensiond = {animal.lower(): len(animal) for animal in animals}
logger.info("D Comprehension: {}".format(comprehensiond))

logger.info("### Set Comprehension ###")

# A set comprehension is useful for turning any sequence into a set. Items can be skipped or modified
# as the set is being built.
#
# If you don't need to modify the items, it's probably easier to just pass the sequence to the set()
# constructor.
#
# It uses curly braces {} without being a key:value pair.
#
# A set is a unique list of values, no repetition allowed.

# Get unique words from a file containing "Mary had a Little Lamb"
with open("./data/mary.txt") as mary_in:
    # \W+ matches one or more non-alphanumeric characters. Split output based on these occurences.
    set_comp = {w.lower() for ln in mary_in for w in re.split(r'\W+', ln) if w}     

logger.info(set_comp)

logger.info("### Iterables ###")

# Iterables are:
#
#   => expressions that can be looped over
#   => can be collections (e.g list, tuple, str, bytes)
#   => can be generates (e.g range(), file objects, enumerate(), zip(), reversed())
#
# Python has many build-in iterables (i.e., file object to allow iterating through the lines of a file).
#
# All builtin collections (list, tuple, str, bytes) are iterables. They keep ALL of their values in
# memory. Many other builtin iterables are generators.
#
# A generator does not keep all its values in memory -- it creates them one at a time as needed, and
# feeds them into the for-in loop. This is a good thing, because it saves memory.
#
# Iterables can be grouped into two categories, Collections and Generators.
#
# Collections are stored in memory and considered "eager", which means everything is available all at once
# in memory.
#
# Generators are considered virtual and "lazy", meaning the data that is generated is not stored in memory,
# and is only available when requested.

logger.info("### Generator Expressions ###")

# A generator expression is similar to a list comprehension, but it provides a generator instead of a list.
# That is, while a list comprehension returns a complete list, the generator expression returns ONE item at
# a time.
#
# The main difference in syntax is that the generator expression uses parentheses () rather than brackets [].
#
# Genrator expressions are especially useful with functions like sum(), min(), and max(), that reduce an
# iterable input to a single value!@! (lol map reduce?)

# List Comprehension vs Generator Expression

# sum the squares of a list of numbers
# using a list comprehension, entire list is stored in memory
s1 = sum([x * x for x in range(20)])

# only one square is in memory at a time with a generator expression
s2 = sum(x * x for x in range(20))

logger.info("S1: {}".format(s1))
logger.info("S2: {}".format(s2))

# More memory-efficient to use generators
#
# 1. using list comprehension, entire list is stored in memory
# 2. with generator expression, only one square is in memory at a time
# 3. only one line in memory at a time. max() iterates over generated values

# Generator file processing example
# Open file, loop through it line by line, reading one line into memory at a time
page = open("./data/mary.txt")
m = max(len(line) for line in page)
page.close()
logger.info("Max: {}".format(m))

logger.info("### Generator Functions ###")

# Generator Functions
#
#   => mostly like a normal function
#   => uses yield rather than return
#   => Maintains state
#
# A generator is like a normal function, but instead of a return statement, it has a "yield" statement.
# Each time the yield statement is reached, it provides the next value in the sequence. When there are
# no more values, the function calls return, and the loop stops.
#
# A generator function maintains state between calls, unlike a normal function.

# Yield multiple values at varying points of the function. The function will seemingly keep being iterated
# so long as there is a yield to process.
#
# State is maintained as you generate / yield values from the function.
def numbers():
    a = 0
    for i in range(3):
        yield a
        a = a + 1
    for i in range(3):
        yield a
        a = a - 1
    yield 100
    yield 200
    yield 300

for num in numbers():
    logger.info(num)

# Using a generator function to calculate all of the prime numbers up until a certain limit, yielding one
# value at a time.
    
logger.info("Prime Numbers:")

def next_prime(limit):
    flags = set()

    for i in range(2, limit):
        if i in flags:
            continue
        for j in range(2*i, limit + 1, i):
            flags.add(j)
        yield i

# Not pre-loading all of the prime numbers and storing them in memory all at once!@!
for prime in next_prime(2000):
    logger.info(prime)

logger.info("File Input Generator Function")

# Use a generator function to yield one line of strings at a time
# 1. 'yield' causes this function to return a generator object
# 2. looping over the generator object returned by trimmed
def trimmed(file_name):
    with open(file_name) as file_in:
        for line in file_in:
            if line.endswith('\n'):
                line = line.rstrip('\n\r')
            yield line

for trimmed_line in trimmed('./data/mary.txt'):
    logger.info(trimmed_line)

logger.info("### String Formatting ###")

# String formatting:
#
#   => Numbered placeholders
#   => Add width, padding
#   => Access elements of sequences and dictionaries
#   => Access object attributes
#
# The traditional way to format strings in Python was the % operator and a format string containing fields
# designated with percent signs. 
#
# The new improved way uses the format() method, which takes a format string and one or more arguments.
# Placeholders consist of curly braces {}, which may contain formatting details. This new method has much
# more flexibility.
#
# By default, the placeholders are numbered from left to right, starting at 0. This corresponds to the order
# of the arguments to format().
#
# Formatting information can be added, preceded by a colon
#
#   {:d}    format the argument as an integer +
#   {:03d}  format as an integer, 3 columns wide, zero padded +
#   {:>25s} same but right-justified
#   {:.3f}  format as a float, with 3 decimal places
#
# Placeholders can be manually numbered. This is handy when you want to use a format() parameter more than
# once.

# Numbered placeholders
logger.info("Try one of these: {0}.jpg {0}.png {0}.bmp {0}.pdf".format('penguin'))

# Curly braces
color = 'blue'
animal = 'iguana'
logger.info("{} {}".format(color, animal))

# Float, with 1 decimal place
fahr = 98.4735633
logger.info('{:.1f}'.format(fahr))

# Display same value in decimal, hexidecimal, octal, and binary formats
value = 12345
logger.info("{0:d} {0:04x} {0:08o} {0:016b}".format(value))

data = {"A": 38, "B" : 127, "C": 9}

# Provides a set-like object providing a view into the Dictionary
# Represents the items as tuples that can be unpacked
logger.info(data.items())

for letter, number in sorted(data.items()):
    # Decimal 4 characters wide, padded
    logger.info("{} {:4d}".format(letter, number))

logger.info("### f-strings ###")

# f-strings
#  
#   => shorter syntax for string formatting
#   => Only available in Python 3.6 and later
#   => Put f in front of string
#
# These are strings that contain placeholders, as used with normal string formatting, but the
# expression to be formatted is also placed within the placeholder. This makes formatting more
# readable, with less typing.
#
# As with formatted strings, any expression can be formatted.
# Other than puttin gthe value to be formatted directly in the placeholder, the formatting
# directives are the same as normal Python 3 string formatting.

# Normal 3.x formatting
x = 24
y = 32.2345
name = "Bill Gates"
company = "Microsoft"
logger.info("{} founded {}".format(name, company))
logger.info("{:.2f} {:.2f}".format(x, y))

# f-strings let you do this simpler and more concisely
# Lets you inject the variable directly into the string itself.
logger.info(f"{name} founded {company}")
logger.info(f"{x:.2f} {y:.2f}")

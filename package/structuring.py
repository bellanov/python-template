"""
Pythonic Programming Examples.

Functions, Modules, and Packages.
"""
import logging

# Configure string format for consumption into logging platforms.
logging.basicConfig(
level=logging.DEBUG, format="%(asctime)-15s %(levelname)-8s %(message)s"
)

# Initialize
logger = logging.getLogger("python-template") 

logger.info("### Functions ###")

# Functions
#
#   => defined with def
#   => Accept parameters
#   => Return a value
#
# Functions are a way of isolating code that is needed in more than one place, refactoring code
# to make it more modular. They are defined with the def statement.
#
# Functions can take various types of parameters. Parameter types are dynamic.
# 
# Functions can return one object of any type, using the return statement. If there is no return statement,
# the function returns None.

def say_hello():
    logger.info("Hello, world")

# A return value of None is returned
h = say_hello()
say_hello()

# NoneType because the function returns None, or has no return values
logger.info(type(h))

def get_hello():
    return "Hello, world!!!"

hello = get_hello()
logger.info(hello)

# Type is string due to the function returning a string
logger.info(type(hello))

# Square root a number
def sqrt(num):
    return num ** .5

m = sqrt(1234)
n = sqrt(2)

logger.info(m)
logger.info(n)

# Formatting returned values from functions
logger.info("m is {:.3f}, n is {:.3f}".format(m, n))

logger.info("### Functions Parameters ###")

# Function Parameters
#
#   => positional or named
#   => required or optional
#   => can have default values
#
# Functions can accept both positional and named parameters. Furthermore, parameters can be required or
# optional. They must be specified in the order presented here.
#
# The first set of parameters, if any, is a set of comma-separated names. These are all REQUIRED. Next,
# you can specify a variable preceded by an asterisk (*) -- this will accept any optional parameters.
#
# After the optional positional parameters, you can specify required named parameters. These MUST come
# after the optional parameters. If there are no optional parameters, you can use a plain asterisk as 
# a placeholder. Finally, you can specify a variable preceded by two asterisks (**) to accept optional
# named parameters.
#
# Positional vs. Named Parameters
#
#   def func(p1,p2,*p3,p4,p5,**p6)
#       pass
#
#   p1, p2 => required, positional parameters
#   *p3 => optional
#   p4, p5 => required named parameters, keyword-only
#   **p6 => optional named parameters

# No function parameters
def fun_one():
    logger.info("Hello World")

logger.info("fun_one()")
fun_one()

# One function parameter
def fun_two(n):
    return n ** 2

x = fun_two(5)
logger.info("fun_two(5) is {}".format(x))

# Function parameter with default value
def fun_three(count=3):
    for _ in range(count):
        logger.info("Spam")

# Consumes the default value
fun_three()

# Overwrites the default value
fun_three(9)

# One fixed, positional parameter with one optional parameter
def fun_four(n, *opt):
    logger.info("fun_four():")
    logger.info("n is {}".format(n))
    logger.info("opt is {}".format(opt))
    logger.info("-" * 20)

# Value gets displayed, *optional parameters are actually a tuple ()
fun_four('apple')

# Value gets displayed, *optional parameters populate the tuple ()
fun_four('apple', 'blueberry', 'peach', 'cherry')

# Has keyword-only parameters
def fun_five(*, spam=0, eggs=0):
    logger.info("fun_five():")
    logger.info(f"spam is: {spam}")
    logger.info(f"eggs is: {eggs}")

# Consumes default values
fun_five()

# Order doesn't matter with keyword arguments
fun_five(spam=1, eggs=2)
fun_five(eggs=1, spam=1)

# Overwrite one value, consume the default for another
fun_five(spam=1)
fun_five(eggs=2)

# Use keyword-named parameters
def fun_six(**named_args):
    logger.info("fun_six():")
    # Iterate over named params and access value at object key named_args[name]
    for name in named_args:
        logger.info(f"{name} ==> {named_args[name]}")

fun_six(name="lancelot", quest="grail", colour="red")

# Display values of optional keyword arguments
def fun_six(**named_args):
    logger.info(named_args)
    logger.info(type(named_args))

fun_six()

# Default parameters
#
#   => assigned with equal sign
#   => used if no values are passed to the function
#
# Required parameters can have default values. THey are assigned to parameters via the equals (=) sign. 
# Parameters without defaults CANNOT be specified after parameters with defaults.

logger.info("Default Parameters")

# Required positional parameter with default parameter. Default parameters MUST come after positional ones.
def spam(greeting, whom='world'):
    logger.info(f"{greeting}, {whom}")

spam("Hello")
spam("Hello", "Mom")

# No optional parameters (* is placeholder), one keyword parameter with no assignment, and
# one keyword parameter with a default value
def ham(*, file_name, file_format='txt'):
    logger.info(f"Processing {file_name} as {file_format}")

ham(file_name='eggs')
ham(file_name='toast', file_format='csv')

# Name Resolution (aka Scope)
#
#   => what is "scope"
#   => Scopes used dynamically
#   => Four levels of scope
#   => Assignments always go into the innermost scope (start with local)
#
# A scope is the area of a Python program where an unqualified (not preceded by a module name) can
# be looked up.
#
# Scopes are used dynamically. There are four nested scopes that are searched for names in the
# following order:
#
#   => local    : local names bound within a function
#   => nonlocal : local names plus local names of outer function(s)
#   => global   : current module's global names
#   => builtin  : built-in functions (contents of the __builtins__ module)
#
# Within a function, all assignments and declarations create local names. All variables found outside of
# local scope (that is, outside of the function) are read-only.
#
# Inside functions, local scope references the local names of the current function. Outside functions, local
# scope is the same as the global scope -- the module's namespace. Class definitions also create a local scope.
#
# Nested functions provide another scope. Code in function B which is defined inside function A has read-only
# access to all of A's variables. This is called nonlocal scope.

logger.info("### Name Resolution ###")
logger.info("Scope Examples")

# Example showing different kinds of scope

# global scope
x = 42
def function_a():
    # local scope to a
    y = 5

    def function_b():
        # local scope to b
        z = 32
        logger.info(f"function_b(): z is {z}")
        logger.info(f"function_b(): y is {y}")
        logger.info(f"function_b(): x is {x}")
        # builtin-scope
        logger.info(f"function_b(): type(x) is {type(x)}")

    return function_b

# Stores function as a callable
f = function_a()
logger.info(type(f))

# Call the function
f()

# The global keyword (BAD BAD BAD BAD BAD).
#
# The global keyword allows a function to modify a global variable. Bad because mutating global data could
# lead to all sorts of hard, troubleshooting issues. A function might change a global that affects other
# parts of the system.
#
# It's better to pass data into functions as parameters and return data as needed. Mutable objects, such as
# lists, sets, or dictionaries, can be modified in place => called by reference.
#
# The nonlocal keyword can be used to make nonlocal variable in an outer function writable. Again, using
# globally scoped variables is dangerous and should be avoided as much as possible!@!.

# Modules
#
#   => files containing python code
#   => end in .py
#   => No real difference from scripts
#
# A module is a file containing Python definitions and statements. The file name is the module name with
# the suffix .py appended. Within a module, the module's name (as a string) is available as the value
# of the global variable name.
#
# To use a module named spam.py, say "import spam"
#
# This does not enter the names of the functions defined in spam directly into the symbol table; it only
# adds the module name spam. Use the module name to access the functions or other attributes.
#
# Python uses modules to contain function sthat can be loaded as needed by scripts. A simple module contains
# one or more functions; more complex modules can contain initialization code as well. Python classes are also
# implemented as modules.
#
# A module is only loaded ONCE, even if there are multiple places in an application that import it.
# 
# Modules and packages should be documented with docstrings.

# Using Import
#
# import statement loads modules
#
# Three variations on the import statement:
#
#   => import module
#   => from module import function-list
#   => from module import * (Use with caution!!@!)
#
# import module
#   => loads the module so its data and functions can be used, but does not put its attributes (names
#       of classes, functions, and variables) into the current namespace.
#
# from module import function, ...
#   => imports only the function(s) specified into the current namespace. Other functions are not 
#       available (even though they are loaded into memory).
#
# from module import *
#   => loads the module, and imports all functions that do not start with an underscore into the current
#       namespace. This should be used with caution, as it can pollute the current namespace and possible
#       overwrite builtin attributes or attributes from a different module.

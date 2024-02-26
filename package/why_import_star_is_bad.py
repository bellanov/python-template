"""Example of why import * is bad."""

# current function in navigation overwrites the initial import from electrical.
from electrical import *
from navigation import *

print(current())
print(voltage())
print(amps())

# Module Search Path => how modules are discovered at runtime
#
#   => searches current folder firest, then predefined locations
#   => Add custom locations to PYTHONPATH
#   => Paths stored in sys.path
#
# When you specify a module to load with the import statement, it first looks in the current directory,
# and then searches the directories listed in the sys.path.
#
#   import sys
#   sys.path
#
# To add locations, put one or more directories to search in the PYTHONPATH environment variable. Separate
# multiple paths by semicolons for windows, or colons for Unix/Linux. This will add them to the sys.path,
# after the current folder, but before the predefined locations.
#
# Windows
#
#   set PYTHONPATH="C:\Documents and settings\Bob\Python"
#
# Linux
#
#   export PYTHONPATH="/home/bob/python"
#
# You can also append to sys.path in your scripts, but this can result in non-portable scripts, and scripts
# that will fail if the location of the imported modules changes.
#
#   import sys
#   sys.path.extend("/usr/dev/python/libs", "/home/bob/pylib")
#   import module1
#   import module2

# Execute modules as scripts
#
#   _name_ is the current module
#
#       set to __main__ if run as script
#       set to module_name if imported
#
# It is sometimes convenient to have a module also be a runnable script. This is handy for testing and
# debugging, and for providing modules that can also be used as standalone utilities.
#
# Since the interpreter defines its own name as '__main__', you can test the current namespace's name
# attribute. If it is '__main__' then you are at the main (top) level of the interpreter, and your
# file is being run as a script; it was not loaded as a module.
#
# Any code in a module that is not contained in function or method is executed when the module is imported.
#
# This can include data assignments and other startup tasks, for example connecting to a database or opening
# a file.
#
# Many modules DO NOT need any initialization code.

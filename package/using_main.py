"""Example use of __main__"""

import sys

# other imports

# constants (aka global variables)

# main function
def main(args):
    function1()
    function2()

def function1():
    print("hello from function1()")

def function2():
    print("hello from function2()")

# Checks if it is a top-level script.
# Checks if it was the file used to start the program!!!
# If so, then call the main function
if __name__ == '__main__':
    # Typical naming convention for the first starting function.
    main(sys.argv[1:])

# Program entry point. While main is not a reserved word, it is a strong convention.
#
# Call main() with the command line parameters (ommiting the script itself).
# String slice skips index 0 for this reason.
    
# Packages
#
#   => Package is a folder containing modules or packages
#   => Startup code goes in __init__.py (optional)
#
# A pckage is a group of related modules or subpackages. The grouping is physical - a package is a
# folder that contains one or more modules. It is a way of giving a hierarchical structure to the
# module namespace so that all modules do not all live in the same folder.
#
# A package may have an initialization script named __init__.py. If present, this script is executed
# when the package or any of its contents are loaded. (In Python 2, __init__.py was required).
#
# Modules in packages are accessed by prefixing the module with the package name, using the dot notation
# used to access module attributes.
#
# Thus, if Module eggs is in package spam, to call the scramble() function in eggs, you would say
# spam.eggs.scramble().
#
# By default, importing a package name by itself has no effect; you must explicitly load the modules in
# the packages. You should usually import the module using its package name, like...
#
#       from spam import eggs, to import from the spam package
# 
# Packages can be nested.
    
# EXAMPLE
#
#
# sound/                    Top-level package
#     __init__.py           Initialize the sound package (optional)
#     formats/              Subpackage for file formats
#         __init__.py           Initialize the formats package (optional)
#         wavread.py
#         wavwrite.py
#         aiffread.py
#         aiffwrite.py
#         auread.py
#         auwrite.py
#         ...

#       effects/            Subpackage for sound effects
#           __init__.py         Initialize the effets package (optional)
#           echo.py
#           surround.py
#           reverse.py
# ...

#       filters/            Subpackage for sound filters
#           __init__.py         Initialize the filters package (optional)
#           equalizer.py
    
# from sound.formats import aiffread
# import sound.effects
# import sounds.filters.equalizer
    
# Configuring import with __init__.py
#
#   => load modules into package's namespace
#   => specify modules to load when * is used
#
# For convenience, you can put import statements in a package's __init__.py to autoload the modules into 
# the package namespace, so that import PKG imports all (or just the selected) modules in the package.
#
# __init__.py can also be used to setup data or other resources that will be used by multiple modules
# within a package.
#
# If the variable __all__ in __init__.py is set to a list of module names, then only these modules will
# be loaded whtn the import is "from PKG import *"
    
# EXAMPLE
#
# Given the following structure...
#
#       __init__.py
#       module_a.py
#           function_a()
#       module_b.py
#           function_b()
#       module_c.py
#           function_c()
#
#   if __init__.py is empty
#     
#       import my_package
#           imports my_package only, but not the contents. No modules are imported. This is not useful.
#
#       import my_package.module_a
#           imports module_a into my_package namespace. Objects in module_a must be prefixed with
#           my_package.module_a
#
#       from my_package import module_a
#           imports module_a into main namespace. Objects in module_a must be prefixed with module_a
#
#       from mypackage import module_a, moduleb
#           imports module_a and module_b into main namespace
#
#       from my_package import *
#           does not import anything
#
#
#   if __init__.py contains:
#       all = ["module_a", "module_b"]
#
#       import my_package
#           Imports my_package only, but not the contents. No modules are imported. This is not useful.
#
#       from my_package import module_a
#           As before, imports module_a into main namespace. Objects in module_a must be prefixed with
#           module_a
#
#       from my_package import *
#           Imports module_a and module_b, but not module_c into main namespace.
#
#
#   if __init__.py contains:
#       all = ["module_a", "module_b"]
#       import module_a
#       import module_b
#
#       import my_package
#           Imports module_a and module_b into the my_package namespace. Objects in module_a must be
#           prefixed with my_package.module_a. Now this is useful.
#
#       from my_package import module_a
#           Imports module_a into the main namespace. Objects in module_a must be prefixed with module_a
#
#       from my_package import *
#           Only imports module_a and module_b into main namespace.
#
#       from my_package import module_c
#           Imports module_c into the main namespace.

# Documenting modules and packages
#
#   => use docstrings
#   => described in PEP 257
#   => Generate docs with Sphinx (optional)
#
# In addition to comments, which are for the maintainer of your code, you should add docstrings, which
# provide documentation for the user of your code.
#
# If the first statement in a module, function, or class is an unassigned string, it is assigned as the
# doctstring of that object. It is stored in the special attribute _doc_, and is so available to code.
#
# The docstring can use any form of literal string, but triple double quotes are preferred, for consistency.
#
# See PEP 257 for a detailed guide on docstring conventions.
#
# Tools such as pydoc, and many IDEs will use information in docstrings. In addition, the Sphinx tool will
# gather docstrings from an entire project and format them as a single HTML, PDF, or EPUB document.




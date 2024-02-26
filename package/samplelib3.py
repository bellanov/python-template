# Aliasing function imports, explicitly naming functions to avoid conflict
from samplelib import spam as pig, ham as hog

pig()
hog()

# How import * can be dangerous
#
#   => imported names may overwrite existing names
#   => be careful to read the documentation
#
# Using import * to import all public names from a module has a high bit of risk. While
# generally harmless, there is the chance that you will unknowingly import a module that
# overwrites some previously-imported module.
#
# To be 100% certain, always import the entire module, or else import names explicitly.


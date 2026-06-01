#!/bin/bash
#
# Format Code Base.

# Format Imports
echo "Formatting imports..."
isort samples

# Format Code
echo "Formatting code base..."
black samples 

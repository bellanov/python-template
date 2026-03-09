#!/bin/bash
#
# Format Code Base.

# Format Imports
echo "Formatting imports..."
isort samples
isort tests

# Format Code
echo "Formatting code base..."
black samples 

# Format Tests
echo "Formatting tests..."
black tests
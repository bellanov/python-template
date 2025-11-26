#!/bin/bash
#
# Lint the code base.

echo "Linting Code"
pylint python_template/

echo "Linting Tests"
pylint tests/
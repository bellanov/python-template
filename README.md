# Python Template

Template for general Python development.

## Requirements

The project is configured to build and test using `tox` in a _Python 3.8_ environment so the following are required:

- Python 3.8

## Installation

First, a local project environment needs to be created, then the project's modules will be installed into locally into a virtual environment.

1. Clone the repository:

   ```sh
   git clone git@github.com:certara/python-template-poc.git
   cd python-template-poc
   ```

1. Create a virtual environment with the appropriate `Python` interpreter:

   ```python
   python3.8 -m venv .venv
   ```

1. Source the virtual environment:

   ```python
   $ source .venv/bin/activate

   $ which python
   /path/to/python-template-poc/.venv/bin/python

   $ python --version
   Python 3.8
   ```

1. Install the Requirements:

   ```python
   pip install -r requirements.txt
   ```

1. Execute tests & coverage:

   ```python
   $ python -m tox

   tests/test_handler.py::test_handler PASSED                               [ 50%]
   tests/test_template.py::test_import PASSED                               [100%]

   ```

1. Test results and coverage are in the `coverage/`directory.

   ```sh
   $ tree coverage/

   coverage/
   ├── coverage.xml
   └── junit.xml

   ```

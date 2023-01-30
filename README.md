# Python Template

Template for general `Python` development.

## Requirements

The project is configured to build and test using `tox` in a _Python 3.10_ environment.

## Installation

First, a local project environment needs to be created, then the project's modules will be installed into locally into a virtual environment.

1. Clone the repository:

   ```sh
   git clone https://github.com/bellanov/python-template.git
   cd python-template
   ```

1. Make your changes!@!

```sh
# Docker Build
docker build -t py-test .
docker run py-test
```

1. Execute the build workflow inside a **Docker** container:

   ```python
   $ python -m tox

   tests/test_package.py::test_hello PASSED                               [100%]

   ```

1. Test results and coverage are in the `coverage/`directory.

   ```sh
   Name                      Stmts   Miss Branch BrPart     Cover   Missing
   ------------------------------------------------------------------------
   src/package/__init__.py       0      0      0      0   100.00%
   src/package/hello.py          2      0      0      0   100.00%
   ------------------------------------------------------------------------
   TOTAL                         2      0      0      0   100.00%

   $ tree coverage/

   coverage/
   ├── coverage.xml
   └── junit.xml

   ```

# python-samples

A series of Python *samples* are available spanning the categories below.

| Sample | Description |
|---|---|
| [*args_kwargs*](https://github.com/bellanov/python-samples/tree/main/samples/args_kwargs) | Overview of *args & kwargs* and their usage. |
| [*assert*](https://github.com/bellanov/python-samples/tree/main/samples/assert) | Overview of *assert* and its usage. |
| [*asychronous_programming*](https://github.com/bellanov/python-samples/tree/main/samples/asychronous_programming) | Overview of *Asynchronous Programming* in Python. |
| [*classes*](https://github.com/bellanov/python-samples/tree/main/samples/classes) | Overview of *Classes / Object-Oriented Programming (OOP)* and their usage. |
| [*control_flow*](https://github.com/bellanov/python-samples/tree/main/samples/control_flow) | Overview of *Control Flow* and its usage. |
| [*counters*](https://github.com/bellanov/python-samples/tree/main/samples/counters) | Overview of *Counters* and their usage. |
| [*defaultdict*](https://github.com/bellanov/python-samples/tree/main/samples/defaultdict) | Overview of *defaultdict* and its usage. |
| [*dictionaries*](https://github.com/bellanov/python-samples/tree/main/samples/dictionaries) | Overview of *Dictionaries* and their usage. |
| [*exceptions*](https://github.com/bellanov/python-samples/tree/main/samples/exceptions) | Overview of *Exceptions* and their usage. |
| [*functions*](https://github.com/bellanov/python-samples/tree/main/samples/functions) | Overview of *Functions* and their usage. |
| [*hello_world*](https://github.com/bellanov/python-samples/tree/main/samples/hello_world) | A very simple *Python* program. |
| [*introduction*](https://github.com/bellanov/python-samples/tree/main/samples/introduction) | A general introduction to the *Python* programming language. |
| [*iterables_and_generators*](https://github.com/bellanov/python-samples/tree/main/samples/iterables_and_generators) | Overview of *Iterables & Generators* and their usage. |
| [*list_comprehensions*](https://github.com/bellanov/python-samples/tree/main/samples/list_comprehensions) | Overview of *List Comprehensions* and their usage. |
| [*lists*](https://github.com/bellanov/python-samples/tree/main/samples/lists) | Overview of *Lists* and their usage. |
| [*modules*](https://github.com/bellanov/python-samples/tree/main/samples/modules) | Overview of *Modules* and their usage. |
| [*randomness*](https://github.com/bellanov/python-samples/tree/main/samples/randomness) | Overview of *Randomness* in Python. |
| [*regex*](https://github.com/bellanov/python-samples/tree/main/samples/regex) | Overview of *Regular Expressions* in Python. |
| [*sets*](https://github.com/bellanov/python-samples/tree/main/samples/sets) | Overview of *Sets* and their usage. |
| [*sorting*](https://github.com/bellanov/python-samples/tree/main/samples/sorting) | Overview of *Sorting* and its usage. |
| [*strings*](https://github.com/bellanov/python-samples/tree/main/samples/strings) | Overview of *Strings* and their usage. |
| [*truthiness*](https://github.com/bellanov/python-samples/tree/main/samples/truthiness) | Overview of *Truthiness* in Python. |
| [*tuples*](https://github.com/bellanov/python-samples/tree/main/samples/tuples) | Overview of *Tuples* and their usage. |
| [*type_annotations*](https://github.com/bellanov/python-samples/tree/main/samples/type_annotations) | Overview of *Type Annotations* in Python. |
| [*virtual_environments*](https://github.com/bellanov/python-samples/tree/main/samples/mvirtual_environments) | Overview of *Virtual Environments* and their usage. |
| [*whitespace_formatting*](https://github.com/bellanov/python-samples/tree/main/samples/whitespace_formatting) | Overview of *Whitespace Formatting* in Python. |
| [*zip_argument_unpacking*](https://github.com/bellanov/python-samples/tree/main/samples/zip_argument_unpacking) | Overview of *zip & Argument Unpacking* in Python. |

# Script Execution

In some cases, scripts may not execute due to the "samples" module not being available. This is because the project is not on the PYTHONPATH.

```sh
pytest
======================================================= ERRORS ========================================================
_____________________________________ ERROR collecting tests/test_hello_world.py ______________________________________
ImportError while importing test module 'C:\Users\cityd\Documents\GitHub\python-samples\tests\test_hello_world.py'.
Hint: make sure your test modules/packages have valid Python names.
Traceback:
..\..\..\anaconda3\envs\dsfs\Lib\importlib\__init__.py:88: in import_module
    return _bootstrap._gcd_import(name[level:], package, level)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
tests\test_hello_world.py:4: in <module>
    from samples.hello_world.app import hello_world
E   ModuleNotFoundError: No module named 'samples'
=============================================== short test summary info ===============================================
ERROR tests/test_hello_world.py
!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!! Interrupted: 1 error during collection !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
================================================== 1 error in 0.10s ===================================================
```

Execute the following command to add the application directory to the PYTHONPATH.

```sh
pip install -e .

Obtaining file:///C:/Users/cityd/Documents/GitHub/python-samples
  Installing build dependencies ... done
  Checking if build backend supports build_editable ... done
  Getting requirements to build editable ... done
  Installing backend dependencies ... done
  Preparing editable metadata (pyproject.toml) ... done
Building wheels for collected packages: python-samples
  Building editable for python-samples (pyproject.toml) ... done
  Created wheel for python-samples: filename=andy_python_samples-0.2.0-py3-none-any.whl size=5609 sha256=19e163f506a80d9f01a397dba46a954c5617a4f7c98699c0e22bedb81798f271
  Stored in directory: C:\Users\cityd\AppData\Local\Temp\pip-ephem-wheel-cache-19vbw_17\wheels\a6\17\c0\d817a572e54c10a4033b71215a913d15bf9712d87f48f8d38b
Successfully built python-samples
Installing collected packages: python-samples
Successfully installed python-samples-0.2.0
```

Now the previous command should execute successfully.

```sh
pytest
================================================= test session starts =================================================
platform win32 -- Python 3.14.3, pytest-9.0.2, pluggy-1.6.0
rootdir: C:\Users\cityd\Documents\GitHub\python-samples
configfile: pyproject.toml
collected 1 item

tests\test_hello_world.py .                                                                                      [100%]

================================================== 1 passed in 0.01s ==================================================
```
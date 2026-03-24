# Virtual Environments

Overview of *Virtual Environments* and their usage.

*Virtual Environments* are sandboxed Python **environments** that maintain their own versions of Python libraries and/or Python itself.

I recommended you install the [Anaconda](https://www.anaconda.com/download) Python distribution, so in this section I’m going to explain how Anaconda’s environments work. If you are not using Anaconda, you can either use the built-in `venv` module or install `virtualenv`. In which case you should follow their instructions instead.

## Execution

To create an (Anaconda) virtual environment, you just do the following:

```sh
# create a Python 3.14 environment named "dsfs"
conda create -n dsfs python=3.14
```

Follow the prompts, and you’ll have a virtual environment called “dsfs,” with the instructions:

```sh
#
# To activate this environment, use
#
#     $ conda activate dsfs
#
# To deactivate an active environment, use
#
#     $ conda deactivate
```

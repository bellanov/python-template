# python-samples

A series of Python *samples* are available spanning the categories below.

| Sample | Description |
|---|---|
| [*builder_pattern*](https://github.com/bellanov/python-samples/tree/main/samples/builder_pattern) | Overview of the *Builder Pattern* and its usage. |
| [*hello_world*](https://github.com/bellanov/python-samples/tree/main/samples/hello_world) | A very simple *Python* program. |
| [*retry_pattern*](https://github.com/bellanov/python-samples/tree/main/samples/retry_pattern) | Overview of the *Retry Pattern* and its usage. |
| [*strategy_pattern*](https://github.com/bellanov/python-samples/tree/main/samples/dsa/strategy_pattern) | Overview of the *Strategy Pattern* and its usage. |

## Script Execution

First, a local project environment needs to be created, then the project's dependencies need to be be installed.

1. Clone the repository.

   ```sh
   git clone https://github.com/bellanov/python-template.git
   cd python-template
   ```

2. Install Dependencies.

   ```sh
   # Install Dependencies
   scripts/install.sh
   ```
## Testing, Linting, and Formatting

Execute the tests to validate your installation.

### Linux

```sh
scripts/test.sh
scripts/lint.sh
scripts/format.sh
```

### Windows

```sh
.\scripts\test.ps1
.\scripts\lint.ps1
.\scripts\format.ps1
```
# Python Template

Template for general `Python` development.

## Requirements

The project is configured to build and test inside a `Docker` in a _Python 3.10_ environment.

## Development Workflow

First, a local project environment needs to be created, then the project's modules will be installed into locally into a virtual environment.

1. Clone the repository:

   ```sh
   git clone https://github.com/bellanov/python-template.git
   cd python-template
   ```

1. Make your changes and **build** the application.

```sh
# Build
docker build -t python-template .

# Execute
docker run python-template
# BOOTSTRAPPING application workflow
# BOOTSTRAPPING application workflow COMPLETED
```

1. Execute Unit Tests (in Docker as well #KISS)

```sh
docker build -t test-python-template= -f test.Dockerfile .
```

1. Build a Release Artifact.

```sh
docker build -t python-template-release -f release.Dockerfile .
```
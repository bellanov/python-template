# Python Template

Template for general `Python` development.

## Requirements

The project is configured to build and test inside a `Docker` in a _Python 3.10_ environment.

## Development Workflow

First, a local project environment needs to be created, then the project's modules will be installed into locally into a virtual environment.

1. Clone the repository.

   ```sh
   git clone https://github.com/bellanov/python-template.git
   cd python-template
   ```

2. Create a virtual environment.

   ```sh
   # Create Virtual Environment
   python3 -m venv .venv

   # Activate Virtual Environment
   source .venv/bin/activate

   # Install Dependencies
   pip install -r requirements.txt 

   # Deactivate Virtual Environment
   deactivate
   ```

3. Make your changes and **build** the application.

   ```sh
   # Build & Unit Test Docker Image
   scripts/build.sh

   # Execute Docker Image
   scripts/deploy.sh

   # BOOTSTRAPPING application workflow
   # EXECUTING application workflow
   # Hello World!!!
   # BOOTSTRAPPING application workflow COMPLETED

   # Teardown Docker Container
   scripts/teardown.sh

   # Purge Docker Image
   scripts/purge.sh
   ```

4. Tag and version code changes. This will trigger a build in **Google Cloud Platform (GCP)** that will be associated with the code changes.

   ```sh
   git tag -a "1.2.3" -m "Version 1.2.3"
   git push --follow-tags
   ```
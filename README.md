# Python Katas Exercises

## Table of contents

- [Katas Exercises](#python-katas-exercises)

  - [Table of contents](#table-of-contents)
  - [Getting started](#getting-started)
  - [Usage](#usage)

    - [Kata 1: extractBookNames](#kata-1-extractBookNames)
    - [Kata 2: sumNumbers](#kata-2-sumNumbers)

  - [Development](#development)
    - [Style guide](#style-guide)
    - [Testing](#testing)
      - [Running tests](#running-tests)
  - [After finishing a task](#after-finishing-a-task)

## Getting started

1. First, clone the repo and install the dependencies,

   ```
    pip install -r requirements.txt
   ```

   Keep in mind that we use pip for managing Python packages.

## Usage

This repository contains several exercises implemented in Python. Below are the details for each exercise and the necessary commands to run each one and their respective tests.

### Kata 1: extractBookNames

This exercise extracts all book names from an array of people, each with their own array of books.

For more details, please refer to the [README](src/extractBookNames/README.md) inside the `src/extractBookNames` directory.

### Kata 2: sumNumbers

This exercise sums all numbers in an array and returns the total.

For more details, please refer to the [README](src/sumNumbers/README.md) inside the `src/sumNumbers` directory.

## Development

### Style guide

Before submitting a patch, please make sure that the code is formatted executing this command:

```
black .
```

### Testing

Testing is crucial for us and we strive for high coverage of our code.

We encourage you to write tests for every functionality you build and also update the existing ones if they need to.

#### Running tests

Before running the test, install the needed dependencies:

```
pip install -r requirements.txt
```

Execute all tests with:

To run the tests we need to run this script

```
pytest
```

## After finishing a task

Before pushing your changes, make sure you run the linter and prettier to ensure the code follows the rules, or the CI pipeline will throw an error and fail:

```
flake8
black .
```

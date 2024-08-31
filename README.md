# CraftGraph

## Description

A brief description of your project, what it does, and its purpose.

## Installation

Instructions on how to install and set up your project. For example:

```bash
# Clone the repository
git clone https://github.com/yourusername/yourproject.git

# Navigate into the project directory
cd yourproject

# Install dependencies
poetry install
```

## Usage

Instructions on how to use your project. For example:

```bash
poetry run python your_script.py
```

## Linting

This project uses `flake8` for linting.

### Running flake8

To check your code for style violations using `flake8`, run:

```bash
poetry run flake8 .
```

### Running flake8 with pytest

To run `flake8` with `pytest`, use the following command:

```bash
poetry run flake8 --extend-select=E203,E266,E501,W503 --ignore=E266,W503 .
```

## Project Documentation

This project uses [MkDocs](https://www.mkdocs.org/) for documentation.

### Installing MkDocs
To install MkDocs, run:
```sh
poetry add mkdocs
```

### Serving Documentation Locally
To serve the documentation locally, run:
```sh
mkdocs serve
```

### Building Documentation
To build the documentation, run:
```sh
mkdocs build
```

## Contributing

Guidelines for contributing to your project.

## License

Information about the license under which your project is distributed.

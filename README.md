# CraftGraph

## Description

CraftGraph is a simple game focused on crafting and resource gathering, where game logic is defined using knowledge
graphs and implemented in Python. The game features resource collection, crafting mechanics, and aims to create an
engaging and educational experience while demonstrating the use of knowledge graphs in game development.

## Installation

Instructions on how to install and set up your project. For example:

```bash
# Clone the repository
git clone https://github.com/smileynet/craftgraph.git

# Navigate into the project directory
cd craftgraph

# Install dependencies
poetry install
```

## Usage

Instructions on how to use your project. For example:

```bash
poetry run python main.py
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

## Rendering Knowledge Graphs

### Graphviz

TBD, install Graphviz

### Plotly

TBD
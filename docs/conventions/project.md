# Project Style and Hygiene

This document outlines the conventions for maintaining code quality, consistency, and hygiene across the project.

## Table of Contents
1. [Coding Standards](#coding-standards)
2. [Linting](#linting)
3. [Code Comments](#code-comments)
4. [File Naming Conventions](#file-naming-conventions)
5. [Versioning and Changelogs](#versioning-and-changelogs)
6. [Environment Setup](#environment-setup)

## Coding Standards

- **Style Guide**: Follow the [PEP 8](https://peps.python.org/pep-0008/) style guide for Python code.
- **Best Practices**:
  - **Type Hints**: Use type hints for function signatures and variable annotations where applicable.
  - **Docstrings**: Write clear and descriptive docstrings for all public modules, functions, classes, and methods.
  - **Code Readability**: Prioritize readability and simplicity in code design.
  - **Consistent Naming**: Use consistent and meaningful naming conventions for variables, functions, and classes.

## Linting

- **Tool**: Use `flake8` for linting.
- **Command**: Run `poetry run flake8` to check for style violations and enforce coding standards.
- **Configuration**: Customize `.flake8` configuration file as needed to fit the project’s requirements.

## Code Comments

- **Clarity**: Write comments that clearly explain the purpose of the code, not just what the code is doing.
- **Relevance**: Ensure comments are relevant and updated as the code evolves.
- **Type**: Use inline comments for brief explanations and block comments for more detailed descriptions.

### Commenting Style
- **Inline Comments**: Place inline comments on the same line as the code they describe, separated by at least two spaces.
- **Block Comments**: Start block comments with a capital letter and use punctuation where appropriate. Leave a blank line before and after the comment block.

## File Naming Conventions

- **Descriptive Names**: Use descriptive and meaningful names that convey the purpose of the file.
- **Lowercase with Hyphens**: Use lowercase letters with hyphens to separate words (e.g., `user-profile.md`).
- **Avoid Special Characters**: Avoid using special characters or spaces in file names.

## Commit Message Conventions

### General Guidelines
- **Conventional Commits**: Follow the [Conventional Commits](https://www.conventionalcommits.org/) specification for commit messages.
- **Present Tense**: Write commit messages in the present tense (e.g., "Add feature" not "Added feature").
- **Imperative Mood**: Use the imperative mood for the subject line (e.g., "Fix bug" instead of "Fixed bug").
- **Limit Length**: Keep the subject line to 50 characters or less. Use the body of the commit message for additional details.

### Format
```
<type>[optional scope]: <subject>

[optional body]

[optional footer(s)]
```

### Types
- **feat**: A new feature.
- **fix**: A bug fix.
- **docs**: Documentation only changes.
- **style**: Changes that do not affect the meaning of the code (white-space, formatting, missing semi-colons, etc.).
- **refactor**: A code change that neither fixes a bug nor adds a feature.
- **test**: Adding missing tests or correcting existing tests.
- **chore**: Changes to the build process or auxiliary tools and libraries such as documentation generation.

## Versioning and Changelogs

- **Semantic Versioning**: Follow [Semantic Versioning](https://semver.org/) (e.g., `1.0.0`).
- **Major.Minor.Patch**: Increment the version number according to the significance of changes.
- **Changelog Guidelines**: Maintain a `CHANGELOG.md` file to document all notable changes. Each entry should include the version number, release date, and a brief description of changes.

## Environment Setup

- Ensure you have Python 3.10 or higher installed.
- Use `poetry` to manage dependencies and virtual environments.
- Run `poetry install` to set up the project environment.
- Activate the virtual environment with `poetry shell` before running scripts or tests.

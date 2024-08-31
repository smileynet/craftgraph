# Coding Conventions

This file outlines the specific coding conventions and guidelines to be followed in this project.

## Table of Contents
1. [Coding Standards](#coding-standards)
2. [Linting](#linting)
3. [Environment Variables](#environment-variables)
4. [Testing](#testing)
5. [LLM Prompt References](#llm-prompt-references)

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
- **Configuration**: Customize `[flake8]` section of 'configuration file as needed to fit the project’s requirements.

## Environment Variables

- **Storage**: Store sensitive information and configuration variables in a `.env` file located in the project root directory.
- **Loading**: Use the `python-dotenv` library to load environment variables.
- **Best Practices**:
  - Always refer to environment variables using `os.getenv()` or similar methods.
  - Avoid hardcoding sensitive information like API keys in code.
  - Use placeholder text (e.g., `{API_KEY}`) in code examples, replacing it with actual values at runtime.

## Testing

- **Tool**: Use [pytest](https://docs.pytest.org/en/stable/) for testing.
- **Requirements**:
  - Ensure all tests pass before pushing any changes.
  - Write unit tests for all critical functionalities.
- **Running Tests**: Use `poetry run pytest` to execute tests in the terminal. Note that `pytest` is configured to include the `src` directory in its path, so imports should not include `src` as part of the import string. Tests for `CraftGraph` are located in `tests/CraftGraph/`.
- **Test Design**:
  - Prefix test function names with `test_` to ensure they are discovered by pytest.
  - Use descriptive names for test functions to clearly indicate what is being tested.
  - Utilize pytest fixtures for setup and teardown operations.
  - Incorporate assertions to verify expected outcomes.
  - Consider using parameterized tests to efficiently test multiple scenarios.

## LLM Prompt References

When generating or discussing code in prompts, adhere to the following guidelines:

1. **Environment Variables**:
   - Refer to environment variables using `os.getenv()` or similar methods.
   - Never hardcode sensitive information in prompts or code.
   - Use placeholders (e.g., `{API_KEY}`) and explain they should be replaced with actual values at runtime.

2. **Testing**:
   - Always include `import pytest` at the beginning of test code examples.
   - Demonstrate proper use of pytest fixtures for setup and teardown.
   - Show how to write clear and descriptive test functions.
   - Include assertions to verify expected outcomes.
   - Emphasize the use of parameterized tests to handle multiple test cases.

By following these coding conventions, we ensure that our codebase remains clean, maintainable, and aligned with industry best practices.

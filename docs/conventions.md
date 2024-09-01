# CraftGraph Conventions

## Knowledge Graphs
- **Library**: Use the `networkx` library for creating and managing knowledge graphs, implemented in `src/CraftGraph/knowledge_graph_parser.py`.
- **Structure**: Define resources and crafting recipes as nodes and edges within the graph.
- **Best Practices**:
  - Ensure that each node represents a unique resource or item.
  - Use directed edges to represent dependencies or crafting recipes.
  - Keep the graph updated with any new resources or recipes added to the game.

## General Coding Conventions
- Follow the project's overall coding conventions as outlined in the main documentation.
- Ensure code readability and maintainability by adhering to established best practices.

## Documentation Guidelines
- **Clarity**: Write clear and concise sentences. Avoid jargon and explain technical terms when necessary.
- **Consistency**: Use consistent terminology, formatting, and tone throughout all documentation.
- **Active Voice**: Prefer active voice over passive voice (e.g., "Run the tests" instead of "The tests should be run").
- **Headings**: Use hierarchical headings (e.g., `##`, `###`) to organize content and improve readability.
- **Code Blocks**: Use triple backticks (```) for code blocks and specify the language (e.g., ```python).
- **Inline Code**: Use single backticks (`) for inline code snippets.
- **Lists**: Use bullet points for unordered lists and numbers for ordered lists.
- **Links**: Use descriptive text for hyperlinks, avoiding raw URLs (e.g., [Python Documentation](https://docs.python.org/3/)).

## Updating Documentatio, before updating documentation.
- **Consistency**: Ensure updates align with the existing structure and tone of the document.
- **Accuracy**: Verify that the updates reflect the actual project practices and tools in use.
- **Clarity**: Maintain clear, concise, and unambiguous language.
- **Documentation**: Any new tools, processes, or conventions introduced should include references or links to official documentation where applicable.

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
- **Configuration**: Customize `.flake8` configuration file as needed to fit the project's requirements.

## Code Comments
- **Clarity**: Write comments that clearly explain the purpose of the code, not just what the code is doing.
- **Relevance**: Ensure comments are relevant and updated as the code evolves.
- **Type**: Use inline comments for brief explanations and block comments for more detailed descriptions.
- **Inline Comments**: Place inline comments on the same line as the code they describe, separated by at least two spaces.
- **Block Comments**: Start block comments with a capital letter and use punctuation where appropriate. Leave a blank line before and after the comment block.

## File Naming Conventions
- **Descriptive Names**: Use descriptive and meaningful names that convey the purpose of the file.
- **Lowercase with Hyphens**: Use lowercase letters with hyphens to separate words (e.g., `user-profile.md`).
- **Avoid Special Characters**: Avoid using special characters or spaces in file names.

## Commit Message Conventions
- **Conventional Commits**: Follow the [Conventional Commits](https://www.conventionalcommits.org/) specification for commit messages.
- **Present Tense**: Write commit messages in the present tense (e.g., "Add feature" not "Added feature").
- **Imperative Mood**: Use the imperative mood for the subject line (e.g., "Fix bug" instead of "Fixed bug").
- **Limit Length**: Keep the subject line to 50 characters or less. Use the body of the commit message for additional details.
- **Format**:
  ```
  <type>[optional scope]: <subject>

  [optional body]

  [optional footer(s)]
  ```
- **Types**:
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

## Environment Variables
- **Storage**: Store sensitive information and configuration variables in a `.env` file located in the project root directory.
- **Loading**: Use the `python-dotenv` library to load environment variables.
- **Best Practices**:
  - Always refer to environment variables using `os.getenv()` or similar methods.
  - Never hardcode sensitive information in prompts or code.
  - Use placeholders (e.g., `{API_KEY}`) and explain they should be replaced with actual values at runtime.

## Testing
- **Tool**: Use [pytest](https://docs.pytest.org/en/stable/) for testing.
- **Requirements**:
  - Ensure all tests pass before pushing any changes.
  - Write unit tests for all critical functionalities.
- **Running Tests**: Use `poetry run pytest` to execute tests in the terminal.
- **Import Conventions**:
  - When importing modules from `src` in test files, use the module name directly without the `src.` prefix.
  - Example: Use `from resource_manager import ResourceManager` instead of `from src.resource_manager import ResourceManager`.
- **Test Location**: Place all test files directly in the `tests/` directory.
- **Test Design**:
  - Prefix test function names with `test_` to ensure they are discovered by pytest.
  - Use descriptive names for test functions to clearly indicate what is being tested.
  - Utilize pytest fixtures for setup and teardown operations.
  - Incorporate assertions to verify expected outcomes.
  - Consider using parameterized tests to efficiently test multiple scenarios.

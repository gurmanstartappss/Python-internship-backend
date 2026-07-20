"""poetry
pip install poetry-to install poetry 
poetry new project name-to create a poetry of a project
poetry add dependency-to add dependency in poetry file 
poetry install-to install all the dependencies automatically
poetry remove dependency-remove dependencies automatically
poetry update dependency-update the dependency
poetry show-show installed packages
poetry shell-activate virtual env

pip                             poetry
installs packages only          manages packages,virtual env,project config and metadata
uses requirement.txt            poetry uses pyproject.toml and lock file

ruff is a very fast python linter and formatter 
It can automatically:
Remove unused imports
Fix formatting issues
Sort imports
Apply many other safe fixes

ruff check --fix 

ruff check
detects linting issues
(unused import, import order, undefined variables, etc.)

ruff format
formats code style
(spacing, indentation, quotes, etc.)

Ruff in Poetry:
- poetry add --group dev ruff
- poetry run ruff check .
- poetry run ruff check --fix .
- poetry run ruff format .
- Runs Ruff inside Poetry's virtual environment.
pip install ruff

"E"  # pycodestyle errors
x=10  # E225 missing whitespace around operator
x = 10

"W"  # pycodestyle warning
name = "sdfghjjjjjjjjjjjjjjbbbbbbbbbbbbbbbbbbb  # W505 line too long
x = "abc"
"F" # pyflakes
import os
print("hello")

print(a)

ruff : F401 'os' imported but unused
ruff : F821 undefined name 'a'

"I" # isort

incorrect
import django
import os
import request

correct
import os

import django
import request
5. "B"--flake8.bugbear #  find common bugs 
6. "up" -- pyupgrade : convert old syntax to new syntax
7. "N" -- pep8-naming:check naming convention
8. "S" -- flake8-bandit:used for security(if we write password as admin123)  Ruff: S105 possible hardcoded password
9. "DJ" -- flake8-django : check django specific mistakes

ruff commands format all files:

poetry run ruff format .        (fixed ruff format)
poetry run ruff check .         (check for linting (spaces in lines  ) issues)
poetry run ruff check . --fix   (automatically fix issues)
"""
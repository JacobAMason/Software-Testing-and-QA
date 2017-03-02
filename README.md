[![Build Status](https://travis-ci.org/JacobAMason/Software-Testing-and-QA.svg?branch=master)](https://travis-ci.org/JacobAMason/Software-Testing-and-QA) [![Coverage Status](https://coveralls.io/repos/github/JacobAMason/Software-Testing-and-QA/badge.svg?branch=master)](https://coveralls.io/github/JacobAMason/Software-Testing-and-QA?branch=master)
# Software Testing and Quality Assurance

Attn Dr. Williams: The requested Assignment pdf can be found in the Assignment1 folder.

## Running Assignment 1
```
git clone https://github.com/JacobAMason/Software-Testing-and-QA.git
cd Software-Testing-and-QA
pip install -e .
python Assignment1/command_line_insterface.py
```

## Development Instructions
To download an Assignment, just clone the repository or download as a zip.
You will need Python, specifically Python 3.6.
This project should run on any system officially supported by Python 3.6.
Requirements for running the assignments are found in `requirements.txt`. Requirements for running unit tests are found in `test_requirements.txt`.
To install requirements, run `pip install -r test_requirements.txt` and `pip install -r requirements.txt`.
This can be done from a virtual environment, if you want to keep this project's dependencies separate from your system Python.

Unit tests are managed by tox.
To run them, simply issue the command `tox` from your system's terminal in the root project directory.
This command will complete with coverage information printed to the terminal.

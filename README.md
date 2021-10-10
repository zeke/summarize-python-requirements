# Summarize Requirements 🐍 📜

> Annotate your Python `requirements.txt` file with summaries of each package.

## What?

This is a tool that:

- Takes a Python `requirements.txt` file as input
- Fetches the summary of each package from the PyPi registry
- Outputs an equivalent requirements list with added comments summarizing each package

It can be used as a Python module or a command line script.

## Example

Before:

```
black==21.9b0
gunicorn==20.1.0
pytz==2021.3
requests==2.26.0
rope==0.20.1
whitenoise==5.3.0
```

After:

```
black==21.9b0                            # The uncompromising code formatter.
gunicorn==20.1.0                         # WSGI HTTP Server for UNIX
pytz==2021.3                             # World timezone definitions, modern and historical
requests==2.26.0                         # Python HTTP for Humans.
rope==0.20.1                             # a python refactoring library...
whitenoise==5.3.0                        # Radically simplified static file serving for WSGI applications
```

## Installation

Note: This is not a published package yet. For now:

```sh
git clone https://github.com/zeke/summarize-requirements
cd summarize-requirements
```

## Command Line Usage

The CLI reads a requirements file as input and prints summarized results as output. It does not overwrite the existing file.

If you run the command with no arguments, it'll look for `requirements.txt` in the current directory:

```sh
python index.py
```

Or you can specify a different file:

```sh
python index.py ~/path/to/your/requirements.txt > new-requirements.txt
```

## Programmatic Usage

```py
from summarize import summarize

for line in summarize('requirements.txt'):
    print(line)
```

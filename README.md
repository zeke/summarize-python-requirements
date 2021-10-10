# Summarize Requirements

> Annotate your Python `requirements.txt` file with summaries of each package.

## What?

This is a command line tool that:

- Takes a Python `requirements.txt` file as input
- Fetches the summary of each package from the PyPi registry
- Outputs an equivalent `requirements.txt` with added comments summarizing each package

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

If you run the command with no arguments, it'll look for `requirements.txt` in the current directory:

```sh
python index.py
```

Or you can specify a differnt requirements file:

```sh
python index.py ~/path/to/your/requirements.txt > new-requirements.txt
```

You can also pipe the output back into the file to update it:

```sh
python index.py requirements.txt > requirements.txt
```

## Programmatic Usage

```py
from summarize import summarize

for line in summarize('requirements.txt'):
    print(line)
```
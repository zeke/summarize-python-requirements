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
requests==2.26.0
requirements-parser==0.2.0
```

After:

```
black==21.9b0                            # The uncompromising code formatter.
requests==2.26.0                         # Python HTTP for Humans.
requirements-parser==0.2.0               # Parses Pip requirement files
```

## Installation

Note: This is not a published package yet. For now:

```sh
git clone https://github.com/zeke/summarize-requirements
cd summarize-requirements
```

## Usage

```sh
python index.py ~/path/to/your/requirements.txt > new-requirements.txt
```
Run the following in your virtualenv:

```sh
pip install -e .[dev]

pytest
```

## How this package was published

Notes to self, since this was my first time publish a Python package.

Video: [Publishing (Perfect) Python Packages on PyPi](https://www.youtube.com/watch?v=GIF3LaRqgXo)


Noteable commands:

```
 2301  python setup.py sdist
 2302  python setup.py sdist
 2303  tar tzf dist/summarize-requirements-0.0.1.tar.gz
 2304  pip install check-manifest
 2305  check-manifest --create
 2306  check-manifest --version
 2307  python setup.py sdist
 2308  tar tzf dist/summarize-requirements-0.0.1.tar.gz
 2309  python setup.py bdist_wheel sdist
 2310  pip install twine
 2311  twine --version
```
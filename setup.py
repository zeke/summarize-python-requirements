from setuptools import setup

with open("README.md", "r") as fh:
  long_description = fh.read()

setup(
  name='summarize-requirements',
  version='0.0.1',
  description='Annotate your requirements.txt file with a short summary of each package.',
  url="https://github.com/zeke/summarize-python-requirements",
  author="Zeke Sikelianos",
  author_email="zeke@sikelianos.com",
  long_description=long_description,
  long_description_content_type="text/markdown",
  py_modules=["summarize_requirements"],
  package_dir={'': 'src'},
  install_requires=[
    "requests==2.26.0",
    "requirements-parser==0.2.0",
  ],
  extras_require={
    "dev": [
      "check-manifest>=0.47",
      "pytest>=3.7",
      "twine>=3.4.2",
    ],
  },
  classifiers=[
    "Environment :: Console",
    "License :: OSI Approved :: MIT License",
    "Programming Language :: Python :: 3",
    "Programming Language :: Python :: Implementation :: PyPy",
    "Programming Language :: Python",
    "Topic :: Documentation",
    "Topic :: Software Development :: Documentation",
    "Topic :: Software Development :: Libraries :: Python Modules",
  ]
)
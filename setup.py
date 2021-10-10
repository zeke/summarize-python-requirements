from setuptools import setup

setup(
  name='summarize-requirements',
  version='0.0.1',
  description='Annotate your requirements.txt file with a short summary of each package.',
  py_modules=["summarize_requirements"],
  package_dir={'': 'src'},
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
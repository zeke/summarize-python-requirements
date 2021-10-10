from setuptools import setup

setup(
  name='summarize-requirements',
  version='0.0.1',
  description='Annotate your requirements.txt file with a short summary of each package.',
  py_modules=["summarize_requirements"],
  package_dir={'': 'src'},
)
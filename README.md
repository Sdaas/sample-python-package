# Context

This shows the structure of a python package reposistory (`docparser`) that contains two modules - `hdfc` and `sbi`

# Usage

Go to the directory where you wish to use this package. Setup the `virtualenv` in the nornal way.

Install a local copy of the pckage `pip install -e ~path-to-package-repo`
This will install the package mypackage and all its dependencies 

```python
from docparser import hdfc, sbi

print("hello world")
print( hdfc.foo())
print( sbi.bar())

```
Any changes made to code in mydocs will be picked up in the myrepo - no need to do anything more

# Development Guide

Setup the virtual env

```bash
virtualenv myenv
source myenv/bin/activate  # or venv\Scripts\activate on Windows

```

Set up the requiremens / dependencies
```bash
pip install -r requirements.txt
```
Setup the dev dependencies
```bash
pip install -r dev-requirements.txt
```

Run all the tests
```bash
pytest # Runs all the test in the tests directory
```

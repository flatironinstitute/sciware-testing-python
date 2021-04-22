# Sciware Testing Examples and Exercises

[![](https://github.com/flatironinstitute/sciware-testing-python/actions/workflows/test.yml/badge.svg)](https://github.com/flatironinstitute/sciware-testing-python/actions/workflows/test.yml/)

This is an example repository for writing tests, for the Sciware Testing session. 
It demonstrates how to setup a repository to use GitHub actions to automatically run tests
on the code.

## Quick-start

### Test

```bash
git clone https://github.com/flatironinstitute/sciware-testing-python.git
cd sciware-testing-python
python3 ./setup.py pytest
```

## Forking This Project

## Contents

* **`README.md`** - File generating this page.
* **`setup.py`** - File describing the metadata for the package and rules to build/install/test it.
* **`requirements.txt`** - File listing the packages required to run the code. It is included by setup.py.
* **`LICENSE`** - File containing the text of the license the code is released under. Having a license file allows other people to use the code.
* **`sciware_testing_python/`** - Directory for all the code.
* **`sciware_testing_python/__init.py__`** - File that python imports to define the `sciware_testing_python` package.
* **`sciware_testing_python/sciware_testing_python.py`** - File with all of the code.
* **`tests/`** - Directory for the code which tests the code in `sciware_testing_python`.
* **`tests/test_sciware_testing_python.py`** - File containing the tests.
* **`.gitignore`** - File which tells github what files to not track (optional)
* **`.github/workflows/`** - Directory containing the configuration file for GitHub actions.
* **`.github/workflows/test.yml`** - File detailing the system configurations to use for the tests.

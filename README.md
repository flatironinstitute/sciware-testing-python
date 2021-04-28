# Sciware Testing Examples and Exercises

[![](https://github.com/flatironinstitute/sciware-testing-python/actions/workflows/test.yml/badge.svg)](https://github.com/flatironinstitute/sciware-testing-python/actions)
[![codecov](https://codecov.io/gh/jamesETsmith/sciware-testing-python/branch/main/graph/badge.svg?token=4z1jy9YqIV)](https://codecov.io/gh/jamesETsmith/sciware-testing-python)

This is an example repository for writing tests, for the Sciware Testing session. 
It demonstrates how to setup a repository to use GitHub actions to automatically run tests
on the code.

- [Materials](https://github.com/flatironinstitute/learn-sciware-dev/tree/master/14_TestingPackaging)
- [Workshop guide](https://flatironinstitute.github.io/learn-sciware-dev/14_TestingPackaging/guide.html)

## Quick-start

### Prerequisites

- python3 with pip3 (with optional virtualenv or conda)

### Install

```bash
git clone https://github.com/flatironinstitute/sciware-testing-python.git
cd sciware-testing-python
pip3 install -e .
```

This will work with a virtualenv, conda, or on a personal machine.
With a system python, you may need `pip3 install --user -e .`.
This will also install dependencies (like `pytest`) specified in [`requirements.txt`](requirements.txt).

The `-e` indicates that we want to continue developing (editing) the installed package.

### Run tests

```bash
pytest
```

## Forking This Project

If you fork this project you should do the following things to make sure that your fork is correctly linked to your GitHub account:

1.  If you haven't linked your GitHub account to [`codecov`](https://about.codecov.io/), do so now.
2.  Change the badge URL at the top of `README.md` to point to your GitHub workflow build. To do this, replace `flatironinstitute` with your GitHub handle in the URLs of the badge.
3.  Change the badge URL at the top of `README.md` to point to your [`codecov`](https://about.codecov.io/) report. Go to [`codecov`](https://about.codecov.io/), navigate to the `sciware-testing-python` project, then go to Settings > Badge.
4.  Change your [`codecov`](https://about.codecov.io/) token in your GitHub actions file (in `.github/workflows`). To get your token go to [`codecov`](https://about.codecov.io/), navigate to the `sciware-testing-python` project, then go to Settings > General > `Repository Upload Token`. Copy this token and use it to set the `CODECOV_TOKEN` variable in `.github/workflows`.

## Contents

* **[`README.md`](README.md)** - File generating this page
* **[`setup.py`](setup.py)** - File describing the metadata for the package and rules to build/install/test it
* **[`requirements.txt`](requirements.txt)** - File listing the packages required to run the code. It is included by setup.py
* **[`LICENSE`](LICENSE)** - File containing the text of the license the code is released under. Having a license file allows other people to use the code
* **[`sciware_testing_python/`](sciware_testing_python/)** - Directory for all the code
* **[`sciware_testing_python/__init.py__`](sciware_testing_python/__init__.py)** - File that python imports to define the `sciware_testing_python` package
* **[`sciware_testing_python/exercise.py`](sciware_testing_python/exercise.py)** - File with all of the code to fill in
* **[`sciware_testing_python/examples.py`](sciware_testing_python/exercise.py)** - Example working solutions
* **[`tests/`](tests/)** - Directory for the code which tests the code in `sciware_testing_python`
* **[`tests/test_exercise.py`](tests/test_1.py)** - File to fill in with some tests
* **[`tests/test_examples.py`](tests/test_examples.py)** - File containing some tests
* **[`.gitignore`](.gitignore)** - File which tells github what files to not track (optional)
* **[`.github/workflows/`](.github/workflows/)** - Directory containing the configuration file for GitHub actions
* **[`.github/workflows/test.yml`](.github/workflows/test.yml)** - File detailing the system configurations to use for the tests.

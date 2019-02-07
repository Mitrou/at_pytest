#!/usr/bin/env bash
pytest -s -v -tb=line --alluredir=/tmp/my_allure_results  # report generated from root not from local path
allure serve /tmp/my_allure_results        # report generated

# pytest CLI arguments https://docs.pytest.org/en/latest/usage.html
# Getting help on version, option names, environment variables
pytest --version   # shows where pytest was imported from
pytest --fixtures  # show available builtin function arguments
pytest -h | --help # show help on command line and config file options
# Stopping after the first (or N) failures
pytest -x            # stop after first failure
pytest --maxfail=2    # stop after two failures
# Specifying tests / selecting tests
# Run tests in a module
pytest test_mod.py
# Run tests in a directory
pytest testing/
# Run tests by keyword expressions
pytest -k "MyClass and not method"
# Run tests by node ids
# To run a specific test within a module:
pytest test_mod.py::test_func
# Another example specifying a test method in the command line:
pytest test_mod.py::TestClass::test_method
# Run tests by marker expressions
# Will run all tests which are decorated with the @pytest.mark.slow decorator.
pytest -m slow
# Modifying Python traceback printing
pytest --showlocals # show local variables in tracebacks
pytest -l           # show local variables (shortcut)
pytest --tb=auto    # (default) 'long' tracebacks for the first and last
                    # entry, but 'short' style for the other entries
pytest --tb=long    # exhaustive, informative traceback formatting
pytest --tb=short   # shorter traceback format
pytest --tb=line    # only one line per failure
pytest --tb=native  # Python standard library formatting
pytest --tb=no      # no traceback at all
# Dropping to PDB (Python Debugger) on failures/start
pytest -x --pdb           # drop to PDB on first failure, then end test session
pytest --pdb --maxfail=3  # drop to PDB for first three failures
pytest --trace            # his will invoke the Python debugger at the start of every test.
# Creating a URL for a whole test session log
pytest --pastebin=all
1. Navigate the directory pytest and run the test package, as follows:

py.test test

2. Running a test package in verbose mode.

py.test -v test

3. Running a single test module within a package with the following command:

py.test -v test/test_module01.py

4. Run a specific test class as follows:

py.test -v test/test_module02.py::TestClass01

5. Run a specific test method as follows:

py.test -v test/test_module02.py::TestClass01::test_case01

6. Run a specific test function as follows:

py.test -v test/test_module01.py::test_case01


============================================

7. Running a test with following commands and compare output

py.test -v test_module03.py
py.test -vs test_module03.py

============================================

8. pytest Fixtures:
Pytest has its own set of fixtures that are flexible, extensible,
and modular. In the module test_module04.py, fixture01() is the
fixture function. It is because we are using the @pytest.fixture()
decorator with that. test_case01() is a test function that uses fixture01().
For that, we are passing fixture01 as an argument to test_case01().

9. If we want to run a block of code after the test with a fixture has run,
we have to add a finalizer function to the fixture.
The test_module07 demonstrates this idea.

10. The pytest provides access to the fixture information on the
requested object. The test_module08 demonstrates this concept.

11. Scope of pytest Fixtures:  The default scope of any fixture is the function level.
The following is the list of scopes for pytest fixtures:
• function: Runs once per test
• class: Runs once per class of tests
• module: Runs once per module
• session: Runs once per session

To use these, define them like this:
@pytest.fixture(scope="class")

12. The pytest.raises(Exception) checks if an exception is raised in the code.
If an exception is raised in the block of the code that include the exception,
the test passes; otherwise, it fails. The test_module09 demonstrates this concept.
In test_case01(), an exception is raised, so it passes. test_case02() does not raise
any exception, so it fails. This is extremely useful for testing negative scenarios.

13. Running py.test -h for help. It will display a list and usage of various command-line
options.

14. Stopping After the First (or N) Failures
We can stop the execution of tests after the first failure using the below command:
py.test -x

To stop execution after five failures use the below command:
py.test --maxfail=5

We can also change the argument provided to --maxfail.

15. You can use the py.test --durations=10 command to show the 10 slowest tests.

16. Generate JUnit-style XML log files in the current directory by running the following command:
py.test --junitxml=result.xml

17. Generate a plaintext result file in the current directory by running the following command:
py.test --resultlog=result.log

18. Send the entire execution log to an online remote pastebin service by running following command:
py.test -v --pastebin=all





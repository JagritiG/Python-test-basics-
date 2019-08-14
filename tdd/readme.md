Test Driven Development TDD:
TDD is a cycle where we
Step1- write the tests first
Step2- watch them fail and
Step3- then write the code to make the failed tests pass.

The concept is demonstrated in the following modules:

Step1- write test code in the module test_module01.py
(see code and run by using command: py.test -vs test_module01.py)

        class TestClass01:

                def test_case01(self):
                        calc = Calculator()
                        result = calc.add(2, 2)
                        assert 4 == result


Step2- watch them fail
While running test_module01, we get an error as:-
    NameError: name 'Calculator' is not defined

The problem is due to us not importing Calculator. We have not created Calculator
module yet!
    So, in the next step, define the Calculator module in the file calculator.py

Step3- write the code to make the failed tests pass

1. Define the Calculator module in the file calculator.py
and import Calculator in the test_module01.py

    class Calculator:

            def add(self, x, y):
                    pass

To make sure that there are no errors in calculator.py,
run the following command after every modification:

    python3 calculator.py

2. Import Calculator in the test_module01.py and run the test_module01.py

While running test_module01, we get an error as:-
    test_module01.py:9: AssertionError

(Now we are in second step again!)
The add() method returns the wrong value (i.e., pass), as it does not do anything
at the moment.

3. Let’s fix the code in the add() method in calculator.py

                class Calculator:

                        def add(self, x, y):
                                return x + y

    While running test_module01, we get
    test_module01.py::TestClass01::test_case01 PASSED


Note:  The pytest returns the line with the error in the test run
so we can decide what we need to change.

==================================================================================
Now, add another test case test_case02() in the test module test_module01.py and check
for more features:

(step1:write code)
        def test_case02(self):
                with pytest.raises(ValueError):
                        result = Calculator().add(2, 'two')

In the above code, we’re trying to add an integer and a string,
which should raise a ValueError exception.

(step2:watch it fail)
        While running test_module01, we get:-
        test_module01.py::TestClass01::test_case01 PASSED
        test_module01.py::TestClass01::test_case02 FAILED

        and an error:
        TypeError: unsupported operand type(s) for +: 'int' and 'str'

In the output, the second test fails as it does not detect a ValueError exception.
So, let’s add the provision to check if both the arguments are numeric,
else raise a ValueError exception.

(step3:Fix the development code)
class Calculator:

        def add(self, x, y):
                number_types = (int, float, complex)

                if isinstance(x, number_types) and isinstance(y, number_types):
                        return x + y

                else:
                        raise ValueError


        While running test_module01, we get:-
        test_module01.py::TestClass01::test_case01 PASSED
        test_module01.py::TestClass01::test_case02 PASSED



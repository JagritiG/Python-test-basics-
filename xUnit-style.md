The major architectural components of all xUnit-style test automation library:
==============================================================================
Test case class: This is the base class of all the test classes in the test modules.
                 All the test classes are derived from here.

Test fixtures: These are functions or methods that run before and after blocks of the test code execute.

Assertions: These functions or methods are used to check the behavior of the component being tested.
            Most of the xUnit-style frameworks are packed with powerful assertion methods.

Test suite: This is the collection or group of related tests that can be executed or scheduled to be
            executed together.

Test runner: This is the program or block of codes that runs the test suite.

Test result formatter: This formats the test results to produce the output of test execution in various
                       human readable formats like plaintext, HTML, and XML.

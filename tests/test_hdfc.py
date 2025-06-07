from docparser.hdfc import foo

def test_foo():
    assert foo() == "HDFC parsing functionality"

# A test that is expected to fail
# This is to demonstrate how to handle a failing test case
def failing_test():
    assert foo() == "This will fail"  # This test is intentionally failing to demonstrate failure handling

def test_failing_foo():
    try:
        failing_test()
    except AssertionError:
        assert True  # The test is expected to fail, so we catch the AssertionError and assert True
    else:
        assert False, "Expected AssertionError but none was raised"  # If no error is raised, the test fails

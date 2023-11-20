#  test_logging.py
from fastapi.testclient import TestClient

from pytest_bdd import scenarios, given, when, then

# Import the steps module
from features.steps import logging_steps

# Define the scenarios to be tested
scenarios("features/logging.feature")


# Define the test client fixture
def fastapi_app_running():
    return TestClient(logging_steps.app)


# Run the BDD tests
if __name__ == '__main__':
    import pytest

    pytest.main(["-sv", "test_logging.py"])


# from fastapi.testclient import TestClient
# from pytest_bdd import scenarios, given, when, then, parsers
#
# # Import the steps module
# from features.steps import logging_steps
#
# # Define the scenarios to be tested
# scenarios("features/logging.feature")
#
#
# # Define the test client fixture
# @given("the FastAPI application is running")
# def fastapi_app_running():
#     return TestClient(logging_steps.app)
#
#
#
# # Run the BDD tests
# if __name__ == '__main__':
#     import pytest
#
#     pytest.main(["-sv", "test_logging.py"])

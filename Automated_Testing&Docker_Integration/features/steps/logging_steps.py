#  features/steps/logging_steps.py:
import pytest
from behave import given, when, then
from fastapi.testclient import TestClient
from app.fastapi_app import app


@given("the FastAPI application is running")
def fastapi_app_running(context):
    context.client = TestClient(app)


@when('I make a POST request to "/register" with the following data:')
def make_post_request(context):
    url = "/register"  # Correct endpoint
    data = context.text
    context.response = context.client.post(url, json=data)


@then('the response status code should be {status_code}')
def check_response_status_code(context, status_code):
    assert context.response.status_code == int(status_code)


@then('the response body should contain {expected_body}')
def check_response_body(context, expected_body):
    assert context.response.json() == expected_body

# from behave import given, when, then
# from fastapi.testclient import TestClient
# from app.fastapi_app import app
#
#
# @given("the FastAPI application is running")
# def fastapi_app_running(context):
#     context.client = TestClient(app)
#
#
# @when('I make a POST request to "/run_test" with the following data:')
# def make_post_request(context):
#     url = "http://localhost:8080/run_test"  # Use the correct endpoint
#     data = context.text
#     context.response = context.client.post(url, json=data)
#
#
# @then('the response status code should be {status_code}')
# def check_response_status_code(context, status_code):
#     assert context.response.status_code == int(status_code)
#
#
# @then('the response body should contain {expected_body}')
# def check_response_body(context, expected_body):
#     assert context.response.json() == expected_body

# from behave import given, when, then
# from fastapi.testclient import TestClient
# from app.fastapi_app import app
#
#
# # @given("the FastAPI application Spring Boot server are running")
# # def fastapi_app_running(context):
# #     context.client = TestClient(app)
#
# @given("the FastAPI application is running")
# def fastapi_app_running(context):
#     context.client = TestClient(app)
#
# @when('I make a POST request to "{endpoint}" with the following data:')
# def make_post_request(context, endpoint):
#     url = "http://localhost:8080/run_test"
#     data = context.text
#     context.response = context.client.post(url, json=data)
#
#
# @then('the response status code should be {status_code}')
# def check_response_status_code(context, status_code):
#     assert context.response.status_code == int(status_code)
#
#
# @then('the response body should contain {expected_body}')
# def check_response_body(context, expected_body):
#     assert context.response.json() == expected_body

# from pytest_bdd import given, when, then
# from fastapi.testclient import TestClient
# from main import app
# import requests
# import pytest
#
# # Define the test client fixture
# @pytest.fixture
# def test_client():
#     return TestClient(app)
#
# # Define the given step
# @given("the Spring Boot server is running")
# def spring_boot_server_running():
#     # Mock the requests.get method to simulate the Spring Boot server running
#     def mock_get(url):
#         assert url == "http://localhost:8080/health"
#         response = requests.Response()
#         response.status_code = 200
#         return response
#
#     requests.get = mock_get
#
# # Define when step
# @when("I register a profile with the name {full_name}")
# def register_profile(test_client, full_name):
#     response = test_client.post("/register", json={"fullName": full_name})
#     return response
#
# # Define then step
# @then("the registration should be successful with a message containing {expected_message}")
# def check_registration_response(response, expected_message):
#     assert response.status_code == 200
#     assert expected_message in response.text
#
#
#
# # import requests
# # from behave import given, when, then
# #
# # @given("the Spring Boot server is running")
# # def step_given_spring_boot_running(context):
# #     # Mock the requests.post method to simulate the Spring Boot server running
# #     def mock_post(url, json_data):
# #         assert url == "http://localhost:8080/register"
# #         assert json_data == {"fullName": "John Doe"}  # Adjust the expected data accordingly
# #         response = requests.Response()
# #         response.status_code = 200
# #         return response
# #
# #     requests.post = mock_post
# #
# # @when('I make a POST request to "{endpoint}" with the following data:')
# # def step_when_make_post_request(context, endpoint):
# #     url = f"http://localhost:8000{endpoint}"  # Adjust the port if needed
# #     data = context.text
# #     context.response = requests.post(url, json=data)
# #
# # @then('the registration should be successful with a message containing "{expected_message}"')
# # def step_then_check_registration_response(context, expected_message):
# #     assert context.response.status_code == 200
# #     assert expected_message in context.response.text

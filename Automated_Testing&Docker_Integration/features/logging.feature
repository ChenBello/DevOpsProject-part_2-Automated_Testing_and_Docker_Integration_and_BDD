# features/register_profile.feature:

Feature: Logging Functionality
  Scenario: Successful user registration
    Given the FastAPI application is running
    When I make a POST request to "/register" with the following data:
      """
      {
        "fullName": "John Doe"
      }
      """
    Then the response status code should be 200
    And the response body should contain {"mocked_key": "mocked_value"}


#Feature: Logging Functionality
#
#  Scenario: Successful user registration
#    Given the FastAPI application is running
#    When I make a POST request to "/run_test" with the following data:
#      """
#      {
#        "test_script": "dummy_script"
#      }
#      """
#    Then the response status code should be 200
#    And the response body should contain {"mocked_key": "mocked_value"}

#Feature: Profile Registration
#
#  Scenario: Successful profile registration
#    Given the FastAPI application Spring Boot server are running"
#    When I register a profile with the name "John Doe"
#    Then the registration should be successful with a message containing "Successfully registered profile: John Doe"
#


#
#Feature: Logging Functionality
#
#  Scenario: Successful user registration
#    Given the FastAPI application is running
#    When I make a POST request to "/run_test" with the following data:
#      """
#      {
#        "test_script": "dummy_script"
#      }
#      """
#    Then the response status code should be 200
#    And the response body should contain {"mocked_key": "mocked_value"}
#
#
#

#Feature: Logging Functionality
#
#  Scenario: Successful user registration
#    Given the Spring Boot server is running
#    When I register a profile with the name "John Doe"
#    Then the registration should be successful with a message containing "Successfully registered profile: John Doe"
#
#
##Feature: User Registration
##
##Scenario: Registering a user
##    Given the Spring Boot server is running
##    When I make a POST request to "/register" with the following data:
##        """
##        {
##          "fullName": "John Doe"
##        }
##        """
##    Then the registration should be successful with a message containing "Successfully registered profile: John Doe"
##
#
#
##Feature: Logging Functionality
##
##  Scenario: Accessing the root endpoint
##    Given the FastAPI application is running
##    When I make a GET request to "/"
##    Then the response status code should be 200
##    And the response body should contain {"Hello": "World"}
##
##  Scenario: Logging is working
##    Given the Spring Boot server is running
##    When I make a request to the FastAPI logging endpoint
##    Then the response should contain the log message "Hello, World!"

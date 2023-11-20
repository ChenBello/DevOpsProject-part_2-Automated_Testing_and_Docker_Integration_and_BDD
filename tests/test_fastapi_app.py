# pip install pytest
# pip install fastapi uvicorn pytest
# pip install --upgrade httpcore httpx

# test_pastapi_app.py:

import requests
from fastapi.testclient import TestClient
import pytest
from app.fastapi_app import app


@pytest.fixture
def test_client():
    return TestClient(app)


def test_register_profile(test_client, monkeypatch):
    # Mock the requests.post method to simulate interaction with Spring Boot
    def mock_post(url, json):
        assert url == "http://localhost:8080/register"
        assert json["fullName"] == "John Doe"

        # Create a mock response with a valid status code (e.g., 200) and HTML content
        response = requests.Response()
        response.status_code = 200
        response._content = b'<html><head></head><body><p>Successfully registered profile: John Doe</p></body></html>'

        return response

    monkeypatch.setattr(requests, 'post', mock_post)

    # Simulate registering a profile and interacting with the Spring Boot server
    response = test_client.post("/register", json={"fullName": "John Doe"})

    assert response.status_code == 200
    assert "Successfully registered profile: John Doe" in response.text

# import pytest
# from fastapi.testclient import TestClient
# from httpx import AsyncClient
#
# from app.fastapi_app import app
#
# @pytest.fixture
# def test_client():
#     return TestClient(app)
#
# @pytest.mark.asyncio
# async def test_run_test_success(test_client):
#     # Mock the Spring Boot server using httpx
#     async with AsyncClient() as client:
#         await client.post("http://localhost:8080/run_test", json={"test_script": "dummy_script"}, status_code=200)
#
#     # Make a request to the FastAPI endpoint
#     response = await test_client.post("/run_test", json={"test_script": "dummy_script"})
#
#     # Check if the response is successful
#     assert response.status_code == 200
#     assert response.json() == {"mocked_key": "mocked_value"}  # Adjust the expected response as needed

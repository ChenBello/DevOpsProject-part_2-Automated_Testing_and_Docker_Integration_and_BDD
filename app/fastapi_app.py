# pip install fastapi uvicorn
# pip install jinja2
#  app/fastapi_app.py:
from fastapi import FastAPI, HTTPException
from fastapi.responses import HTMLResponse
from pydantic import BaseModel
import requests
import logging

app = FastAPI(debug=True)

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


class ProfileRequest(BaseModel):
    fullName: str


@app.post("/register", response_class=HTMLResponse)
async def register_profile(profile_request: ProfileRequest):
    # Simulate interaction with the Spring Boot server
    spring_boot_url = "http://localhost:8080/register"

    # Prepare data to send to Spring Boot server
    data = {
        "fullName": profile_request.fullName,
    }

    try:
        # Make a POST request to the Spring Boot server
        response = requests.post(spring_boot_url, json=data)
        response.raise_for_status()  # Raise an exception for HTTP errors

        # Log the successful interaction
        logger.info(f"Successfully registered profile: {profile_request.fullName}")

        # If successful, return a simple HTML response
        return HTMLResponse(
            content=f"<html><head></head><body><p>Successfully registered profile: {profile_request.fullName}</p></body></html>")

    except requests.RequestException as e:
        # Log the error
        logger.error(f"Error interacting with Spring Boot server: {str(e)}")

        # Raise an HTTPException with a custom error message
        raise HTTPException(status_code=500, detail="Internal server error during registration")

# from fastapi import FastAPI, HTTPException
# from fastapi.responses import HTMLResponse
# from pydantic import BaseModel
# import requests
# import logging
#
# app = FastAPI(debug=True)
#
# # Configure logging
# logging.basicConfig(level=logging.INFO)
# logger = logging.getLogger(__name__)
#
#
# class ProfileRequest(BaseModel):
#     fullName: str
#
#
# @app.post("/register", response_class=HTMLResponse)
# async def register_profile(profile_request: ProfileRequest):
#     # Simulate interaction with the Spring Boot server
#     spring_boot_url = "http://localhost:8080/register"
#
#     # Prepare data to send to Spring Boot server
#     data = {
#         "fullName": profile_request.fullName,
#     }
#
#     try:
#         # Make a POST request to the Spring Boot server
#         response = requests.post(spring_boot_url, json=data)
#         response.raise_for_status()  # Raise an exception for HTTP errors
#
#         # Log the successful interaction
#         logger.info(f"Successfully registered profile: {profile_request.fullName}")
#
#         # If successful, return a simple HTML response
#         return HTMLResponse(content=f"<html><head></head><body><p>Successfully registered profile: {profile_request.fullName}</p></body></html>")
#
#     except requests.RequestException as e:
#         # Log the error
#         logger.error(f"Error interacting with Spring Boot server: {str(e)}")
#
#         # Raise an HTTPException with a custom error message
#         raise HTTPException(status_code=500, detail="Internal server error during registration")
#


# # pip install fastapi httpx pytest pytest-bdd
# from fastapi import FastAPI, HTTPException
# import httpx
# # p
# # ip install -r requirements.txt --use-deprecated=legacy-resolver
# app = FastAPI()
#
# @app.post("/run_test")
# async def run_test(test_script: str):
#     try:
#         # Assuming the Spring Boot server is running on http://localhost:8080
#         spring_boot_url = "http://localhost:8080/run_test"
#
#         # Prepare data to send to the Spring Boot server
#         data = {"test_script": test_script}
#
#         # Make a POST request to the Spring Boot server using httpx
#         async with httpx.AsyncClient() as client:
#             response = await client.post(spring_boot_url, json=data)
#             response.raise_for_status()  # Raise an exception for HTTP errors
#
#         # Log the successful interaction
#         print(f"Successfully ran test script: {test_script}")
#
#         # If successful, return the response from the Spring Boot server
#         return response.json()
#
#     except httpx.RequestError as e:
#         # Log the error
#         print(f"Error interacting with Spring Boot server: {str(e)}")
#
#         # Raise an HTTPException with a 500 status code
#         raise HTTPException(status_code=500, detail="Internal server error during test execution")

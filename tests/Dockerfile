# Use an official Python runtime as a parent image
FROM python:3.9

# Set the working directory in the container
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app

# Install any needed packages specified in requirements.txt
RUN pip install -r requirements.txt

# Run pytest when the container launches
CMD ["pytest", "-sv", "C:\Users\chenb\PycharmProjects\Automated_Testing&Docker_Integration\tests"]

#cd tests
#docker-compose up --build test-runner

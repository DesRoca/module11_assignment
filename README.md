# IS601 Module 11: Assignment-Implement and Test a Calculation Model with Optional Factory Pattern

## Objective
For this assignment, I defined a Calculation model using SQLAlchemy and create robust validation with Pydantic schemas. I also implemented a factory pattern for extensibility and reinforce my CI/CD pipeline by testing the new functionality.

## My Github Repository
https://github.com/DesRoca/module11_assignment

## My Github Actions Workflow
https://github.com/DesRoca/module11_assignment/actions

## My DockerHub Image
https://hub.docker.com/repository/docker/desroca/601_module9/tags/54f2035041930deae3b505919e9d215423aa3692/sha256:c63bc4040d9f9164c4c9f5733206871ce8d062b30aea4835ea1c41d833edd414

# Instructions

## Running Tests Locally

### Prerequisites
- Python 3.12
- PostgreSQL
- Docker Desktop
- Git

1. Clone the repository

git clone https://github.com/DesRoca/module11_assignment/actions
cd module10_assignment

2. Create and activate a virtual environment

python3 -m venv venv
source venv/bin/activate

3. Install dependencies

python -m pip install --upgrade pip
pip install -r requirements.txt

4. Configure the database

Make sure your PostgreSQL database is running and the DATABASE_URL environment variable is configured correctly.

Example database connection string:

DATABASE_URL=postgresql://postgres:postgres@localhost:5432/fastapi_db

Update the connection string to match your local PostgreSQL configuration.

5. Run the tests

Run the complete test suite:

pytest

To run individual test categories:

Unit tests:

pytest -vv --tb=short tests/unit/

Integration tests:

pytest -vv --tb=short tests/integration/

End-to-end tests:

pytest -vv -s --tb=short tests/e2e/

Integration and end-to-end tests require the appropriate database and application dependencies to be running.

### Docker Hub

The Docker image is automatically built and deployed to Docker Hub through the GitHub Actions workflow after successful testing and security scanning on the main branch.

### Docker Hub Repository:

https://hub.docker.com/r/desroca/601_module9

Pull the latest image using:

docker pull desroca/601_module9:latest


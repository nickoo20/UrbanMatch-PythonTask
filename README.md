# UrbanMatch-PythonTask
# FastAPI MatchMatching API

This project is a Matchmaking API built using FastAPI. The API allows for creating, reading, updating, and deleting user profiles. It also includes functionality to find user matches based on city and interests.

## Assumptions Made

- The `interests` field accepts a string rather than a list of strings.
- Email validation is enforced using Pydantic's `EmailStr`.
- The `gender` field is assumed to be a string.
- The `age` field is assumed to be an integer.
- The `city` field is assumed to be a string.

## Project Structure

- `main.py`: The main FastAPI application file containing route definitions.
- `models.py`: SQLAlchemy models for the User entity.
- `schemas.py`: Pydantic models for request and response validation.
- `database.py`: Database setup and session creation.
- `requirements.txt`: Dependencies for the project.

## Requirements

- Python 3.7+
- FastAPI
- SQLAlchemy
- Pydantic
- SQLite (or any preferred SQL database)
- Uvicorn

## Setup

1. **Clone the repository:**
    ```sh
    git clone <repository_url>
    cd <repository_directory>
    ```

2. **Create and activate a virtual environment:**
    ```sh
    python -m venv env
    source env/bin/activate  # On Windows, use `env\Scripts\activate`
    ```

3. **Install dependencies:**
    ```sh
    pip install -r requirements.txt
    ```

4. **Run the application:**
    ```sh
    uvicorn main:app --reload
    ```

## Usage

### Endpoints

- **GET /users/**
    - Retrieve all users.
    - Response: List of user profiles.

- **POST /users/**
    - Create a new user.
    - Request body: JSON object containing `email`, `name`, `age`, `gender`, `city`, and `interests`.
    - Response: Created user profile.

- **GET /users/{user_id}**
    - Retrieve a specific user by ID.
    - Response: User profile.

- **PUT /users/{user_id}**
    - Update an existing user by ID.
    - Request body: JSON object containing any of the fields `email`, `name`, `age`, `gender`, `city`, or `interests`.
    - Response: Updated user profile.

- **DELETE /users/{user_id}**
    - Delete a user by ID.
    - Response: Confirmation message.

- **GET /users/{user_id}/matches**
    - Find matches for a user based on city and interests.
    - Response: List of matching user profiles.

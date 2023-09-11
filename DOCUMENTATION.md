# HNGx Backend Stage 2 Task API Documentation

### Introduction

Welcome to the documentation for the My Awesome API. This API allows you to perform CRUD (Create, Read, Update, Delete) operations on user profiles.

## API Endpoints
#### Create a Person Profile
Endpoint: POST /api

##### Request Format:
`{
    "name": "John Doe"
}`

##### Response Format:
    {
        "status": true,
        "message": "Person data added.",
        "data": {
            "user_id": 1,
            "name": "John Doe",
            "created_on_date": "2023-09-09",
            "create_on_time": "12:30:45"
        }
    }

#### Get Person Profile
Endpoint: GET /api/{user_id}

##### Request Format: 
`No request body required.`

##### Response Format:
    {
        "status": true,
        "message": "Person data retrieved.",
        "data": {
            "user_id": 1,
            "name": "John Doe",
            "created_on_date": "2023-09-09",
            "create_on_time": "12:30:45"
        }
    }

#### Update Person Profile
Endpoint: PATCH /api/{user_id}

##### Request Format:
    {
        "name": "Updated Name"
    }

##### Response Format:
    {
        "status": true,
        "message": "Person with user_id 1 updated successfully."
    }

#### Delete Person Profile
Endpoint: DELETE /api/{user_id}

##### Request Format: 
    No request body required.

##### Response Format:
    {
        "status": true,
        "message": "Person with user_id 1 has been deleted successfully."
    }

## Sample Usage
### Creating a Person Profile
##### Request:

###### POST /api
    Content-Type: application/json

    {
        "name": "Jane Smith"
    }

#### Response:
    HTTP/1.1 201 Created
    {
        "status": true,
        "message": "Person data added.",
        "data": {
            "user_id": 2,
            "name": "Jane Smith",
            "created_on_date": "2023-09-09",
            "create_on_time": "13:45:22"
        }
    }

### Getting Personal Profile
#### Request:
`GET /api/2`
#### Response:
    HTTP/1.1 200 OK
    {
        "status": true,
        "message": "Person data retrieved.",
        "data": {
            "user_id": 2,
            "name": "Jane Smith",
            "created_on_date": "2023-09-09",
            "create_on_time": "13:45:22"
        }
    }


# Limitations and Assumptions
*The API assumes that person profiles are identified by unique numeric IDs.
This documentation covers the basic functionality of the API and does not include advanced features like authentication and authorization as the project does not require that.*

## Local Setup

*To set up and run the API locally:*

- Clone the repository from GitHub.
- Install the required dependencies using `pip install -r requirements.txt`.
- Create and apply the database migrations using `python manage.py makemigrations` and `python manage.py migrate`.
- Run the development server with `python manage.py runserver`.

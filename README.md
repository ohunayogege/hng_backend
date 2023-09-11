# HNGx Backend Stage 2 Task API Documentation

Welcome to the documentation for the HNGx Backend Stage 2 Task API. This API allows you to perform CRUD (Create, Read, Update, Delete) operations on person profiles.

## Table of Contents

- [Prerequisites](#prerequisites)
- [Getting Started](#getting-started)
  - [Installation](#installation)
  - [Database Setup](#database-setup)
- [Running the API](#running-the-api)
- [API Endpoints](#api-endpoints)
  - [Create a Person Profile](#create-a-person-profile)
  - [Get Person Profile](#get-person-profile)
  - [Update Person Profile](#update-person-profile)
  - [Delete Person Profile](#delete-person-profile)
- [Sample Usage](#sample-usage)
- [Limitations and Assumptions](#limitations-and-assumptions)

## Prerequisites

Before you begin, ensure you have met the following requirements:

- Python 3.x installed.
- Pip package manager installed.
- A code editor (e.g., VSCode) for development.
- Postman or a similar tool for API testing.

## Getting Started

### Installation

1. Clone the repository:

   ```bash
    git clone https://github.com/ohunayogege/hng_backend.git
    cd hng_backend
2. Create a virtual environment (recommended):
   ```bash
   python -m venv venv
3. Activate the virtual environment:
   ```bash
   - On Windows:
   venv\Scripts\activate
   
   - On macOS and Linux:
   source venv/bin/activate

4. Install the required dependencies:
    `pip install -r requirements.txt`

### Database Setup
    python manage.py makemigrations
    python manage.py migrate

### Running the API
*To run the API locally, use the following command:*
    `python manage.py runserver`

*The API will be available at http://localhost:8000/.*

### API Endpoints

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

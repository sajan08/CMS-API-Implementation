Content Management System (CMS) API

This project is a backend implementation for a Content Management System (CMS) using Django and Django REST Framework (DRF). The CMS API supports content creation, management, and authentication for two types of users: Admin and Author.


---

Features

1. User Roles:

Admin: Can manage (view, edit, delete) all content.

Author: Can manage their own content only.



2. Authentication:

Token-based authentication using Simple JWT.



3. Content Management:

Create, Read, Update, Delete (CRUD) content.

Content includes title, body, summary, categories, and PDF document upload.



4. Search Functionality:

Search content by title, body, summary, or categories.



5. Validations:

User and content fields are validated (e.g., email, password strength, PDF-only uploads).



6. Test Cases:

Unit tests for all key features using Django's TestCase.





---

Requirements

Python 3.8 or higher

Django 4.x

Django REST Framework (DRF)

Simple JWT for authentication



---

Setup Instructions

1. Clone the Repository

git clone <repository_url>
cd cms_project

2. Set Up Virtual Environment

Create and activate a virtual environment:

python -m venv venv
source venv/bin/activate  # For Linux/Mac
venv\Scripts\activate     # For Windows

3. Install Dependencies

Install required Python libraries:

pip install -r requirements.txt

4. Apply Migrations

Run the following commands to set up the database:

python manage.py makemigrations
python manage.py migrate

5. Seed Admin User

To create a default admin user for testing, run:

python manage.py createsuperuser

6. Run the Server

Start the development server:

python manage.py runserver

The API will be available at: http://127.0.0.1:8000/api/


---

API Endpoints

Authentication

Login (Obtain Token): POST /api/token/

Refresh Token: POST /api/token/refresh/


Content Management

Get All Content: GET /api/contents/

Create Content: POST /api/contents/

Update Content: PUT /api/contents/<id>/

Delete Content: DELETE /api/contents/<id>/


Example Payloads

Create Content

{
  "title": "Sample Title",
  "body": "This is a sample body.",
  "summary": "This is a summary.",
  "categories": [1, 2],
  "document": "path/to/document.pdf"
}

Future Enhancements

Add filtering and sorting for content.

Implement frontend integration.

Enhance unit test coverage.

Add detailed logs for API calls.


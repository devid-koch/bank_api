# Bank API Service

This project provides a REST API service to get the list of banks and their branch details. The API is built using Django and Django REST Framework.

## Setup Instructions

### Prerequisites

- Python 3.x
- Django 3.x
- Django REST Framework
- PostgreSQL (or any other preferred database)

### Project Setup

1. **Clone the Repository:**

   ```sh
   git clone https://github.com/devid-koch/bank_api
   cd bank_api

2. **Install Dependencies:**
    pip install -r requirements.txt

3. **Configure the Database:**
    Update the DATABASES settings in bank_api/settings.py to configure your database.

    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.postgresql',
            'NAME': 'your_db_name',
            'USER': 'your_db_user',
            'PASSWORD': 'your_db_password',
            'HOST': 'localhost',
            'PORT': '',
        }
    }

4. **Run Migrations:**
    python manage.py migrate

5. **Create a Superuser:**
    python manage.py createsuperuser

6. **Populating Initial Data**
    To populate the database with initial data, you can use the Django admin interface or a custom script.

    **Method 1: Using Django Admin Interface**
    ### Run the Development Server:
    python manage.py runserver
    ### Access the Admin Interface:
    Go to http://127.0.0.1:8000/admin and log in with the superuser credentials.
    ### Add Banks and Branches:
    Use the admin interface to add Bank and Branch entries.

    **Method 2: Using a Script**
    Create a Script (populate_data.py) in the Project Directory:
    {I have created the populate_data.py script}
    
    Run the Script:
    python populate_data.py

    **Testing the API**
    Using Postman or any preferred software 
    Get the list of banks:

    Request Type: GET
    URL: http://127.0.0.1:8000/api/banks/
    
    Get branch details by IFSC code:

    Request Type: GET
    URL: http://127.0.0.1:8000/api/branches/SBIN0000001/ (replace SBIN0000001 with the actual IFSC code you want to test)

    **Running Tests**
    Run the tests using Django's test command:
    python manage.py test banks

    **Conclusion**
    This project provides a REST API service for managing banks and their branches. The API is built using Django and Django REST Framework, with endpoints to get the list of banks and branch details for a specific branch. The database can be populated with initial data using the Django admin interface or a custom script. The API has been tested using Postman and automated test cases.
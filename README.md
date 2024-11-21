This project is a REST API for managing a library of books. The API provides the following features:

Features

1. CRUD Operations for Books

	•	Add a new book.
	•	Retrieve a list of all books (with filtering options).
	•	View details of a single book.
	•	Update book information.
	•	Delete a book.

2. Filtering and Search

	•	Filter books by author, genre, or publication year.
	•	Search for books by a partial title match.

3. Pagination

	•	Divide results into pages of 10 items each.

4. Authentication and Authorization

	•	Use token-based authentication (TokenAuthentication or JWT).
	•	Allow only authenticated users to perform CRUD operations.

5. Admin Access

	•	Only administrators can delete books.

6. API Documentation

	•	Automatically generate API documentation using Swagger

Installation and Setup

Prerequisites

Make sure you have Python and Git installed.

1. Clone the Repository

Run the following command to clone the repository:
-- 
git clone https://github.com/vladduucckk/restapi-books
--

2. Create and Activate a Virtual Environment
--
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
--
3. Install Dependencies

Install the required dependencies from the requirements.txt file:
--
pip install -r requirements.txt
--
4. Run Migrations(if necessary)
--
python manage.py makemigrations
python manage.py migrate
--
API Documentation

•	The API documentation is available at /docs/ 

Testing

Run tests to ensure the API works as expected:
--
python manage.py test
--


## Gutenberg Book Collection API
This project is a Django-based API that provides a collection of books sourced from Project Gutenberg (https://www.gutenberg.org/), which is a free online resource of over 60,000 eBooks. This API allows you to search, filter, and explore the vast collection of books by various criteria.

## Features
Book Search: Search books by title, author, topic, language, or Gutenberg ID.
Filter Books: Supports filtering by author, topic, language, mime-type, and Gutenberg ID.
Pagination: The API supports pagination for listing books in chunks.
Case-insensitive partial matching for authors, topics, and titles.
## API Endpoints
### List all books:

URL: /api/books/
Method: GET
Description: Get a list of all books.
Search by Author:

URL: /api/books/?author=<author_name>
Method: GET
Example: /api/books/?author=homer
Search by Topic:

URL: /api/books/?topic=<topic_name>
Method: GET
Example: /api/books/?topic=relativity
Search by Language:

URL: /api/books/?language=<language_code>
Method: GET
Example: /api/books/?language=en
Search by Gutenberg ID:

URL: /api/books/?id=<gutenberg_id>
Method: GET
Example: /api/books/?id=6130
Multiple Search:

URL: /api/books/?author=<author_name>&topic=<topic_name>&language=<language_code>&id=<gutenberg_id>
Method: GET
Example: /api/books/?author=homer&topic=Relativity&language=en&id=6130
Example Responses
Book details will include:
Title
Author(s)
Language(s)
Subject(s)
Bookshelf(s)
Formats and MIME types available
## Project Setup
### Prerequisites
Before you begin, ensure that you have the following installed on your machine:

Python 3.8+
Django 3.x+
Docker (for containerization)
Docker Compose (for orchestrating containers)
Installation
Clone the repository:

git clone https://github.com/sbiju/gutenberg.git
cd gutenberg
Install dependencies: If you're using a virtual environment, activate it and install the requirements:

pip install -r requirements.txt
Build and start the Docker containers: For development setup using Docker, run:

docker compose up --build
Copy the data from dump files
Run the server: If you're using Docker, your app will be available at http://localhost:8000. You can access the API by visiting the appropriate endpoints.

For local Django setup:

python manage.py runserver
Environment Variables
You may need to configure environment variables for settings like the database. You can set them in a .env file or use environment variable configuration in your deployment.

## Deployment
This application is containerized using Docker, and it can be deployed on any cloud platform like AWS EC2. The following steps will deploy the application on AWS EC2.

## License
This project is licensed under the MIT License - see the LICENSE file for details.
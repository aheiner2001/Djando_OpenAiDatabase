# Overview

## Project Title:
API Calls to Retrieve Data from Database

## Project Description:
A project that uses Django and OpenAI API to fetch data from a database through API calls.

## Project Goals:
- Set up Django API for database interaction
- Use OpenAI API for chat functionality
- Implement CRUD operations

---

## Instructions for Build and Use

### Steps to build and/or run the software:

1. Clone the repository:
    ```bash
    git clone <repository-link>
    ```
2. Install dependencies:
    ```bash
    pip install -r requirements.txt
    ```
3. Set up the database:
    ```bash
    python manage.py migrate
    ```
4. Start the server:
    ```bash
    python manage.py runserver
    ```

### Instructions for using the software:

1. Go to `http://localhost:8000` in your browser.
2. Use API endpoints to interact with the app.

---

## Development Environment

Required software and libraries:
- **Python 3.x**
- **Django 3.x**
- **Django REST Framework**
- **OpenAI API**

---

## Useful Websites to Learn More
- [Django Documentation](https://www.djangoproject.com/start/)
- [Django REST Framework](https://www.django-rest-framework.org/)
- [OpenAI API Docs](https://beta.openai.com/docs/)

---

## Future Work

Things I plan to add or improve:
- [ ] Add better error handling
- [ ] Optimize OpenAI API integration
- [ ] Refactor code for scalability

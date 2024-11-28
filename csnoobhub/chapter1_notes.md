## Chapter 1: Initial Setup

### Summary
- **Python Installed**: Python 3 was installed using Homebrew.
- **Virtual Environment**: Set up and activated a virtual environment using `python3 -m venv env`.
- **Django Installed**: Installed Django version <insert version>.
- **Project Created**: Created a Django project named `csnoobhub`.
- **Server Running**: Verified the server is accessible at `http://127.0.0.1:8000/`.

### Key Commands Used
```bash
# Virtual Environment Setup
python3 -m venv env
source env/bin/activate

# Install Django
pip install django

# Start Project
django-admin startproject csnoobhub .
python manage.py runserver
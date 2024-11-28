## Chapter 2: Hello World App

### Key Concepts
- **HTTP Request/Response Cycle**:
  - Request: User requests `/hello/`.
  - URL Dispatcher: Matches `/hello/` to `hello_world` view.
  - View: Returns "Hello, World!" response.
  - Response: Sent back to the browser.

- **MVT Pattern**:
  - Model: Handles data (not used in this chapter).
  - View: Processes requests (e.g., `hello_world`).
  - Template: Defines HTML layout (not used in this chapter).

### Commands Used
```bash
# Create hello app
python manage.py startapp hello

# Define view
# hello/views.py
def hello_world(request):
    return HttpResponse("<h1>Hello, World!</h1>")

# URL configuration
# hello/urls.py
path('', views.hello_world, name='hello_world')

# Git commands
git add .
git commit -m "Chapter 2: Completed Hello World App"
git push
## Chapter 3: Pages App

### Key Concepts
- **Templates**: Used `home.html` for dynamic rendering.
- **Class-Based Views (CBVs)**: Implemented `HomePageView` with `TemplateView`.
- **URL Routing**: Connected `/` to `pages.urls` and `HomePageView`.

### Project Structure

### Commands Used
```bash
# Create pages app
python manage.py startapp pages

# Create and add templates
mkdir -p pages/templates/pages
touch pages/templates/pages/home.html

# Define CBV
# pages/views.py
class HomePageView(TemplateView):
    template_name = 'pages/home.html'

# Git Commands
git add .
git commit -m "Chapter 3: Added Pages App with Class-Based Views and Templates"
git push

#Chapter 3: Pages App

Key Concepts

	1.	Templates:
	•	Used home.html in templates/pages/ to dynamically render HTML for the homepage.
	2.	Class-Based Views (CBVs):
	•	Implemented HomePageView in views.py using Django’s TemplateView.
	•	CBVs improve modularity and reuse compared to Function-Based Views (FBVs).
	3.	URL Routing:
	•	Mapped the root URL (/) to HomePageView through pages/urls.py and csnoobhub/urls.py.

    #Deliverables

	1.	A functional Pages App with:
	•	Dynamic homepage rendered at /.
	•	Template-based content.
	•	Class-Based View for modularity.
	2.	GitHub Repository:
	•	Updated with Chapter 3 progress.
	•	Commit message: "Chapter 3: Added Pages App with Class-Based Views and Templates".
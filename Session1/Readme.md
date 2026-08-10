# Session 1 — Django Fundamentals

## Build Your First Web Application

Welcome to **Session 1** of the Django Web Development Bootcamp.

In this session, we will build the foundation of a **Student Management System** using Django.

You will start with an empty project directory and gradually build a working Django website with:

* A Home page
* An About page
* A Students page
* URL routing
* Django views
* HTML templates
* Template inheritance
* Bootstrap styling
* Navigation between pages

By the end of this session, you should understand the basic flow of a Django application:

```text
Browser
   ↓
URL
   ↓
View
   ↓
Template
   ↓
Response
   ↓
Browser
```

> **Important:** Database, Models, Forms, CRUD, Authentication, GitHub, and Deployment are intentionally outside the scope of Session 1. They will be introduced in later sessions.

---

# 📌 Start Here

If you are following this workshop for the first time, read this README from the top.

The expected workflow is:

```text
1. Prepare your environment
        ↓
2. Create a virtual environment
        ↓
3. Install Django
        ↓
4. Create the Django project
        ↓
5. Create the students app
        ↓
6. Configure URLs
        ↓
7. Create views
        ↓
8. Create templates
        ↓
9. Add template inheritance
        ↓
10. Add Bootstrap
        ↓
11. Build navigation
        ↓
12. Complete the challenge
        ↓
13. Review the checklist
```

**Do not worry if some of the concepts look unfamiliar at first. We will introduce them step by step.**

---

# 1. Session Overview

## Session

**Session 1 — Django Fundamentals**

## Duration

Approximately **3 hours**

## Project

**Student Management System**

## Difficulty

Beginner

## Main Goal

Build the foundation of a Django web application.

---

# 2. Session Schedule

The workshop is approximately three hours.

| Time        | Activity                         |
| ----------- | -------------------------------- |
| 00:00–00:10 | Welcome + project preview        |
| 00:10–00:25 | What is Django + MVT             |
| 00:25–00:40 | Setup + virtual environment      |
| 00:40–01:00 | Create Django project            |
| 01:00–01:20 | Create `students` app            |
| 01:20–01:30 | Break                            |
| 01:30–01:55 | URLs + Views                     |
| 01:55–02:20 | Templates                        |
| 02:20–02:40 | Template inheritance + Bootstrap |
| 02:40–02:50 | Challenge                        |
| 02:50–03:00 | Solution + recap                 |

> **Tip:** Don't rush through the commands. The purpose of this session is to understand how the pieces of Django fit together.

---

# 3. What We Are Building

Throughout the bootcamp, we will build a project called:

> **Student Management System**

The application will gradually become a real student management application.

### Session 1

We are building only the website foundation:

```text
Student Management System
│
├── Home
├── About
└── Students
```

### Session 2

We will introduce:

```text
Database
   ↓
Student Model
   ↓
Forms
   ↓
CRUD
```

### Session 3

We will introduce:

```text
Authentication
   +
GitHub
   +
Deployment
```

The important idea is:

> **We are building one application progressively across three sessions.**

---

# 4. Session 1 Learning Objectives

By the end of this session, you should be able to:

* Explain what Django is.
* Explain what a Django project is.
* Explain what a Django app is.
* Understand project vs app.
* Create a Django project.
* Create a Django app.
* Run the Django development server.
* Understand the purpose of `manage.py`.
* Understand the purpose of `settings.py`.
* Understand basic URL routing.
* Create Django views.
* Create HTML templates.
* Configure a project-level templates directory.
* Render templates from views.
* Use template inheritance.
* Use `{% extends %}`.
* Use `{% block %}`.
* Add Bootstrap using a CDN.
* Build navigation between pages.
* Understand the basic Django request/response cycle.
* Understand Django's MVT architecture at a beginner level.

---

# 5. What Is Django?

**Django** is a web framework written in Python.

A web framework provides tools and conventions that make it easier to build web applications.

Without a framework, you would need to handle many things yourself.

Django provides tools for:

* URL routing
* Handling requests
* Generating responses
* HTML templates
* Database interaction
* Forms
* Authentication
* Administration

We will learn these features gradually.

For Session 1, our main focus is:

```text
URLs
 ↓
Views
 ↓
Templates
```

---

# 6. What Is a Django Project?

A Django **project** is the overall configuration and structure of a Django website.

Our project will be called:

```text
config
```

The project contains configuration such as:

* Project settings
* Main URL configuration
* Server configuration

The project is not the same thing as an app.

---

# 7. What Is a Django App?

A Django **app** is a component of a Django project that handles a particular area of functionality.

Our app will be:

```text
students
```

It will eventually handle student-related functionality.

For example:

```text
Student Management System
│
├── students
├── accounts
├── reports
└── ...
```

A project can contain multiple apps.

For this bootcamp, we will start with one:

```text
students
```

---

# 8. Project vs App

This distinction is important.

| Django Project                  | Django App                     |
| ------------------------------- | ------------------------------ |
| Overall website configuration   | Specific area of functionality |
| Contains project settings       | Contains application logic     |
| Contains main URL configuration | Can contain app-specific URLs  |
| Can contain multiple apps       | Belongs to a project           |

### Simple analogy

Think about a university.

```text
University
│
├── Computer Engineering
├── Civil Engineering
├── Business
└── Management
```

The university is similar to the **Django project**.

The departments are similar to **Django apps**.

For our project:

```text
Student Management System
        │
        └── students app
```

---

# 9. Prerequisites

This workshop is designed for beginners.

You do not need previous Django experience.

### Recommended knowledge

Basic knowledge of:

* Python
* Functions
* Variables
* HTML
* CSS

### Not required

You do **not** need to know:

* Django
* SQL
* Databases
* React
* REST APIs
* Docker
* PostgreSQL

We will introduce the required concepts during the workshop.

---

# 10. Required Software

Before beginning, make sure you have:

| Software    | Purpose                     |
| ----------- | --------------------------- |
| Python 3    | Django programming language |
| VS Code     | Code editor                 |
| Web browser | Testing the application     |
| Git         | Optional in Session 1       |

---

# 11. Environment Setup

Open your terminal.

### Windows

You can use:

* PowerShell
* Command Prompt
* Windows Terminal

### macOS/Linux

Use Terminal.

---

# 12. Check Python

Run:

```bash
python --version
```

You should see something similar to:

```text
Python 3.11.x
```

The exact version may be different.

---

## Windows: Try `py` if `python` does not work

Run:

```bash
py --version
```

If this works, you can use:

```bash
py
```

instead of:

```bash
python
```

throughout the workshop.

For example:

```bash
py --version
```

or:

```bash
py manage.py runserver
```

---

# 13. Create the Project Directory

Choose where you want to store your project.

Run:

```bash
mkdir student-management
```

Then enter the directory:

```bash
cd student-management
```

Your current directory should now be:

```text
student-management/
```

---

# 14. Create a Virtual Environment

A **virtual environment** is an isolated Python environment for a project.

It allows a project to have its own Python packages.

Create one called `.venv`.

### Windows

```bash
python -m venv .venv
```

If you use `py`:

```bash
py -m venv .venv
```

### macOS/Linux

```bash
python3 -m venv .venv
```

After running the command, you should have:

```text
student-management/
└── .venv/
```

---

# 15. Activate the Virtual Environment

## Windows PowerShell

```powershell
.venv\Scripts\Activate.ps1
```

## Windows Command Prompt

```cmd
.venv\Scripts\activate
```

## macOS/Linux

```bash
source .venv/bin/activate
```

If successful, your terminal should show something similar to:

```text
(.venv)
```

For example:

```text
(.venv) C:\Users\Student\student-management>
```

This means your virtual environment is active.

---

# 16. Install Django

With the virtual environment activated:

```bash
python -m pip install django
```

Windows users using `py` can use:

```bash
py -m pip install django
```

Verify Django:

```bash
python -m django --version
```

You should see a Django version.

For example:

```text
5.x
```

The exact version may vary depending on when you install Django.

---

# 17. Create the Django Project

Now we are ready to create the project.

Run:

```bash
django-admin startproject config .
```

If `django-admin` is not available, use:

```bash
python -m django startproject config .
```

The final `.` is important.

It means:

> Create the Django project in the current directory.

---

# 18. Understand the Initial Project Structure

After creating the project:

```text
student-management/
│
├── manage.py
│
├── config/
│   ├── __init__.py
│   ├── settings.py
│   ├── urls.py
│   ├── asgi.py
│   └── wsgi.py
│
└── .venv/
```

---

# 19. Important Django Files

## `manage.py`

`manage.py` is the command-line tool for your Django project.

We will use it to run commands such as:

```bash
python manage.py runserver
```

and:

```bash
python manage.py startapp students
```

Think of it as the main command tool for your Django project.

---

## `settings.py`

Located at:

```text
config/settings.py
```

This contains project configuration.

Examples include:

* Installed apps
* Templates
* Database configuration
* Middleware
* Static files

We will modify this file during Session 1.

---

## `urls.py`

Located at:

```text
config/urls.py
```

This contains the main URL configuration.

It tells Django where to look when a browser requests a URL.

---

## `views.py`

Located at:

```text
students/views.py
```

This file will contain the Python functions that handle requests.

---

## Templates

Templates are HTML files that Django renders for the browser.

We will create:

```text
templates/
├── base.html
├── home.html
├── about.html
└── students/
    └── list.html
```

---

# 20. Run the Development Server

Before creating our app, let's make sure Django works.

Run:

```bash
python manage.py runserver
```

You should see:

```text
Starting development server at http://127.0.0.1:8000/
```

Open your browser:

```text
http://127.0.0.1:8000/
```

You should see the Django welcome page.

🎉 **Your first Django project is running!**

---

## Stop the server

In the terminal, press:

```text
Ctrl + C
```

---

# 21. Create the `students` App

Now create our application.

Run:

```bash
python manage.py startapp students
```

Django creates:

```text
students/
├── migrations/
├── __init__.py
├── admin.py
├── apps.py
├── models.py
├── tests.py
└── views.py
```

We will create one additional file ourselves:

```text
students/urls.py
```

---

# 22. Register the App

Creating an app does not automatically make Django use it.

We need to register it.

Open:

`config/settings.py`

Find:

```python
INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
]
```

Add:

```python
"students",
```

The complete section should now be:

`config/settings.py`

```python
INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",

    "students",
]
```

---

# 23. Create Your First View

A **view** is Python code that handles a request and returns a response.

Open:

`students/views.py`

Replace the contents with:

```python
from django.http import HttpResponse


def home(request):
    return HttpResponse("<h1>Welcome to Student Management System</h1>")
```

The important part is:

```python
def home(request):
```

This defines our view.

And:

```python
return HttpResponse(...)
```

returns a response to the browser.

---

# 24. Create App-Level URLs

Create:

`students/urls.py`

```python
from django.urls import path
from . import views


urlpatterns = [
    path("", views.home, name="home"),
]
```

This says:

> When the root URL of this app is requested, call the `home` view.

---

# 25. Connect App URLs to Project URLs

Now open:

`config/urls.py`

Replace its contents with:

```python
from django.contrib import admin
from django.urls import include, path


urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include("students.urls")),
]
```

The important line is:

```python
path("", include("students.urls")),
```

This tells Django:

> Send root-level URLs to the `students` app's URL configuration.

---

# 26. Test the First View

Start the server:

```bash
python manage.py runserver
```

Open:

```text
http://127.0.0.1:8000/
```

You should see:

```text
Welcome to Student Management System
```

Our first Django request/response cycle works!

---

# 27. Understanding the URL → View → Response Flow

When you visit:

```text
http://127.0.0.1:8000/
```

the process is:

```text
Browser
   ↓
/
   ↓
config/urls.py
   ↓
students/urls.py
   ↓
views.home()
   ↓
HttpResponse
   ↓
Browser
```

In simple terms:

```text
URL
 ↓
View
 ↓
Response
```

This is one of the most important concepts in Django.

---

# 28. Introducing Templates

Returning HTML directly from Python is possible:

```python
return HttpResponse("<h1>Hello</h1>")
```

But it becomes difficult to maintain when pages become larger.

Instead, Django lets us use **templates**.

A template is an HTML file that Django can render.

This gives us a cleaner separation:

```text
Python logic
    ↓
views.py

HTML
    ↓
templates/
```

---

# 29. Create the Templates Directory

At the project root, create:

```text
templates/
```

Your project should now contain:

```text
student-management/
│
├── manage.py
├── config/
├── students/
├── templates/
└── .venv/
```

---

# 30. Configure the Templates Directory

Open:

`config/settings.py`

Find:

```python
"DIRS": [],
```

Change it to:

```python
"DIRS": [BASE_DIR / "templates"],
```

The complete `TEMPLATES` section should be:

`config/settings.py`

```python
TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [BASE_DIR / "templates"],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]
```

Now Django knows where our project-level templates are located.

---

# 31. Render a Template from a View

We no longer need `HttpResponse`.

We can use Django's `render()` function.

Open:

`students/views.py`

Replace the file with:

```python
from django.shortcuts import render


def home(request):
    return render(request, "home.html")
```

Now the view says:

> Render `home.html` and return it to the browser.

---

# 32. Create the Home Template

Create:

`templates/home.html`

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">

    <title>Student Management System</title>
</head>

<body>

    <h1>Student Management System</h1>

    <p>
        Welcome to our Student Management System.
    </p>

</body>
</html>
```

Visit:

```text
http://127.0.0.1:8000/
```

You should now see the HTML page.

---

# 33. Create the About Page

Now we will create a second page.

First, add the view.

Open:

`students/views.py`

```python
from django.shortcuts import render


def home(request):
    return render(request, "home.html")


def about(request):
    return render(request, "about.html")
```

---

## Add the URL

Open:

`students/urls.py`

```python
from django.urls import path
from . import views


urlpatterns = [
    path("", views.home, name="home"),
    path("about/", views.about, name="about"),
]
```

---

## Create the Template

Create:

`templates/about.html`

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">

    <title>About - Student Management System</title>
</head>

<body>

    <h1>About</h1>

    <p>
        The Student Management System is a Django application
        developed as part of our Django Web Development Bootcamp.
    </p>

    <a href="/">Back to Home</a>

</body>
</html>
```

Visit:

```text
http://127.0.0.1:8000/about/
```

---

# 34. Create the Students Page

The Students page will initially be static.

The database will be introduced in Session 2.

Add the view.

`students/views.py`

```python
from django.shortcuts import render


def home(request):
    return render(request, "home.html")


def about(request):
    return render(request, "about.html")


def student_list(request):
    return render(request, "students/list.html")
```

---

## Add the URL

`students/urls.py`

```python
from django.urls import path
from . import views


urlpatterns = [
    path("", views.home, name="home"),
    path("about/", views.about, name="about"),
    path("students/", views.student_list, name="student-list"),
]
```

---

## Create the Template Directory

Create:

```text
templates/students/
```

Then create:

`templates/students/list.html`

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">

    <title>Students - Student Management System</title>
</head>

<body>

    <h1>Students</h1>

    <p>
        Student records will be displayed here in Session 2.
    </p>

</body>
</html>
```

Visit:

```text
http://127.0.0.1:8000/students/
```

---

# 35. Why Template Inheritance?

At this point, all three pages have their own:

```html
<!DOCTYPE html>
<html>
<head>
    ...
</head>
<body>
    ...
</body>
</html>
```

This creates duplication.

Imagine having 20 pages.

If you wanted to change the navigation bar, you would have to update 20 files.

Django solves this with **template inheritance**.

---

# 36. Create `base.html`

Create:

`templates/base.html`

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">

    <title>{% block title %}Student Management System{% endblock %}</title>
</head>

<body>

    <header>
        <h1>Student Management System</h1>
    </header>

    <main>
        {% block content %}
        {% endblock %}
    </main>

</body>
</html>
```

The important parts are:

```django
{% block title %}
{% endblock %}
```

and:

```django
{% block content %}
{% endblock %}
```

These create areas that child templates can customize.

---

# 37. Use `{% extends %}`

Now update the Home page.

Replace:

`templates/home.html`

with:

```html
{% extends "base.html" %}

{% block title %}
Home - Student Management System
{% endblock %}

{% block content %}

<h2>Welcome</h2>

<p>
    Welcome to the Student Management System.
</p>

<p>
    This application is being developed during our
    Django Web Development Bootcamp.
</p>

{% endblock %}
```

The first line:

```django
{% extends "base.html" %}
```

means:

> Use `base.html` as the parent template.

---

# 38. Update the About Page

Replace:

`templates/about.html`

with:

```html
{% extends "base.html" %}

{% block title %}
About - Student Management System
{% endblock %}

{% block content %}

<h2>About the Project</h2>

<p>
    The Student Management System is a Django application
    developed as part of our Django Web Development Bootcamp.
</p>

<p>
    In future sessions, this application will be connected
    to a database and will support student management operations.
</p>

<a href="/">Back to Home</a>

{% endblock %}
```

---

# 39. Update the Students Page

Replace:

`templates/students/list.html`

with:

```html
{% extends "base.html" %}

{% block title %}
Students - Student Management System
{% endblock %}

{% block content %}

<h2>Students</h2>

<p>
    Student records will be displayed here in Session 2.
</p>

{% endblock %}
```

Now all three pages share the same base layout.

---

# 40. Template Inheritance — Mental Model

Our templates now look like:

```text
base.html
│
├── home.html
├── about.html
└── students/list.html
```

The parent contains common structure.

The child templates provide page-specific content.

For example:

```text
base.html
│
├── Navbar
├── Page structure
├── CSS
│
└── {% block content %}
          ↑
          │
          ├── Home content
          ├── About content
          └── Students content
```

---

# 41. Add Bootstrap

We will use Bootstrap through a CDN.

We are **not** learning Bootstrap in depth today.

The purpose is simply to make our Django pages look cleaner while demonstrating how templates can use an external CSS framework.

Replace:

`templates/base.html`

with:

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">

    <title>{% block title %}Student Management System{% endblock %}</title>

    <link
        href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/css/bootstrap.min.css"
        rel="stylesheet"
    >
</head>

<body>

    <main class="container py-5">

        {% block content %}
        {% endblock %}

    </main>

</body>
</html>
```

Now Bootstrap is available to all templates extending `base.html`.

---

# 42. Build the Navigation Bar

Because the navigation should appear on every page, it belongs in `base.html`.

Replace:

`templates/base.html`

with:

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">

    <title>{% block title %}Student Management System{% endblock %}</title>

    <link
        href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/css/bootstrap.min.css"
        rel="stylesheet"
    >
</head>

<body>

    <nav class="navbar navbar-dark bg-dark">
        <div class="container">

            <a class="navbar-brand" href="{% url 'home' %}">
                Student Management System
            </a>

            <div>

                <a
                    class="btn btn-outline-light me-2"
                    href="{% url 'home' %}"
                >
                    Home
                </a>

                <a
                    class="btn btn-outline-light me-2"
                    href="{% url 'about' %}"
                >
                    About
                </a>

                <a
                    class="btn btn-outline-light"
                    href="{% url 'student-list' %}"
                >
                    Students
                </a>

            </div>

        </div>
    </nav>

    <main class="container py-5">

        {% block content %}
        {% endblock %}

    </main>

</body>
</html>
```

---

# 43. Understanding `{% url %}`

You may have noticed:

```django
{% url 'home' %}
```

and:

```django
{% url 'about' %}
```

These are Django template tags.

Instead of hard-coding:

```html
href="/about/"
```

we can use the URL's name:

```django
{% url 'about' %}
```

The name comes from:

`students/urls.py`

```python
path("about/", views.about, name="about"),
```

The URL name is:

```text
about
```

Similarly:

```python
path("", views.home, name="home"),
```

has the name:

```text
home
```

And:

```python
path("students/", views.student_list, name="student-list"),
```

has the name:

```text
student-list
```

---

# 44. Final `students/views.py`

At this point, your complete file should be:

`students/views.py`

```python
from django.shortcuts import render


def home(request):
    return render(request, "home.html")


def about(request):
    return render(request, "about.html")


def student_list(request):
    return render(request, "students/list.html")
```

---

# 45. Final `students/urls.py`

Your complete file should be:

`students/urls.py`

```python
from django.urls import path
from . import views


urlpatterns = [
    path("", views.home, name="home"),
    path("about/", views.about, name="about"),
    path("students/", views.student_list, name="student-list"),
]
```

---

# 46. Final `config/urls.py`

Your complete file should be:

`config/urls.py`

```python
from django.contrib import admin
from django.urls import include, path


urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include("students.urls")),
]
```

---

# 47. Final `templates/base.html`

Your complete file should be:

`templates/base.html`

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">

    <title>{% block title %}Student Management System{% endblock %}</title>

    <link
        href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/css/bootstrap.min.css"
        rel="stylesheet"
    >
</head>

<body>

    <nav class="navbar navbar-dark bg-dark">
        <div class="container">

            <a class="navbar-brand" href="{% url 'home' %}">
                Student Management System
            </a>

            <div>

                <a
                    class="btn btn-outline-light me-2"
                    href="{% url 'home' %}"
                >
                    Home
                </a>

                <a
                    class="btn btn-outline-light me-2"
                    href="{% url 'about' %}"
                >
                    About
                </a>

                <a
                    class="btn btn-outline-light"
                    href="{% url 'student-list' %}"
                >
                    Students
                </a>

            </div>

        </div>
    </nav>

    <main class="container py-5">

        {% block content %}
        {% endblock %}

    </main>

</body>
</html>
```

---

# 48. Final `templates/home.html`

`templates/home.html`

```html
{% extends "base.html" %}

{% block title %}
Home - Student Management System
{% endblock %}

{% block content %}

<div class="p-5 mb-4 bg-light rounded-3">

    <div class="container-fluid py-4">

        <h1 class="display-5 fw-bold">
            Student Management System
        </h1>

        <p class="col-md-8 fs-5">
            A Django web application being developed during
            our Django Web Development Bootcamp.
        </p>

        <a
            href="{% url 'student-list' %}"
            class="btn btn-primary btn-lg"
        >
            View Students
        </a>

    </div>

</div>

{% endblock %}
```

---

# 49. Final `templates/about.html`

`templates/about.html`

```html
{% extends "base.html" %}

{% block title %}
About - Student Management System
{% endblock %}

{% block content %}

<div class="row">

    <div class="col-md-8">

        <h1>About the Project</h1>

        <p class="lead">
            The Student Management System is a learning project
            built using Django.
        </p>

        <p>
            In Session 1, we are building the foundation of the
            application using Django views, URLs, templates,
            template inheritance, and Bootstrap.
        </p>

        <a
            href="{% url 'home' %}"
            class="btn btn-primary"
        >
            Back to Home
        </a>

    </div>

</div>

{% endblock %}
```

---

# 50. Final `templates/students/list.html`

`templates/students/list.html`

```html
{% extends "base.html" %}

{% block title %}
Students - Student Management System
{% endblock %}

{% block content %}

<div class="d-flex justify-content-between align-items-center mb-4">

    <div>

        <h1>Students</h1>

        <p class="text-muted mb-0">
            Student records will be introduced in Session 2.
        </p>

    </div>

</div>

<div class="alert alert-info">
    No student records are available yet.
    We will connect this page to a database in Session 2.
</div>

<a
    href="{% url 'home' %}"
    class="btn btn-primary"
>
    Back to Home
</a>

{% endblock %}
```

---

# 51. Final Project Structure

At the end of Session 1, your project should look like:

```text
student-management/
│
├── manage.py
│
├── config/
│   ├── __init__.py
│   ├── settings.py
│   ├── urls.py
│   ├── asgi.py
│   └── wsgi.py
│
├── students/
│   ├── migrations/
│   │   └── __init__.py
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── models.py
│   ├── tests.py
│   ├── urls.py
│   └── views.py
│
├── templates/
│   ├── base.html
│   ├── home.html
│   ├── about.html
│   └── students/
│       └── list.html
│
└── static/
    └── css/
        └── style.css
```

> The `.venv/` directory will also exist locally, but it should not be committed to Git.

---

# 52. Understanding MVT

Django commonly uses an architecture called **MVT**:

```text
M = Model
V = View
T = Template
```

## Model

The Model represents data.

For example, a future Student model might contain:

```text
Student
├── name
├── email
├── faculty
└── semester
```

We will **not** create this in Session 1.

Models belong to Session 2.

---

## View

The View contains Python logic.

Example:

```python
def home(request):
    return render(request, "home.html")
```

The view handles the request and decides what response should be returned.

---

## Template

The Template contains the HTML shown to the user.

For example:

```html
<h1>Student Management System</h1>
```

---

## Session 1 MVT Focus

For now:

```text
Browser
   ↓
URL
   ↓
View
   ↓
Template
   ↓
Response
   ↓
Browser
```

Later, we will add Models and databases.

---

# 53. Request/Response Cycle

Let's understand what happens when a user visits:

```text
/about/
```

### Step 1 — Browser sends a request

The browser requests:

```text
GET /about/
```

### Step 2 — Django checks the URLs

Django checks:

`config/urls.py`

which includes:

```python
path("", include("students.urls")),
```

Django then checks:

`students/urls.py`

and finds:

```python
path("about/", views.about, name="about"),
```

### Step 3 — Django calls the view

Django calls:

```python
views.about
```

### Step 4 — The view renders the template

```python
return render(request, "about.html")
```

### Step 5 — Django returns a response

The browser receives the generated HTML.

### Step 6 — Browser displays the page

The user sees the About page.

The complete flow:

```text
Browser
   ↓
Request
   ↓
URL Configuration
   ↓
View
   ↓
Template
   ↓
HTML Response
   ↓
Browser
```

---

# 54. Session 1 Challenge

## 🎯 Primary Challenge — Build the About Page

Now it is your turn.

Create an `/about/` page using the concepts you have learned.

### Requirements

Your page must contain:

* [ ] A page title
* [ ] A short description
* [ ] Navigation
* [ ] Bootstrap styling
* [ ] A link back to Home
* [ ] Template inheritance

The page should be available at:

```text
http://127.0.0.1:8000/about/
```

### Your task

Try to build it yourself before looking at the previous implementation.

Think about the required pieces:

```text
About Page
   │
   ├── URL
   │
   ├── View
   │
   └── Template
```

Ask yourself:

> Which file handles the URL?

> Which function handles the request?

> Which HTML file should be rendered?

> How can the page reuse `base.html`?

---

# 55. Optional Challenge

Finished early?

Create a new:

```text
/contact/
```

page.

### Requirements

Your Contact page should:

* Have its own URL.
* Have its own view.
* Have its own template.
* Extend `base.html`.
* Use Bootstrap.
* Appear in the navigation.
* Provide a way to return to Home.

### Extra challenge

Try to complete it **without copying the exact implementation from the previous pages**.

The objective is to test whether you understand the relationship between:

```text
URL
 ↓
View
 ↓
Template
```

---

# 56. Optional Git Setup

GitHub will be covered properly in Session 3.

For Session 1, Git is optional.

If Git is already installed, you can initialize the repository:

```bash
git init
```

Check the status:

```bash
git status
```

Create:

`.gitignore`

```gitignore
# Python
__pycache__/
*.py[cod]

# Virtual environments
.venv/
venv/

# Django
db.sqlite3

# Environment variables
.env

# IDE
.vscode/
.idea/

# Operating system files
.DS_Store
Thumbs.db
```

Then:

```bash
git add .
```

Create your first commit:

```bash
git commit -m "Complete Django Session 1 foundation"
```

> **Do not worry about GitHub yet.** The complete Git/GitHub workflow will be covered in Session 3.

---

# 57. Common Errors & Troubleshooting

## `python` is not recognized

### Cause

Python may not be installed or may not be available in your PATH.

### Try

```bash
py --version
```

If that works, use `py` instead of `python`.

---

## `py` works but `python` does not

This is common on Windows.

Use:

```bash
py manage.py runserver
```

instead of:

```bash
python manage.py runserver
```

---

## Virtual environment will not activate

### Windows PowerShell

Try:

```powershell
.venv\Scripts\Activate.ps1
```

If PowerShell blocks the script, you may need:

```powershell
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
```

Then:

```powershell
.venv\Scripts\Activate.ps1
```

Alternatively, use Command Prompt:

```cmd
.venv\Scripts\activate
```

---

## Django is not installed

Check:

```bash
python -m django --version
```

If Django is missing:

```bash
python -m pip install django
```

Make sure your virtual environment is activated first.

---

## `django-admin` is not recognized

Use:

```bash
python -m django startproject config .
```

instead of:

```bash
django-admin startproject config .
```

---

## `ModuleNotFoundError: No module named 'django'`

### Likely cause

Django is not installed in your active virtual environment.

Check that the terminal contains:

```text
(.venv)
```

Then run:

```bash
python -m pip install django
```

Verify:

```bash
python -m django --version
```

---

## `TemplateDoesNotExist`

For example:

```text
TemplateDoesNotExist: home.html
```

### Check your directory

Make sure:

```text
templates/
└── home.html
```

exists.

### Check `settings.py`

Make sure:

```python
"DIRS": [BASE_DIR / "templates"],
```

### Check your view

Make sure:

```python
return render(request, "home.html")
```

matches the filename exactly.

---

## 404 Page Not Found

Check that your URL exists.

For About:

`students/urls.py`

```python
path("about/", views.about, name="about"),
```

And:

`config/urls.py`

```python
path("", include("students.urls")),
```

Also make sure you visit:

```text
http://127.0.0.1:8000/about/
```

---

## `NoReverseMatch`

If you see:

```text
NoReverseMatch
```

check the URL name.

For example:

```django
{% url 'about' %}
```

requires:

```python
path("about/", views.about, name="about"),
```

The names must match exactly.

---

## Port 8000 is already in use

Run the development server on another port:

```bash
python manage.py runserver 8001
```

Then visit:

```text
http://127.0.0.1:8001/
```

---

## Changes are not appearing

Try:

1. Save your file.
2. Refresh the browser.
3. Check the terminal for errors.
4. Stop the server:

```text
Ctrl + C
```

5. Start it again:

```bash
python manage.py runserver
```

---

# 58. Useful Django Commands

| Command                              | Purpose                     |
| ------------------------------------ | --------------------------- |
| `python --version`                   | Check Python                |
| `python -m venv .venv`               | Create virtual environment  |
| `python -m pip install django`       | Install Django              |
| `python -m django --version`         | Check Django                |
| `django-admin startproject config .` | Create project              |
| `python manage.py runserver`         | Start development server    |
| `python manage.py startapp students` | Create app                  |
| `python manage.py check`             | Check project configuration |
| `python manage.py help`              | Show available commands     |

### Windows `py` alternative

```bash
py --version
py -m venv .venv
py -m pip install django
py -m django --version
py manage.py runserver
py manage.py startapp students
```

---

# 59. Final Session 1 Checklist

Before finishing, verify everything.

## Environment

* [ ] Python installed
* [ ] Python version checked
* [ ] Virtual environment created
* [ ] Virtual environment activated
* [ ] Django installed
* [ ] Django version checked

## Django Project

* [ ] Django project created
* [ ] `manage.py` exists
* [ ] Development server works
* [ ] Django welcome page was displayed

## Students App

* [ ] `students` app created
* [ ] App registered in `INSTALLED_APPS`
* [ ] `students/views.py` created
* [ ] `students/urls.py` created
* [ ] App URLs connected to project URLs

## Templates

* [ ] `templates/` directory created
* [ ] Templates configured in `settings.py`
* [ ] `base.html` created
* [ ] `home.html` created
* [ ] `about.html` created
* [ ] `students/list.html` created
* [ ] Template inheritance implemented

## Pages

* [ ] Home page works
* [ ] About page works
* [ ] Students page works
* [ ] Navigation works

## Frontend

* [ ] Bootstrap added
* [ ] Navbar created
* [ ] Buttons added
* [ ] Basic page layout implemented

## Understanding

* [ ] I understand what Django is
* [ ] I understand project vs app
* [ ] I understand what `manage.py` does
* [ ] I understand basic URL routing
* [ ] I understand what a view does
* [ ] I understand what a template is
* [ ] I understand `{% extends %}`
* [ ] I understand `{% block %}`
* [ ] I understand the basic MVT architecture
* [ ] I understand the URL → View → Template flow

---

# 60. Final Verification

Before considering Session 1 complete, run:

```bash
python manage.py check
```

You should see:

```text
System check identified no issues (0 silenced).
```

Then start the server:

```bash
python manage.py runserver
```

Test all three URLs.

### Home

```text
http://127.0.0.1:8000/
```

### About

```text
http://127.0.0.1:8000/about/
```

### Students

```text
http://127.0.0.1:8000/students/
```

Test every navigation button.

---

# 61. Key Takeaways

If you remember only a few things from Session 1, remember these:

### Django

Django is a Python web framework for building web applications.

### Project

The project contains the overall configuration.

```text
config/
```

### App

The app contains functionality for a specific part of the application.

```text
students/
```

### URLs

URLs determine which view should handle a request.

### Views

Views contain Python logic that handles requests and returns responses.

### Templates

Templates contain the HTML that users see.

### Template inheritance

`base.html` provides common structure that other templates can reuse.

### MVT

```text
Model
View
Template
```

For Session 1, our primary focus is:

```text
URL
 ↓
View
 ↓
Template
 ↓
Response
```

---

# 62. What Happens in Session 2?

Congratulations — you have built the foundation of the Student Management System.

Right now, the Students page is static.

In Session 2, we will make it dynamic.

We will introduce:

### Django Models

Define what a student record looks like.

### SQLite

Store student information in a database.

### Migrations

Apply changes to the database structure.

### Django ORM

Work with database records using Python.

### Django Admin

Manage records through Django's built-in administration interface.

### ModelForms

Create forms connected to our Student model.

### Validation

Make sure submitted data is valid.

### CRUD

Implement:

```text
Create
Read
Update
Delete
```

The application will evolve from:

```text
Session 1
Static Django website
```

to:

```text
Session 2
Dynamic Student Management System
```

---

# 🎉 Session 1 Complete

You have now built the foundation of a Django web application.

The journey so far:

```text
Python
  ↓
Virtual Environment
  ↓
Django
  ↓
Project
  ↓
App
  ↓
URLs
  ↓
Views
  ↓
Templates
  ↓
Template Inheritance
  ↓
Bootstrap
  ↓
Navigation
```

The next step is to give the application something to manage.

## Session 2

> **Database & CRUD — Make the Application Dynamic**

See you there.

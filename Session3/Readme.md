Session 3 — Authentication, GitHub & Deployment

Turn It Into a Real Application

Django Web Development Bootcamp — Session 3

Welcome to Session 3 of the Django Web Development Bootcamp.

In Session 1, we built the basic structure of our Student Management System using Django URLs, views, templates, Bootstrap, and template inheritance.

In Session 2, we made the application dynamic by connecting Django to SQLite and implementing database-backed CRUD operations.

In this session, we will take the same project one step further by adding authentication, Git/GitHub, and deployment.

🎯 Session Goal

By the end of this session, you will transform your application from:

DATABASE + CRUD
       ↓
AUTHENTICATION
       ↓
GIT + GITHUB
       ↓
PRODUCTION DATABASE
       ↓
DEPLOYMENT
       ↓
LIVE APPLICATION

Our Student Management System will now become an application that can:

Register users

Log users in

Log users out

Protect student management pages

Track code with Git

Store the project on GitHub

Use PostgreSQL in production

Run as a deployed Django application

🧠 What We Will Build

Our Student Management System will gradually become:

                  Student Management System
                           │
          ┌────────────────┼────────────────┐
          │                │                │
          ↓                ↓                ↓
    Authentication     Students          Admin
          │                │
     ┌────┼────┐           ↓
     ↓    ↓    ↓         CRUD
 Register Login Logout     │
          │           ┌────┼────┐
          │           ↓    ↓    ↓
          │         Create Read Update
          │                 │
          │                 ↓
          │               Delete
          │                 │
          └─────────────────┤
                            ↓
                       PostgreSQL
                            │
                            ↓
                          Render
                            │
                            ↓
                     Live Application

By the end of this session, the project will no longer be only a local Django application.

It will be a deployed web application that can be accessed through the internet.

📚 Session 3 Learning Objectives

During this session, you will learn how to:

Understand Django authentication

Understand users and sessions

Create a registration page

Use Django's built-in authentication system

Implement login

Implement logout

Display the authenticated user

Protect views using login_required

Understand Git

Initialize a Git repository

Create a .gitignore

Create commits

Create a GitHub repository

Push the Django project to GitHub

Understand why SQLite is useful for development

Understand why PostgreSQL is suitable for production

Connect Django to PostgreSQL

Use environment variables

Configure static files for deployment

Create a deployment build script

Deploy the Django application to Render

Run production migrations

Create a production superuser

Test authentication and CRUD on the live application

⏱️ Suggested 3-Hour Workshop Plan

Time

Topic

0:00 – 0:10

Recap of Session 2

0:10 – 0:45

Django Authentication

0:45 – 1:15

Login, Logout & Protected Pages

1:15 – 1:25

Short Break

1:25 – 1:45

Git & GitHub

1:45 – 2:00

Push Project to GitHub

2:00 – 2:20

SQLite → PostgreSQL

2:20 – 2:50

Deploy Django Application to Render

2:50 – 3:00

Testing, Challenge & Final Recap

Tip: Do not worry if your code is not identical to the instructor's code at every step. The important thing is understanding what each part does.

🔄 Quick Recap from Session 2

In Session 2, we changed our application from a static application into a database-backed application.

The basic flow became:

Browser
   ↓
URL
   ↓
View
   ↓
Model / ORM
   ↓
SQLite Database
   ↓
View
   ↓
Template
   ↓
Browser

For CRUD operations, the flow became:

Browser
   ↓
Form
   ↓
POST
   ↓
View
   ↓
ModelForm
   ↓
Validation
   ↓
Database

Our Student model contains:

Student
 ├── name
 ├── email
 ├── phone
 ├── faculty
 ├── semester
 └── created_at

And we already have:

Create
Read
Update
Delete

Now we need to control who can access these operations.

🔐 1. What Is Authentication?

Authentication answers a simple question:

Who are you?

For example:

Username
Password

The application checks those credentials and determines whether the user is authenticated.

The basic flow is:

User
  ↓
Login
  ↓
Authentication
  ↓
Authenticated User
  ↓
Student Management System

👤 2. Django's Built-in Authentication

Django already provides an authentication system.

It includes functionality for:

Users

Passwords

Login

Logout

Sessions

Authentication checks

Django already includes:

django.contrib.auth

We will use Django's built-in User model for this workshop.

We are keeping authentication simple. We are not introducing custom user models, OAuth, social login, JWT, or role-based authentication in this session.

📝 3. Create a Registration View

We want users to be able to create an account.

The flow will be:

/register/
      ↓
Registration Form
      ↓
Create User
      ↓
Login
      ↓
Student List

Open:

students/views.py

Add:

from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login

Then add:

def register(request):

    if request.method == "POST":

        form = UserCreationForm(request.POST)

        if form.is_valid():

            user = form.save()

            login(request, user)

            return redirect("student-list")

    else:

        form = UserCreationForm()

    return render(
        request,
        "students/register.html",
        {"form": form}
    )

🧠 Understanding the Registration View

When the user submits the registration form:

POST Request
     ↓
UserCreationForm
     ↓
Validation
     ↓
Create User
     ↓
Login User
     ↓
Student List

The important line:

user = form.save()

creates the user.

Then:

login(request, user)

logs the user into the current session.

📄 4. Create the Registration Template

Create:

students/templates/students/register.html

Add:

{% extends "base.html" %}

{% block title %}
Register - Student Management System
{% endblock %}

{% block content %}

<div class="row justify-content-center">
    <div class="col-md-6">

        <h2 class="mb-4">Create Account</h2>

        <form method="POST">

            {% csrf_token %}

            {{ form.as_p }}

            <button
                type="submit"
                class="btn btn-primary"
            >
                Register
            </button>

        </form>

        <p class="mt-3">
            Already have an account?
            <a href="{% url 'login' %}">
                Login
            </a>
        </p>

    </div>
</div>

{% endblock %}

Notice that we are still using the same template inheritance structure from the previous sessions:

base.html
    ↓
register.html

🔗 5. Add the Registration URL

Open:

students/urls.py

Add:

path(
    "register/",
    views.register,
    name="register"
),

The URL becomes:

/register/

Test it:

http://127.0.0.1:8000/register/

Create a test account.

🔑 6. Add Login

Django already provides a login view.

We do not need to manually implement password checking.

Open:

students/urls.py

Add:

from django.contrib.auth import views as auth_views

Then add:

path(
    "login/",
    auth_views.LoginView.as_view(
        template_name="students/login.html"
    ),
    name="login"
),

📄 7. Create the Login Template

Create:

students/templates/students/login.html

Add:

{% extends "base.html" %}

{% block title %}
Login - Student Management System
{% endblock %}

{% block content %}

<div class="row justify-content-center">
    <div class="col-md-6">

        <h2 class="mb-4">Login</h2>

        <form method="POST">

            {% csrf_token %}

            {{ form.as_p }}

            <button
                type="submit"
                class="btn btn-primary"
            >
                Login
            </button>

        </form>

        <p class="mt-3">
            Don't have an account?
            <a href="{% url 'register' %}">
                Register
            </a>
        </p>

    </div>
</div>

{% endblock %}

↪️ 8. Configure Login Redirect

Open:

config/settings.py

Add:

LOGIN_REDIRECT_URL = "/students/"
LOGOUT_REDIRECT_URL = "/"

This means:

Successful Login
       ↓
/students/

and:

Logout
   ↓
/

🚪 9. Add Logout

We can use Django's built-in logout view.

Open:

students/urls.py

Add:

path(
    "logout/",
    auth_views.LogoutView.as_view(),
    name="logout"
),

The URL becomes:

/logout/

🛡️ 10. Protect the Student Pages

This is one of the most important concepts in this session.

Currently:

Anyone
   ↓
/students/
   ↓
Student Records

We want:

Anonymous User
      ↓
/students/
      ↓
Login Required
      ↓
/login/

🔒 11. Use login_required

Open:

students/views.py

Add:

from django.contrib.auth.decorators import login_required

Then protect the student list:

@login_required
def student_list(request):

    students = Student.objects.all()

    return render(
        request,
        "students/student_list.html",
        {"students": students}
    )

If an unauthenticated user visits the page, Django redirects them to the login page.

🧩 12. Protect All CRUD Operations

The Student Management System should not allow anonymous users to create, update or delete student records.

Add:

@login_required

to:

student_list
student_create
student_update
student_delete

For example:

@login_required
def student_create(request):
    ...

@login_required
def student_update(request, student_id):
    ...

@login_required
def student_delete(request, student_id):
    ...

Our application now works like:

                    Student Management System

                             │
                             ↓
                        Is logged in?
                        /          \
                      No            Yes
                      ↓              ↓
                   Login         Student CRUD
                                   │
                       ┌───────────┼───────────┐
                       ↓           ↓           ↓
                     Create       Edit       Delete

🧭 13. Update the Navigation Bar

Open:

templates/base.html

We want the navigation to change depending on whether the user is logged in.

Add the following inside the navigation area:

{% if user.is_authenticated %}

    <span class="text-white me-3">
        Hello, {{ user.username }}
    </span>

    <a
        href="{% url 'logout' %}"
        class="btn btn-outline-light"
    >
        Logout
    </a>

{% else %}

    <a
        href="{% url 'login' %}"
        class="btn btn-outline-light me-2"
    >
        Login
    </a>

    <a
        href="{% url 'register' %}"
        class="btn btn-primary"
    >
        Register
    </a>

{% endif %}

Now:

Not Logged In
     ↓
Login | Register

and:

Logged In
     ↓
Hello, username | Logout

🧪 14. Test Authentication

Start the server:

python manage.py runserver

Test Registration

Open:

/register/

Create a new account.

Expected:

Registration
     ↓
Account Created
     ↓
Automatically Logged In
     ↓
/students/

Test Logout

Click:

Logout

Expected:

Logout
   ↓
Homepage

Test Protected Page

After logout, visit:

/students/

Expected:

/students/
      ↓
Not Authenticated
      ↓
/login/

Test Login

Log in again.

Expected:

Login
  ↓
/students/
  ↓
Student CRUD Available

📦 15. What Is Git?

Our project is becoming larger.

We need a way to track changes.

Git is a version control system.

It allows us to:

Track changes

Save versions of the project

See project history

Return to previous versions

Think of it as:

Project
   ↓
Git
   ↓
Commits
   ↓
Project History

🌐 16. Git vs GitHub

Git and GitHub are not the same thing.

Git

A version-control system running on our computer.

GitHub

An online platform for storing and collaborating on Git repositories.

The relationship is:

Git
 ↓
Local Repository
 ↓
GitHub
 ↓
Remote Repository

🛠️ 17. Initialize Git

From the project root:

git init

Check the repository:

git status

You should now have a Git repository for the project.

🚫 18. Create .gitignore

We should not commit files that should remain local.

Create:

.gitignore

Add:

.venv/
venv/
__pycache__/
*.py[cod]
db.sqlite3
.env

Why ignore db.sqlite3?

Because this is our local development database.

We will use PostgreSQL for the deployed application.

Why ignore .env?

Environment files may contain secrets such as:

SECRET_KEY
DATABASE_URL

These should not be uploaded to GitHub.

💾 19. Create a Git Commit

Check the files:

git status

Add them:

git add .

Create a commit:

git commit -m "Complete authentication"

Check the history:

git log --oneline

🐙 20. Create a GitHub Repository

Create a new repository on GitHub.

Suggested name:

student-management-system

If your local project already contains a README, do not create another README during repository creation.

Connect your local repository:

git remote add origin YOUR_GITHUB_REPOSITORY_URL

Check:

git remote -v

Push the project:

git branch -M main
git push -u origin main

After pushing, open the GitHub repository and verify that your project files are visible.

🗄️ 21. SQLite and Production

In Session 2, we used SQLite:

Django
  ↓
SQLite
  ↓
db.sqlite3

SQLite is excellent for learning because:

No separate database server is required

Django supports it by default

The database is stored in a single file

It is simple to set up

It is excellent for small projects and workshops

However, when we deploy the application, we want a proper persistent production database.

We will use:

Django
  ↓
PostgreSQL

🔄 22. SQLite → PostgreSQL

We are not changing our Student model.

The model remains:

Student
 ├── name
 ├── email
 ├── phone
 ├── faculty
 ├── semester
 └── created_at

Only the database changes.

Before:

Django
   ↓
SQLite
   ↓
db.sqlite3

After deployment:

Django
   ↓
PostgreSQL
   ↓
Render Database

The Django ORM continues to work with our existing model.

📦 23. Install Production Dependencies

Activate your virtual environment.

Install:

pip install psycopg2-binary

Install database URL support:

pip install dj-database-url

Install WhiteNoise for static files:

pip install whitenoise

Install Gunicorn:

pip install gunicorn

Save the dependencies:

pip freeze > requirements.txt

🔐 24. Environment Variables

We should not put production secrets directly into our source code.

For example:

SECRET_KEY
DATABASE_URL

should be provided through environment variables.

The production architecture becomes:

GitHub
   │
   │ Source Code
   ↓
Render
   │
   ├── SECRET_KEY
   │
   └── DATABASE_URL
          │
          ↓
      PostgreSQL

⚙️ 25. Configure the Database

Open:

config/settings.py

Add:

import os
import dj_database_url

Then configure the database:

DATABASE_URL = os.environ.get("DATABASE_URL")

if DATABASE_URL:

    DATABASES = {
        "default": dj_database_url.parse(DATABASE_URL)
    }

else:

    DATABASES = {
        "default": {
            "ENGINE": "django.db.backends.sqlite3",
            "NAME": BASE_DIR / "db.sqlite3",
        }
    }

Now the application behaves differently depending on the environment.

Local Development

No DATABASE_URL
       ↓
SQLite
       ↓
db.sqlite3

Render

DATABASE_URL exists
       ↓
PostgreSQL

This means we can continue using SQLite locally while the deployed application uses PostgreSQL.

🎨 26. Configure Static Files

Production applications need to collect static files.

Open:

config/settings.py

Add WhiteNoise after Django's security middleware:

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "whitenoise.middleware.WhiteNoiseMiddleware",

    # existing middleware...
]

Configure:

STATIC_URL = "static/"

STATIC_ROOT = BASE_DIR / "staticfiles"

🔑 27. Configure the Secret Key

We should not hard-code the production secret key.

Use:

SECRET_KEY = os.environ.get(
    "SECRET_KEY",
    "django-insecure-development-key"
)

For production, Render will provide the real secret through an environment variable.

Warning: Never commit a real production secret key to GitHub.

🐞 28. Configure DEBUG

For local development, we normally use:

DEBUG = True

For production, we should disable debug mode.

A simple environment-based configuration is:

DEBUG = os.environ.get(
    "DEBUG",
    "False"
) == "True"

Locally:

DEBUG=True

can be used when needed.

On Render:

DEBUG=False

📜 29. Create build.sh

Create a new file in the project root:

build.sh

Add:

#!/usr/bin/env bash

set -o errexit

pip install -r requirements.txt

python manage.py collectstatic --no-input

python manage.py migrate

The purpose of the build script is to prepare the application whenever Render deploys it.

The process is:

Install Dependencies
        ↓
Collect Static Files
        ↓
Run Migrations
        ↓
Start Application

🧪 30. Test Before Deployment

Before deploying, test the project locally.

Run:

python manage.py check

Then:

python manage.py collectstatic

Then:

python manage.py migrate

Finally:

python manage.py runserver

Test:

/register/
/login/
/logout/
/students/

Make sure authentication and CRUD still work.

Tip: Fix local errors before deploying. Deployment is much easier when the project already works correctly on your computer.

💾 31. Commit Deployment Changes

Check:

git status

Add:

git add .

Commit:

git commit -m "Prepare project for deployment"

Push:

git push

Your GitHub repository should now contain the deployment-ready project.

🚂 32. Deploy to Render

For deployment, our architecture will be:

GitHub
   │
   ↓
Render Web Service
   │
   ↓
Django Application
   │
   ↓
Render PostgreSQL

We will create two production resources:

1. Render Web Service
2. Render PostgreSQL Database

🗄️ 33. Create a PostgreSQL Database

In Render:

Create a new PostgreSQL database.

Give the database a name.

Wait until the database is available.

Use the database connection URL for the web service.

The important relationship is:

Render PostgreSQL
       ↓
DATABASE_URL
       ↓
Django

🌐 34. Create the Render Web Service

In Render:

Create a new Web Service.

Connect your GitHub account.

Select your repository:

student-management-system

Select the appropriate Python environment.

Configure the build command:

./build.sh

Configure the start command:

python -m gunicorn config.asgi:application -k uvicorn.workers.UvicornWorker

🔐 35. Add Environment Variables

In the Render service settings, add:

SECRET_KEY
DATABASE_URL

You may also configure:

DEBUG=False

For:

DATABASE_URL

use the PostgreSQL connection URL provided by your Render database.

The production environment becomes:

Render
  │
  ├── Django
  │
  ├── SECRET_KEY
  │
  ├── DATABASE_URL
  │
  └── PostgreSQL

🚀 36. Deploy the Application

Click:

Deploy

Render will perform approximately this process:

GitHub Repository
        ↓
Clone Project
        ↓
Install Dependencies
        ↓
Run build.sh
        ↓
Collect Static Files
        ↓
Run Migrations
        ↓
Start Gunicorn
        ↓
Live Application

Wait until the deployment finishes successfully.

👑 37. Create the Production Superuser

There is an important difference between our local and production databases.

Our local superuser exists in:

Local SQLite

The production application uses:

Production PostgreSQL

Therefore, the local superuser does not automatically exist in the production database.

Open the Render Shell and run:

python manage.py createsuperuser

Follow the prompts.

Now you can access:

/admin/

using the production superuser.

🧪 38. Test the Live Application

Open the Render URL:

https://your-project.onrender.com/

Test the public pages:

/

/about/

Test authentication:

/register/

/login/

/logout/

Test protected pages:

/students/

Test CRUD:

Create
Read
Update
Delete

Test Admin:

/admin/

💾 39. Verify PostgreSQL Persistence

Create a student on the live application:

Create Student
      ↓
Django
      ↓
PostgreSQL

Refresh the page.

The student should still exist.

The final production flow is:

Browser
   ↓
Render
   ↓
Django
   ↓
Django ORM
   ↓
PostgreSQL
   ↓
Student Data

The local:

db.sqlite3

is no longer responsible for production data.

🧠 40. Understanding the Final Architecture

Our application has now evolved significantly.

Before Session 2

Browser
   ↓
Django
   ↓
Templates

After Session 2

Browser
   ↓
Django
   ↓
ORM
   ↓
SQLite

After Session 3

                         Browser
                            ↓
                         Render
                            ↓
                          Django
                            ↓
                  ┌─────────┴─────────┐
                  ↓                   ↓
            Authentication         ORM
                  ↓                   ↓
                User             PostgreSQL
                  │                   │
                  └─────────┬─────────┘
                            ↓
                    Student Management

🧩 41. Session 3 Challenge

Protect the Student Management System

Now implement and test the following yourself.

Requirements

Anonymous users cannot access /students/

Anonymous users cannot create students

Anonymous users cannot update students

Anonymous users cannot delete students

Logged-in users can perform CRUD

The navbar displays the logged-in username

Logged-in users can logout

After logout, protected pages require login again

Hint

Use:

from django.contrib.auth.decorators import login_required

Then:

@login_required
def your_view(request):
    ...

Expected Result

When not logged in:

/students/
      ↓
/login/

When logged in:

/students/
      ↓
Student CRUD

⚠️ 42. Common Problems

TemplateDoesNotExist

Example:

TemplateDoesNotExist:
students/login.html

Make sure the file exists at:

students/templates/students/login.html

NoReverseMatch

Example:

NoReverseMatch:
Reverse for 'login' not found

Check that your URL has:

name="login"

For example:

path(
    "login/",
    auth_views.LoginView.as_view(
        template_name="students/login.html"
    ),
    name="login"
)

ModuleNotFoundError: dj_database_url

Install:

pip install dj-database-url

Then:

pip freeze > requirements.txt

ModuleNotFoundError: psycopg2

Install:

pip install psycopg2-binary

Then:

pip freeze > requirements.txt

collectstatic Error

Check:

STATIC_URL = "static/"
STATIC_ROOT = BASE_DIR / "staticfiles"

and make sure WhiteNoise is installed:

pip install whitenoise

Database Connection Error

Check:

DATABASE_URL

in the Render environment variables.

Make sure it contains the correct PostgreSQL connection URL.

DisallowedHost

Make sure the deployed hostname is allowed by Django's ALLOWED_HOSTS configuration.

🏁 43. Final Session 3 Checklist

Before leaving the session, make sure you can answer yes to these questions:

Authentication

Do I understand authentication?

Can I register a user?

Can I log in?

Can I log out?

Do I understand user.is_authenticated?

Can I protect a view with login_required?

Are the Student CRUD pages protected?

Git & GitHub

Do I understand what Git is?

Do I understand the difference between Git and GitHub?

Can I initialize a Git repository?

Do I know why .gitignore is needed?

Can I create a commit?

Can I connect a local repository to GitHub?

Can I push my project to GitHub?

Deployment

Do I understand why SQLite is useful locally?

Do I understand why we use PostgreSQL for production?

Can I configure DATABASE_URL?

Do I understand environment variables?

Can I configure static files?

Can I create build.sh?

Can I deploy a Django project to Render?

Can I run migrations on the production database?

Can I create a production superuser?

Can I test the live application?

💡 The Big Idea

Don't leave this session thinking:

"I learned some authentication and deployment commands."

Instead, remember the complete journey:

DJANGO
   ↓
PROJECT
   ↓
APP
   ↓
URLS
   ↓
VIEWS
   ↓
TEMPLATES
   ↓
DATABASE
   ↓
MODELS
   ↓
ORM
   ↓
CRUD
   ↓
AUTHENTICATION
   ↓
GIT
   ↓
GITHUB
   ↓
POSTGRESQL
   ↓
RENDER
   ↓
LIVE APPLICATION

And the production application flow:

USER
  ↓
LOGIN
  ↓
AUTHENTICATED USER
  ↓
STUDENT CRUD
  ↓
DJANGO ORM
  ↓
POSTGRESQL
  ↓
RENDER

🎓 Session 3 Complete

You have taken the Student Management System from a local database-backed Django project to a more complete web application with:

Authentication
      ↓
Git & GitHub
      ↓
PostgreSQL
      ↓
Deployment
      ↓
Live Application

You did not just learn Django commands.

You built a project progressively:

Session 1
Django Fundamentals
        ↓
Session 2
Database & CRUD
        ↓
Session 3
Authentication, GitHub & Deployment
        ↓
Complete Student Management System

🚀 Bootcamp Complete

The same project has evolved through all three sessions.

Student Management System
          │
          ├── Django
          ├── Templates
          ├── Bootstrap
          ├── Database
          ├── ORM
          ├── CRUD
          ├── Authentication
          ├── Git
          ├── GitHub
          ├── PostgreSQL
          └── Render

You started with a basic Django website and finished with a deployed, database-backed application.
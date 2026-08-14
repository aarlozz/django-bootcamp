# Session 3 — Authentication, GitHub & Deployment

## Turn It Into a Real Application

> **Django Web Development Bootcamp — Session 3**

Welcome to **Session 3** — the final session of the Django Web Development Bootcamp.

In Session 1, we built the foundation of our **Student Management System** using Django URLs, views, templates, template inheritance, and Bootstrap.

In Session 2, we connected the application to a database and implemented full CRUD (Create, Read, Update, Delete) for student records using a `Student` model, `ModelForm`, and SQLite.

Today, we take the application the rest of the way. We will:

* Add authentication, so only logged-in users can manage students
* Push the project to GitHub
* Connect the project to a production PostgreSQL database
* Deploy the application to Render
* Test the finished, **live** Student Management System

---

## 🎯 Session Goal

By the end of this session, you will transform your application from:

```text
LOCAL, UNPROTECTED, DATABASE-BACKED APPLICATION
                    ↓
AUTHENTICATED APPLICATION
                    ↓
VERSION-CONTROLLED APPLICATION (GITHUB)
                    ↓
PRODUCTION-READY APPLICATION (POSTGRESQL)
                    ↓
🌐 LIVE, DEPLOYED APPLICATION (RENDER)
```

---

# 🧭 The Bootcamp Journey So Far

```text
Session 1
Static Django Website
        ↓
Session 2
Dynamic CRUD Application
        ↓
Session 3
Authenticated Application
        ↓
GitHub
        ↓
PostgreSQL
        ↓
Render
        ↓
🌐 LIVE STUDENT MANAGEMENT SYSTEM
```

Each stage builds directly on the one before it:

* **Session 1** gave the application URLs, views, and templates — the skeleton.
* **Session 2** gave the application a database, a model, and CRUD — the ability to actually store and manage data.
* **Session 3** makes that data safe (only logged-in users can touch it), puts the code under version control, and moves the whole application from your laptop onto the public internet.

Nothing from Sessions 1 or 2 gets thrown away or rebuilt. We are only **adding** to the existing `students` app inside the existing `student-management` project.

---

# 📚 Session 3 Learning Objectives

By the end of this session, you should be able to:

* Explain what authentication is and why the application needs it
* Explain Django's built-in `User` model and auth system
* Implement user registration
* Implement login and logout
* Protect views using `@login_required`
* Create authentication templates
* Redirect users correctly after login, logout, and registration
* Use `git init`, `git add`, `git commit`, `git push`
* Write a correct `.gitignore` for a Django project
* Explain why secrets should never be committed to GitHub
* Explain why the workshop uses SQLite locally but PostgreSQL in production
* Install and understand `psycopg2-binary` and `dj-database-url`
* Configure `DATABASES` using an environment variable
* Run migrations against a production database
* Explain why we do **not** copy local SQLite data into production
* Explain the Render deployment architecture
* Deploy a Django project to Render
* Configure Render environment variables
* Create a production superuser
* Test a live, deployed CRUD application

---

# ⏱️ Suggested 3-Hour Workshop Plan

| Time        | Part   | Topic                                              |
| ----------- | ------ | --------------------------------------------------- |
| 0:00 – 0:15 | Recap  | Session 2 recap + Session 3 roadmap                 |
| 0:15 – 0:55 | Part 1 | Authentication (register, login, logout, protect)   |
| 0:55 – 1:15 | Part 2 | Git & GitHub                                        |
| 1:15 – 1:20 | —      | Break                                                |
| 1:20 – 1:50 | Part 3 | SQLite → PostgreSQL, environment variables, settings |
| 1:50 – 2:35 | Part 4 | Render: PostgreSQL, Web Service, deploy, migrate     |
| 2:35 – 2:50 | —      | Final testing on the live application                |
| 2:50 – 3:00 | —      | Challenge + wrap-up                                  |

> **Tip:** Deployment can occasionally be slow or fail because of a typo in an environment variable, not because of your code. Don't panic — the Troubleshooting section near the end covers the most common issues.

> **Fallback:** If your deployment gets stuck during the workshop, keep working on your local Postgres/settings configuration and follow along as the instructor demonstrates the Render steps on the shared screen. You can redeploy after the session using this README.

---

# 🔄 Quick Recap From Session 2

At the end of Session 2, your project supports:

* ✅ `Student` model (`name`, `email`, `phone`, `faculty`, `semester`, `created_at`)
* ✅ SQLite database (`db.sqlite3`)
* ✅ Django Admin with the `Student` model registered
* ✅ `StudentForm` (`ModelForm`)
* ✅ Full CRUD: `student_list`, `student_create`, `student_update`, `student_delete`
* ✅ Templates: `student_list.html`, `student_form.html`, `student_confirm_delete.html`

Your project currently looks like this:

```text
student-management/
│
├── manage.py
├── db.sqlite3
│
├── config/
│   ├── __init__.py
│   ├── settings.py
│   ├── urls.py
│   ├── asgi.py
│   └── wsgi.py
│
├── students/
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── forms.py
│   ├── models.py
│   ├── urls.py
│   ├── views.py
│   │
│   ├── migrations/
│   │   ├── __init__.py
│   │   └── 0001_initial.py
│   │
│   └── templates/
│       └── students/
│           ├── student_list.html
│           ├── student_form.html
│           └── student_confirm_delete.html
│
└── templates/
    └── base.html
```

There is one problem: **anyone** who visits `/students/` can view, create, edit, or delete student records. There is no concept of a logged-in user yet. We fix that first.

---

# PART 1 — AUTHENTICATION

# 🔐 1. What Is Authentication?

**Authentication** is the process of confirming who a user is — usually with a username and password.

This is different from **authorization**, which decides what an authenticated user is *allowed* to do. This workshop only needs authentication: a user is either logged in or not.

```text
Visitor
   ↓
Registration
   ↓
Account Created
   ↓
Login
   ↓
Authenticated User
   ↓
Student Management
   ↓
Logout
```

---

# 🤔 2. Why Does the Student Management System Need Authentication?

Right now, `/students/` is public. Anyone with the URL can delete every student record.

A real Student Management System should only allow **staff members who are logged in** to view and manage student records. That is exactly what we are adding today.

---

# 👤 3. Django's Built-In `User` System

Django ships with a complete authentication system out of the box, including:

* A `User` model (`django.contrib.auth.models.User`)
* Password hashing (you never store plain-text passwords)
* Login/logout session handling
* Built-in forms (`UserCreationForm`, `AuthenticationForm`)
* Built-in views (`LoginView`, `LogoutView`)
* The `@login_required` decorator

`django.contrib.auth` is already in your `INSTALLED_APPS` from Session 1 — you do not need to add anything there.

We will use Django's default `User` model exactly as-is. We are **not** creating a custom user model, and we are **not** adding OAuth, social login, JWTs, or role-based permissions — those are outside the scope of this workshop.

---

# 🧩 4. Authentication Plan

We will add:

| Feature      | URL         | View                    | Template                       |
| ------------ | ----------- | ------------------------ | ------------------------------- |
| Registration | `/register/`| `students.views.register`| `registration/register.html`    |
| Login        | `/login/`   | Django's `LoginView`     | `registration/login.html`       |
| Logout       | `/logout/`  | Django's `LogoutView`    | — (redirects, no template needed) |

We will protect these existing views with `@login_required`:

```text
student_list
student_create
student_update
student_delete
```

`home` and `about` will stay public — there is nothing sensitive on those pages.

---

# 📁 5. Create the Registration Form Template Folder

Django's built-in `LoginView` looks for a template at `registration/login.html` by default. Create the folder now:

```text
templates/
└── registration/
```

We'll place both `login.html` and `register.html` inside this folder, alongside the existing `base.html`.

---

# ✍️ 6. Add the `register` View

**File:** `students/views.py` — **MODIFIED**

Add these imports to the top of the file, alongside your existing ones:

```python
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
```

Then add the registration view:

```python
def register(request):

    if request.method == "POST":
        form = UserCreationForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect("login")

    else:
        form = UserCreationForm()

    return render(
        request,
        "registration/register.html",
        {"form": form}
    )
```

**What changed:** A new `register` view was added.

**Why:** Django does not provide a built-in *registration* view — only login/logout. `UserCreationForm` is a built-in `ModelForm` for the `User` model that handles username, password, and password confirmation, including hashing the password correctly.

**How it works:** On `GET`, an empty form is shown. On `POST`, if the submitted username/password pair is valid, a new `User` is created and the visitor is redirected to the login page.

**How to test it:** We'll test this after the URL and template are in place, later in this section.

---

# 🔗 7. Add the Registration URL

**File:** `students/urls.py` — **MODIFIED**

Add the new path:

```python
path("register/", views.register, name="register"),
```

Your full file should now look like:

```python
from django.urls import path
from . import views


urlpatterns = [
    path("", views.home, name="home"),
    path("about/", views.about, name="about"),

    path("students/", views.student_list, name="student-list"),
    path("students/create/", views.student_create, name="student-create"),
    path(
        "students/<int:student_id>/edit/",
        views.student_update,
        name="student-update"
    ),
    path(
        "students/<int:student_id>/delete/",
        views.student_delete,
        name="student-delete"
    ),

    path("register/", views.register, name="register"),
]
```

> **Note:** Use your actual existing paths for `student-list`, `student-create`, `student-update`, and `student-delete` from Session 2 — only the `register` line is new. The layout above assumes your Session 2 `students/urls.py` nested student paths under `students/`; if your version kept them at the root (`""`, `"create/"`, `"<int:student_id>/edit/"`), keep that structure and simply add the `register` line.

---

# 🔗 8. Add Login and Logout URLs

Rather than writing login/logout views by hand, we use Django's built-in ones directly in the project-level URLs.

**File:** `config/urls.py` — **MODIFIED**

```python
from django.contrib import admin
from django.urls import include, path
from django.contrib.auth import views as auth_views


urlpatterns = [
    path("admin/", admin.site.urls),

    path(
        "login/",
        auth_views.LoginView.as_view(template_name="registration/login.html"),
        name="login"
    ),
    path(
        "logout/",
        auth_views.LogoutView.as_view(),
        name="logout"
    ),

    path("", include("students.urls")),
]
```

**What changed:** Two new paths, `login/` and `logout/`, using Django's built-in `LoginView` and `LogoutView`.

**Why:** Django already implements login and logout correctly — including session handling and CSRF protection — so we reuse it instead of writing it ourselves.

**How it works:** `LoginView` renders `registration/login.html` and, on a valid `POST`, logs the user in. `LogoutView` logs the user out and redirects them (we configure where, in the next step).

**How to test it:** Visit `http://127.0.0.1:8000/login/` after the template is created (next section).

---

# ⚙️ 9. Configure Redirect Settings

**File:** `config/settings.py` — **MODIFIED**

Add these three settings anywhere below `INSTALLED_APPS` (a good spot is near the bottom of the file):

```python
LOGIN_URL = "login"
LOGIN_REDIRECT_URL = "student-list"
LOGOUT_REDIRECT_URL = "home"
```

**What changed:** Three new settings were added.

**Why:**
* `LOGIN_URL` tells `@login_required` where to send an unauthenticated visitor.
* `LOGIN_REDIRECT_URL` tells Django where to send a user right after a successful login.
* `LOGOUT_REDIRECT_URL` tells Django where to send a user right after logging out.

**How it works:** These are just named URL patterns — Django looks them up with `reverse()` internally, the same mechanism behind `{% url %}`.

**How to test it:** Log in and confirm you land on the students page; log out and confirm you land on the home page.

---

# 🖼️ 10. Create the Login Template

**File:** `templates/registration/login.html` — **NEW**

```html
{% extends "base.html" %}

{% block title %}
Login - Student Management System
{% endblock %}

{% block content %}

<div class="row justify-content-center">

    <div class="col-md-5">

        <h1 class="mb-4">Login</h1>

        <form method="POST">

            {% csrf_token %}

            {{ form.as_p }}

            <button type="submit" class="btn btn-primary">
                Login
            </button>

        </form>

        <p class="mt-3">
            Don't have an account?
            <a href="{% url 'register' %}">Register here</a>
        </p>

    </div>

</div>

{% endblock %}
```

**Why:** `LoginView` automatically passes a login `form` (Django's `AuthenticationForm`) into this template's context — we just need to render it, exactly like we render `StudentForm` in `student_form.html`.

---

# 🖼️ 11. Create the Registration Template

**File:** `templates/registration/register.html` — **NEW**

```html
{% extends "base.html" %}

{% block title %}
Register - Student Management System
{% endblock %}

{% block content %}

<div class="row justify-content-center">

    <div class="col-md-5">

        <h1 class="mb-4">Register</h1>

        <form method="POST">

            {% csrf_token %}

            {{ form.as_p }}

            <button type="submit" class="btn btn-primary">
                Create Account
            </button>

        </form>

        <p class="mt-3">
            Already have an account?
            <a href="{% url 'login' %}">Login here</a>
        </p>

    </div>

</div>

{% endblock %}
```

**How to test both templates:**

1. Start the server: `python manage.py runserver`
2. Visit `http://127.0.0.1:8000/register/`
3. Create a test account
4. You should be redirected to `/login/`
5. Log in with that account
6. You should be redirected to `/students/` (currently still unprotected — we fix that next)

---

# 🔒 12. Protect the Student Pages With `@login_required`

**File:** `students/views.py` — **MODIFIED**

Add `@login_required` directly above each of the four student-management views. Your file should now look like:

```python
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from .models import Student
from .forms import StudentForm


def home(request):
    return render(request, "home.html")


def about(request):
    return render(request, "about.html")


@login_required
def student_list(request):
    students = Student.objects.all()

    return render(
        request,
        "students/student_list.html",
        {"students": students}
    )


@login_required
def student_create(request):

    if request.method == "POST":
        form = StudentForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect("student-list")

    else:
        form = StudentForm()

    return render(
        request,
        "students/student_form.html",
        {"form": form}
    )


@login_required
def student_update(request, student_id):

    student = get_object_or_404(Student, id=student_id)

    if request.method == "POST":
        form = StudentForm(request.POST, instance=student)

        if form.is_valid():
            form.save()
            return redirect("student-list")

    else:
        form = StudentForm(instance=student)

    return render(
        request,
        "students/student_form.html",
        {"form": form}
    )


@login_required
def student_delete(request, student_id):

    student = get_object_or_404(Student, id=student_id)

    if request.method == "POST":
        student.delete()
        return redirect("student-list")

    return render(
        request,
        "students/student_confirm_delete.html",
        {"student": student}
    )


def register(request):

    if request.method == "POST":
        form = UserCreationForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect("login")

    else:
        form = UserCreationForm()

    return render(
        request,
        "registration/register.html",
        {"form": form}
    )
```

**What changed:** `@login_required` was added above `student_list`, `student_create`, `student_update`, and `student_delete`.

**Why:** This is the actual protection step. Without it, anyone could still reach `/students/` directly by typing the URL.

**How it works:** `@login_required` checks `request.user.is_authenticated`. If the visitor is not logged in, Django redirects them to `LOGIN_URL` (which we set to `"login"`), and after a successful login, `LOGIN_REDIRECT_URL` sends them back.

**How to test it:**

1. Log out
2. Try visiting `http://127.0.0.1:8000/students/` directly
3. You should be redirected to `/login/?next=/students/`
4. Log in — you should land back on `/students/`

---

# 🧭 13. Update the Navigation Bar

**File:** `templates/base.html` — **MODIFIED**

Update the navbar's link section to show different links depending on whether the visitor is logged in:

```html
<div>

    <a class="btn btn-outline-light me-2" href="{% url 'home' %}">
        Home
    </a>

    <a class="btn btn-outline-light me-2" href="{% url 'about' %}">
        About
    </a>

    {% if user.is_authenticated %}

        <a class="btn btn-outline-light me-2" href="{% url 'student-list' %}">
            Students
        </a>

        <form method="POST" action="{% url 'logout' %}" class="d-inline">
            {% csrf_token %}
            <button type="submit" class="btn btn-outline-light">
                Logout ({{ user.username }})
            </button>
        </form>

    {% else %}

        <a class="btn btn-outline-light me-2" href="{% url 'login' %}">
            Login
        </a>

        <a class="btn btn-outline-light" href="{% url 'register' %}">
            Register
        </a>

    {% endif %}

</div>
```

**What changed:** The "Students" link and a "Logout" button now only appear for logged-in users. Logged-out visitors see "Login" and "Register" instead.

**Why:** There is no point showing a link to a page the visitor will just get redirected away from. This also gives a clear visual signal of whether you are logged in.

**How it works:** `{% if user.is_authenticated %}` uses Django's `auth` context processor (already enabled in your `TEMPLATES` setting from Session 1), which makes `user` available in every template automatically. Logout is submitted as a `POST` form rather than a plain link — Django's `LogoutView` only accepts `POST` by default, which also prevents a page prefetcher or crawler from accidentally logging someone out.

**How to test it:** Log in and out and confirm the navbar changes correctly each time.

---

# ✅ 14. Authentication — What We Just Built

```text
Visitor
   ↓
/register/
   ↓
UserCreationForm
   ↓
User created
   ↓
/login/
   ↓
AuthenticationForm
   ↓
Session created
   ↓
/students/ (protected by @login_required)
   ↓
/logout/
   ↓
Session ended
```

At this point, run through the full local checklist before moving on:

* [ ] Can register a new account
* [ ] Can log in with that account
* [ ] `/students/` redirects to `/login/` when logged out
* [ ] `/students/` works normally when logged in
* [ ] Create / Update / Delete still work while logged in
* [ ] Logout works and redirects to Home
* [ ] Navbar shows the correct links in both states

---

# PART 2 — GIT & GITHUB

# 🌱 15. Why Git and GitHub?

Right now, your project only exists on your own computer. Render (and any deployment platform) needs a way to get a copy of your code — that's what GitHub is for.

```text
Local Project
   ↓
git init
   ↓
git add
   ↓
git commit
   ↓
GitHub Repository
   ↓
git push
   ↓
Render
```

We only cover the Git commands needed for this workflow — no branching, pull requests, or GitHub Actions today.

---

# 🔍 16. Check if Git Is Already Set Up

If you completed the *optional* Git setup at the end of Session 1, you already have a local repository. Check:

```bash
git status
```

* If you see `fatal: not a git repository`, continue to step 17.
* If you see a list of tracked/untracked files instead, skip to step 19 — you already have a repo and a `.gitignore`.

---

# 🌱 17. Initialize the Repository

If you don't already have one:

```bash
git init
```

**What this does:** Creates a hidden `.git/` folder that turns your project directory into a Git repository capable of tracking changes.

---

# 📄 18. Create `.gitignore`

**File:** `.gitignore` — **NEW** (or already exists from Session 1)

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

# Static files (collected in production)
staticfiles/

# IDE
.vscode/
.idea/

# Operating system files
.DS_Store
Thumbs.db
```

**Why this matters — this is critical:** Your repository must **never** contain:

```text
venv/            → huge, machine-specific, easy to regenerate
.env              → contains secrets
db.sqlite3        → your local database file, may contain test data
secrets/keys      → should never exist in the repo at all
```

If secrets or credentials get committed to a public GitHub repository, anyone can read them — including automated bots that scan GitHub for leaked keys within seconds of a push. Environment variables exist specifically so secrets live only on your machine and on Render's servers, never in your source code.

---

# 📦 19. Stage and Commit Your Changes

Check what Git sees:

```bash
git status
```

Stage everything (respecting `.gitignore`):

```bash
git add .
```

Commit:

```bash
git commit -m "Add authentication to Student Management System"
```

**What this does:** `git add .` stages all changed/new files except the ones excluded by `.gitignore`. `git commit` saves a permanent snapshot of the staged files with a message describing the change.

---

# 🌐 20. Create a GitHub Repository

1. Go to [github.com](https://github.com) and log in
2. Click **New repository**
3. Name it, for example: `student-management`
4. Leave it **empty** (no README, no `.gitignore`, no license — you already have these locally)
5. Click **Create repository**

GitHub will show you a remote URL that looks like:

```text
https://github.com/your-username/student-management.git
```

---

# 🔗 21. Connect Your Local Repository to GitHub

```bash
git remote add origin https://github.com/your-username/student-management.git
```

**What this does:** Registers the GitHub URL under the name `origin`, so Git knows where to push your commits.

If you already added a remote earlier and need to change it:

```bash
git remote set-url origin https://github.com/your-username/student-management.git
```

---

# 🚀 22. Push to GitHub

```bash
git branch -M main
git push -u origin main
```

**What this does:** `git branch -M main` makes sure your default branch is named `main`. `git push -u origin main` uploads your commits to GitHub and remembers `origin main` as the default target for future pushes.

**How to test it:** Refresh your GitHub repository page in the browser — your files should now be visible there. Confirm that `db.sqlite3`, `venv/`, and `.env` are **not** in the file list.

From now on, after any further change:

```bash
git add .
git commit -m "Describe what changed"
git push
```

---

# PART 3 — PRODUCTION PREPARATION

# 🗄️ 23. SQLite vs. PostgreSQL

We used SQLite during local development because it's convenient — no separate server, no setup, just a single file.

For our deployed application, we will use **PostgreSQL** instead.

```text
Local Development

Django
  ↓
SQLite
  ↓
db.sqlite3


Production

Django
  ↓
PostgreSQL
  ↓
Render
```

You do **not** need to learn PostgreSQL administration or SQL for this workshop. You only need to understand the practical transition: SQLite is convenient for local development, PostgreSQL is used for the deployed application, and Django connects to it through a single environment variable — `DATABASE_URL`.

---

# 📦 24. Install Production Database Packages

```bash
pip install psycopg2-binary dj-database-url gunicorn whitenoise
```

| Package            | Purpose                                                                 |
| ------------------- | ------------------------------------------------------------------------ |
| `psycopg2-binary`   | Lets Django talk to a PostgreSQL database                                |
| `dj-database-url`   | Converts a single `DATABASE_URL` string into Django's `DATABASES` config |
| `gunicorn`          | A production web server that actually runs Django on Render              |
| `whitenoise`        | Serves static files (like the Django Admin's CSS/JS) in production       |

> Django's own development server (`runserver`) is only meant for local development. Render needs a real production server — that's what `gunicorn` provides.

---

# 📝 25. Freeze Your Dependencies

**File:** `requirements.txt` — **NEW** (or **MODIFIED** if it already exists)

```bash
pip freeze > requirements.txt
```

Your file should now contain at least:

```text
Django
psycopg2-binary
dj-database-url
gunicorn
whitenoise
```

(Exact version numbers will also appear — that's expected and fine.)

**Why:** Render doesn't have your packages installed. It reads `requirements.txt` and installs exactly what your project needs.

---

# ⚙️ 26. Update `settings.py` for Production

We'll make four changes to `config/settings.py`: `SECRET_KEY`, `DEBUG`, `ALLOWED_HOSTS`, and `DATABASES`. Each change keeps working exactly the same locally, and only changes behavior once the matching environment variable is set on Render.

**File:** `config/settings.py` — **MODIFIED**

At the very top of the file, make sure `os` is imported and add `dj_database_url`:

```python
import os
from pathlib import Path
import dj_database_url
```

### `SECRET_KEY`

```python
SECRET_KEY = os.environ.get(
    "SECRET_KEY",
    "django-insecure-your-existing-local-key"
)
```

**Why:** Locally, nothing changes — the fallback value (your existing key from `startproject`) is used. On Render, we will set a real `SECRET_KEY` environment variable, and that value will be used instead. The production key should never be the same as the one sitting in your GitHub repository.

### `DEBUG`

```python
DEBUG = os.environ.get("DEBUG", "True") == "True"
```

**Why:** Locally this defaults to `True` (normal development behavior — detailed error pages). On Render, we will explicitly set `DEBUG=False`, because showing detailed error pages (including parts of your source code) to the public internet is a serious security risk.

### `ALLOWED_HOSTS`

```python
ALLOWED_HOSTS = []

RENDER_EXTERNAL_HOSTNAME = os.environ.get("RENDER_EXTERNAL_HOSTNAME")
if RENDER_EXTERNAL_HOSTNAME:
    ALLOWED_HOSTS.append(RENDER_EXTERNAL_HOSTNAME)
```

**Why:** Django refuses requests to hostnames not listed in `ALLOWED_HOSTS`, as a security measure. Render automatically provides the `RENDER_EXTERNAL_HOSTNAME` environment variable for every web service, so this fills itself in correctly without you having to hard-code your Render URL.

### `DATABASES`

Find your existing `DATABASES` setting (currently pointing at SQLite) and replace it with:

```python
DATABASES = {
    "default": dj_database_url.config(
        default=f"sqlite:///{BASE_DIR / 'db.sqlite3'}"
    )
}
```

**Why:** `dj_database_url.config()` looks for a `DATABASE_URL` environment variable. Locally, that variable doesn't exist, so it falls back to your existing SQLite database — your local workflow is completely unaffected. On Render, we will set `DATABASE_URL` to point at a real PostgreSQL database, and Django will connect there automatically, with **no code change required**.

This is exactly why we use an environment variable instead of hard-coding a database connection string: the same code works in two different environments.

---

# 🎨 27. Configure Static Files for Production

Your project uses Bootstrap through a CDN and has no custom CSS/JS files of your own — so there's nothing to configure for *your* templates. However, the **Django Admin** interface does ship its own CSS/JS, and Render's production server does not serve static files automatically the way `runserver` does locally. `whitenoise` handles this for us.

**File:** `config/settings.py` — **MODIFIED**

Add `whitenoise` to `MIDDLEWARE`, directly after `SecurityMiddleware`:

```python
MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "whitenoise.middleware.WhiteNoiseMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]
```

Add near your other static settings (create this section if it doesn't exist yet):

```python
STATIC_URL = "static/"
STATIC_ROOT = BASE_DIR / "staticfiles"
STATICFILES_STORAGE = "whitenoise.storage.CompressedManifestStaticFilesStorage"
```

**Why:** `STATIC_ROOT` is the folder Django collects all static files into for production (via `collectstatic`, covered in the deployment steps). `WhiteNoiseMiddleware` then serves those files directly from your Django process — no separate file server needed, which keeps this beginner-friendly.

**How to test it locally:**

```bash
python manage.py collectstatic --no-input
```

You should see a new `staticfiles/` folder appear (already excluded by `.gitignore`) containing the Django Admin's CSS/JS.

---

# 🔄 28. Migrations in Production

After Django connects to PostgreSQL, that database is **completely empty** — it has no tables yet.

```bash
python manage.py migrate
```

This creates all the necessary tables (`Student`, Django's built-in `User`/session/auth tables, etc.) inside PostgreSQL, based on your existing migration files. We'll run this against Render's database in Part 4, from the Render Shell.

> **Important:** We are **not** migrating your local SQLite data into PostgreSQL. Render's PostgreSQL database starts empty. After running migrations there, you'll create a fresh production superuser and fresh student records directly on the live site. This keeps the workshop simple — teaching a SQLite → PostgreSQL data transfer is a separate, more advanced topic.

```text
Local SQLite
   ↓
Used for learning/testing only

Render PostgreSQL
   ↓
Fresh production database
   ↓
Run migrations
   ↓
Create production superuser
   ↓
Create fresh student records
```

---

# 💾 29. Commit Your Production Configuration

```bash
git add .
git commit -m "Prepare project for production deployment"
git push
```

Your GitHub repository now contains everything Render needs to build and run your application — without a single secret exposed in the code.

---

# PART 4 — RENDER DEPLOYMENT

# 🏗️ 30. Deployment Architecture

```text
GitHub
   ↓
Render Web Service  ──────  Render PostgreSQL
   ↓
Django Application
   ↓
🌐 LIVE STUDENT MANAGEMENT SYSTEM
```

Render will:

1. Pull your code from GitHub
2. Install dependencies from `requirements.txt`
3. Run your build command (which also runs `collectstatic`)
4. Start your app using `gunicorn`
5. Connect it to a Render-managed PostgreSQL database

---

# 🐘 31. Create the Render PostgreSQL Database

1. Log in at [render.com](https://render.com)
2. Click **New** → **PostgreSQL**
3. Give it a name, e.g. `student-management-db`
4. Choose the free tier (sufficient for this workshop)
5. Click **Create Database**

Once it's ready, open the database page and find the **Internal Database URL** (or **Connection String**). It looks like:

```text
postgresql://user:password@host/dbname
```

Copy it — you'll paste it into your web service's environment variables in the next step.

---

# 🌐 32. Create the Render Web Service

1. Click **New** → **Web Service**
2. Connect your GitHub account and select your `student-management` repository
3. Configure:

| Setting        | Value                                                            |
| -------------- | ----------------------------------------------------------------- |
| Name           | `student-management` (or any name you like)                       |
| Runtime        | Python 3                                                           |
| Build Command  | `pip install -r requirements.txt && python manage.py collectstatic --no-input && python manage.py migrate && python manage.py createsuperuser --noinput || true` |
| Start Command  | `gunicorn config.wsgi`                                             |

---

# 🔑 33. Configure Environment Variables

In your Web Service's **Environment** tab, add:

| Key                   | Value                                                |
| ---------------------- | ------------------------------------------------------ |
| `SECRET_KEY`            | a new random string, e.g. `your-secret-key`             |
| `DEBUG`                 | `False`                                                 |
| `DATABASE_URL`          | the Internal Database URL you copied in step 31         |
| `DJANGO_SUPERUSER_USERNAME` | admin         |
| `DJANGO_SUPERUSER_EMAIL` | admin@example.com         |
| `DJANGO_SUPERUSER_PASSWORD` | Strong@123         |

> Never paste your *actual* secret values into a README, a commit, or a chat message — the values above are placeholders. Generate your own `SECRET_KEY`, for example with:
> ```bash
> python -c "import secrets; print(secrets.token_urlsafe(50))"
> ```

`RENDER_EXTERNAL_HOSTNAME` is provided automatically by Render — you don't need to set it yourself.

---

# 🚀 34. Deploy

Click **Create Web Service** (or **Deploy** if you already created it). Render will:

* Clone your repository
* Run your build command
* Start your app with `gunicorn`

Watch the deploy logs. A successful deploy ends with a line indicating `gunicorn` has started and is listening for requests.

---

# 🧱 35. Run Migrations on Render

Open your Web Service's **Shell** tab and run:

```bash
python manage.py migrate
```

This creates every table — including the `Student` table and Django's authentication tables — inside your Render PostgreSQL database.

---

# 👑 36. Create a Production Superuser

Still in the Render Shell:

```bash
python manage.py createsuperuser
```

Follow the prompts to set a username, email, and password.

> This creates a **brand-new** admin account inside the production PostgreSQL database. Your local SQLite superuser from Session 2 does **not** automatically exist here — you must create one directly on Render.

---

# 🌐 37. Open the Live Application

Render shows your live URL at the top of the Web Service page, something like:

```text
https://student-management.onrender.com
```

Open it in your browser.

---

# ✅ 38. Final Testing Checklist

Test every one of these directly on the **live** Render URL:

* [ ] Homepage loads
* [ ] Registration works
* [ ] Login works
* [ ] Logout works
* [ ] `/students/` redirects to login when logged out
* [ ] Create student works
* [ ] Update student works
* [ ] Delete student works
* [ ] `/admin/` loads and looks styled correctly (confirms WhiteNoise is serving static files)
* [ ] Refresh the page after creating a student — the record is still there (confirms PostgreSQL persistence, not an in-memory fluke)

---

# 🔁 39. The Complete Deployment Flow

```text
Local Django Project
   ↓
Git
   ↓
GitHub
   ↓
Render
   ↓
Render PostgreSQL
   ↓
Environment Variables
   ↓
Migrations
   ↓
Production Superuser
   ↓
🌐 LIVE APPLICATION
```

---

# 🏗️ 40. Final Project Structure

```text
student-management/
│
├── .gitignore
├── requirements.txt
├── manage.py
├── db.sqlite3                (local only — never committed)
│
├── config/
│   ├── __init__.py
│   ├── settings.py           MODIFIED — SECRET_KEY, DEBUG, ALLOWED_HOSTS,
│   │                          DATABASES, MIDDLEWARE, static config,
│   │                          LOGIN_URL, LOGIN_REDIRECT_URL, LOGOUT_REDIRECT_URL
│   ├── urls.py                MODIFIED — login/ and logout/ paths
│   ├── asgi.py
│   └── wsgi.py
│
├── students/
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── forms.py
│   ├── models.py
│   ├── urls.py                MODIFIED — register/ path
│   ├── views.py               MODIFIED — register view, @login_required
│   │
│   ├── migrations/
│   │   ├── __init__.py
│   │   └── 0001_initial.py
│   │
│   └── templates/
│       └── students/
│           ├── student_list.html
│           ├── student_form.html
│           └── student_confirm_delete.html
│
└── templates/
    ├── base.html               MODIFIED — auth-aware navbar
    ├── home.html
    ├── about.html
    └── registration/
        ├── login.html          NEW
        └── register.html       NEW
```

---

# 🩺 41. Troubleshooting

## Authentication

### `NoReverseMatch` for `login` or `register`

**Cause:** The URL name doesn't exist yet, or you're using the wrong name in `{% url %}`.
**Fix:** Confirm `name="login"` exists in `config/urls.py` and `name="register"` exists in `students/urls.py`.
**Verify:** `{% url 'login' %}` and `{% url 'register' %}` should resolve without errors.

### `TemplateDoesNotExist: registration/login.html`

**Cause:** The `templates/registration/` folder is missing, or the file is misnamed.
**Fix:** Confirm the file lives at `templates/registration/login.html`, matching Django's default `LoginView` template path exactly.
**Verify:** Visit `/login/` — the form should render.

### Logging in redirects to the wrong page

**Cause:** `LOGIN_REDIRECT_URL` is missing or points to the wrong URL name.
**Fix:** Confirm `LOGIN_REDIRECT_URL = "student-list"` is in `settings.py` and that `"student-list"` is a real URL name.
**Verify:** Log in and confirm you land on `/students/`.

### `@login_required` doesn't redirect at all

**Cause:** The decorator is missing, or it's above the wrong function.
**Fix:** Double-check the decorator sits directly above `def student_list(request):` (and the other three views) with no blank line issue.
**Verify:** Log out, visit `/students/`, confirm you're redirected to `/login/?next=/students/`.

## Git & GitHub

### Git doesn't recognize a file you expect it to track

**Cause:** The file is listed in `.gitignore`.
**Fix:** Check `.gitignore` — if the file genuinely should be tracked, remove the matching line.
**Verify:** `git status` should show the file.

### `git push` fails with a permissions/authentication error

**Cause:** GitHub no longer accepts password authentication over HTTPS.
**Fix:** Use a Personal Access Token in place of your password, or set up SSH authentication.
**Verify:** `git push` completes without an authentication prompt failing.

### `.gitignore` isn't working for a file already tracked

**Cause:** `.gitignore` only affects untracked files — if a file was committed *before* you added it to `.gitignore`, Git keeps tracking it.
**Fix:**
```bash
git rm --cached db.sqlite3
git commit -m "Stop tracking db.sqlite3"
```
**Verify:** `git status` no longer shows changes to that file after editing it locally.

## PostgreSQL / Environment Variables

### `django.db.utils.OperationalError` on Render

**Cause:** `DATABASE_URL` is missing or incorrect on the Web Service.
**Fix:** Re-check the Environment tab — confirm `DATABASE_URL` exactly matches the Internal Database URL from your Render PostgreSQL instance.
**Verify:** Redeploy and check the logs for a successful startup.

### Missing environment variable errors

**Cause:** `SECRET_KEY`, `DEBUG`, or `DATABASE_URL` wasn't set on Render.
**Fix:** Add the missing variable in the Environment tab, then trigger a manual deploy.
**Verify:** The deploy log shows the app starting cleanly.

### Migration errors on Render

**Cause:** Usually means `DATABASE_URL` isn't connecting correctly yet.
**Fix:** Confirm the database is fully provisioned (not still spinning up) before running `migrate`.
**Verify:** `python manage.py migrate` in the Render Shell completes without errors.

## Render Build / Start

### Render build fails

**Cause:** Usually a missing package in `requirements.txt`.
**Fix:** Run `pip freeze > requirements.txt` again locally and re-commit/push.
**Verify:** The next Render build log shows all packages installing successfully.

### Render start command fails immediately

**Cause:** Typically `gunicorn config.wsgi` pointing at the wrong module path.
**Fix:** Confirm your project's config folder is actually named `config` (matches `config/wsgi.py`).
**Verify:** The deploy log shows `gunicorn` binding to a port and staying running.

### `ALLOWED_HOSTS` error on the live site

**Cause:** `RENDER_EXTERNAL_HOSTNAME` isn't being read correctly, or `ALLOWED_HOSTS` was overwritten instead of appended to.
**Fix:** Re-check the `ALLOWED_HOSTS` code from step 26 — it must use `.append()`, not `=`.
**Verify:** Reload the live URL — the "DisallowedHost" error should be gone.

### Static files (Admin CSS) missing/unstyled on the live site

**Cause:** `collectstatic` wasn't run, or `whitenoise` middleware/setting is missing.
**Fix:** Confirm the build command includes `python manage.py collectstatic --no-input`, and that `WhiteNoiseMiddleware` is in `MIDDLEWARE` directly after `SecurityMiddleware`.
**Verify:** Reload `/admin/` on the live site — it should look properly styled.

### Admin login works locally but not on the live site

**Cause:** No production superuser has been created yet — the local one only exists in your local SQLite file.
**Fix:** Run `python manage.py createsuperuser` from the Render Shell.
**Verify:** Log in at `https://your-app.onrender.com/admin/` with the new credentials.

### Data disappears after a redeploy

**Cause:** This should **not** happen with a proper Render PostgreSQL database — if it does, double check `DATABASE_URL` is actually set (if it's missing, Django silently falls back to a fresh local SQLite file on each new deploy, which does not persist).
**Fix:** Re-verify the `DATABASE_URL` environment variable.
**Verify:** Create a student, trigger a manual redeploy from the Render dashboard, and confirm the student is still there afterward.

---

# 🎯 42. Session 3 Challenge

**Problem statement:** Right now, any logged-in user can edit or delete *any* student record — there's no ownership. Add a lightweight safeguard without introducing a whole new authorization system.

**Requirements:**

* Add a `created_by` field to the `Student` model, linked to Django's `User` model
* Automatically set it to the currently logged-in user when a student is created
* On the student list page, display who created each record

**Hints:**

```python
created_by = models.ForeignKey(
    User,
    on_delete=models.CASCADE,
    null=True,
    blank=True
)
```

```python
if form.is_valid():
    student = form.save(commit=False)
    student.created_by = request.user
    student.save()
    return redirect("student-list")
```

Remember: this is a new model field, so it needs its own migration:

```bash
python manage.py makemigrations
python manage.py migrate
```

**Expected result:** The student list shows an extra "Added by" column with each record's creator, and new students are automatically attributed to whoever is logged in when they create them.

*(This is intentionally similar in spirit to the fields you already know from `Student` — it does not require ForeignKey deep-dives or advanced relationships to complete.)*

---

# 🏁 Final Session 3 Checklist

- [ ] Authentication implemented
- [ ] Registration tested
- [ ] Login tested
- [ ] Logout tested
- [ ] Protected student pages tested
- [ ] Git repository updated
- [ ] Project pushed to GitHub
- [ ] `.gitignore` protects `venv/`, `.env`, and `db.sqlite3`
- [ ] Production dependencies configured (`psycopg2-binary`, `dj-database-url`, `gunicorn`, `whitenoise`)
- [ ] `DATABASES` reads from `DATABASE_URL`
- [ ] `SECRET_KEY`, `DEBUG`, and `ALLOWED_HOSTS` read from environment variables
- [ ] Render PostgreSQL created
- [ ] Render Web Service created and connected to GitHub
- [ ] Environment variables configured on Render
- [ ] Deployed successfully
- [ ] Migrations applied on Render
- [ ] Production superuser created
- [ ] Live application tested
- [ ] CRUD tested on the live application
- [ ] Django Admin tested on the live application
- [ ] Database persistence verified after a redeploy

---

# 🎓 43. From Session 1 to a Live Application

```text
Session 1
Static Django Website

    ↓

Session 2
Dynamic CRUD Application

    ↓

Session 3
Authenticated Application

    ↓

GitHub

    ↓

PostgreSQL

    ↓

Render

    ↓

🌐 LIVE STUDENT MANAGEMENT SYSTEM
```

You started this bootcamp writing your very first Django view. Since then you have:

* Built URLs, views, templates, and template inheritance
* Connected a database and implemented full CRUD with a `ModelForm`
* Added real authentication with registration, login, logout, and protected pages
* Put your project under version control with Git and pushed it to GitHub
* Connected a production PostgreSQL database through an environment variable
* Deployed the whole application to Render

Your Student Management System is no longer just a learning exercise running on your laptop — it's a real, authenticated, database-backed web application, live on the internet, that anyone can visit.

---

# 🎉 Bootcamp Complete

```text
Python
  ↓
Django
  ↓
URLs → Views → Templates
  ↓
Database → Models → CRUD
  ↓
Authentication
  ↓
Git → GitHub
  ↓
PostgreSQL
  ↓
Render
  ↓
🌐 LIVE STUDENT MANAGEMENT SYSTEM
```

Congratulations — you've completed the Django Web Development Bootcamp.

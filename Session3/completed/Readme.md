# Session 2 — Database & CRUD

## Make the Application Dynamic

> **Django Web Development Bootcamp — Session 2**

Welcome to **Session 2** of the Django Web Development Bootcamp.

In Session 1, we built the basic structure of our **Student Management System** using Django URLs, views, templates, Bootstrap, and template inheritance.

The application could display pages, but the student page was still mostly **static**.

In this session, we will make the application **dynamic** by connecting Django to a database.

---

## 🎯 Session Goal

By the end of this session, you will transform your application from:

```text
STATIC APPLICATION
       ↓
DATABASE
       ↓
DYNAMIC APPLICATION
```

Instead of writing student information directly inside HTML, we will store actual student records in a database and allow users to:

* Create students
* View students
* Update students
* Delete students

This is called **CRUD**.

```text
C → Create
R → Read
U → Update
D → Delete
```

---

# 🧠 What We Will Build

Our Student Management System will gradually become:

```text
                Student Management System
                         │
          ┌──────────────┼──────────────┐
          │              │              │
       Students        Create         Admin
          │              │
          ↓              ↓
      Database ←────── Student
          │
          ├── View
          ├── Update
          └── Delete
```

By the end of this session, the `/students/` page will display actual records stored in the database.

---

# 📚 Session 2 Learning Objectives

During this session, you will learn how to:

* Understand what a database is
* Understand why web applications need databases
* Understand SQLite
* Understand Django Models
* Create a Django Model
* Define model fields
* Understand `CharField`
* Understand `EmailField`
* Understand `IntegerField`
* Understand `DateTimeField`
* Understand `max_length`
* Understand `auto_now_add=True`
* Understand basic model validation
* Understand Django migrations
* Run `makemigrations`
* Run `migrate`
* Understand the Django ORM
* Register models in Django Admin
* Create a Django superuser
* Add student records through Admin
* Retrieve records from the database
* Display database records in templates
* Understand CRUD
* Create a `ModelForm`
* Validate form input
* Use CSRF protection
* Connect forms to views
* Update records
* Delete records
* Connect the database, views, URLs, and templates together

---

# ⏱️ Suggested 3-Hour Workshop Plan

| Time        | Topic                             |
| ----------- | --------------------------------- |
| 0:00 – 0:15 | Recap of Session 1                |
| 0:15 – 0:40 | Databases, SQLite & Django Models |
| 0:40 – 1:10 | Create Model & Run Migrations     |
| 1:10 – 1:30 | Django Admin & Superuser          |
| 1:30 – 1:50 | Retrieve & Display Students       |
| 1:50 – 2:30 | Create Student with ModelForm     |
| 2:30 – 2:50 | Update & Delete Students          |
| 2:50 – 3:00 | CRUD Recap & Challenge            |

> **Tip:** Don't worry if your code is not identical to the instructor's code at every step. The important thing is understanding what each part does.

---

# 🔄 Quick Recap from Session 1

In Session 1, we learned the basic Django request flow:

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

For example:

```text
Browser
   ↓
/students/
   ↓
students/views.py
   ↓
students.html
   ↓
HTML Response
```

The problem is that our application does not yet have a proper place to store student information.

We could hard-code:

```html
<h3>Premal Shrestha</h3>
<p>Computer Engineering</p>
```

But imagine having 1,000 students.

We cannot manually write 1,000 HTML entries.

We need a **database**.

---

# 🗄️ 1. What Is a Database?

A database is a structured place where an application can store and retrieve information.

For our project, we need to store information such as:

```text
Student Name
Email
Phone
Faculty
Semester
Created Date
```

Instead of storing this information directly inside HTML, we store it in a database.

For example:

```text
Student
-------------------------------------
Name:       Premal Shrestha
Email:      premal@example.com
Phone:      9800000000
Faculty:    Computer Engineering
Semester:   6
```

Then Django can retrieve this information whenever someone visits the website.

---

# 🤔 Why Does Our Application Need a Database?

Without a database:

```text
HTML
 └── Student information is manually written
```

With a database:

```text
Database
 └── Student records
       ↓
     Django
       ↓
    Template
       ↓
    Browser
```

A database gives our application **persistent storage**.

That means the data remains available even after we close the browser or restart the Django server.

---

# 🪶 2. What Is SQLite?

For this workshop, Django will use **SQLite**.

SQLite is a lightweight database that stores the database in a single file.

Django creates this file:

```text
db.sqlite3
```

You will normally see it in the root directory of your Django project:

```text
project/
│
├── manage.py
├── db.sqlite3
│
├── config/
│   ├── settings.py
│   ├── urls.py
│   └── ...
│
└── students/
    ├── models.py
    ├── views.py
    └── ...
```

### Why SQLite for this workshop?

SQLite is useful for beginners because:

* No separate database server is required
* No complicated database installation is required
* Django supports it by default
* The database is stored in a single file
* It is excellent for learning and small projects

> In larger production systems, developers often use databases such as PostgreSQL or MySQL. For this workshop, SQLite keeps our focus on learning Django.

---

# 🧩 3. Django Models

Now we need to tell Django what a **Student** looks like.

Django uses something called a **Model**.

A model is a Python class that describes the structure of data we want to store.

Think of it like this:

```text
Python Model
      ↓
Database Table
```

Our `Student` model will represent a database table containing student records.

---

# 📋 4. Designing the Student Model

We will use the following fields:

| Field        | Django Type     | Purpose                |
| ------------ | --------------- | ---------------------- |
| `name`       | `CharField`     | Student's name         |
| `email`      | `EmailField`    | Student's email        |
| `phone`      | `CharField`     | Student's phone number |
| `faculty`    | `CharField`     | Student's faculty      |
| `semester`   | `IntegerField`  | Current semester       |
| `created_at` | `DateTimeField` | Record creation time   |

We are deliberately keeping the model simple.

We do **not** need:

* ForeignKey
* ManyToManyField
* OneToOneField
* Complex relationships

Those topics can be introduced later when they become necessary.

---

# 🛠️ 5. Create the Student Model

Open:

```text
students/models.py
```

You should already have the `students` app from Session 1.

Add the following:

```python
from django.db import models


class Student(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=15)
    faculty = models.CharField(max_length=100)
    semester = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
```

---

# 🔍 Understanding the Model

Let's understand each line.

## `class Student(models.Model):`

```python
class Student(models.Model):
```

We are creating a Python class called `Student`.

It inherits from:

```python
models.Model
```

This tells Django:

> "This Python class should be treated as a Django database model."

---

# 📝 `name`

```python
name = models.CharField(max_length=100)
```

`CharField` is used for relatively short text.

Examples:

```text
Premal Shrestha
Kiran Thapa
Anisha Sharma
```

### What is `max_length`?

```python
max_length=100
```

means the field can contain up to 100 characters.

---

# 📧 `email`

```python
email = models.EmailField()
```

`EmailField` is designed for email addresses.

For example:

```text
premal@example.com
student@gmail.com
```

It also provides email-oriented validation.

---

# 📱 `phone`

```python
phone = models.CharField(max_length=15)
```

We use `CharField` rather than `IntegerField` for phone numbers.

Why?

Because phone numbers are identifiers, not values that we normally perform mathematical calculations on.

For example:

```text
9801234567
```

Using text also avoids issues with leading zeros in some numbering systems.

---

# 🏫 `faculty`

```python
faculty = models.CharField(max_length=100)
```

This stores the student's faculty.

Example:

```text
Computer Engineering
Civil Engineering
Information Technology
Business Administration
```

---

# 🔢 `semester`

```python
semester = models.IntegerField()
```

`IntegerField` stores whole numbers.

Examples:

```text
1
2
3
4
5
6
7
8
```

---

# 🕒 `created_at`

```python
created_at = models.DateTimeField(auto_now_add=True)
```

This stores when the student record was first created.

The important part is:

```python
auto_now_add=True
```

It tells Django:

> Automatically set this field to the current date and time when the object is first created.

We don't need to manually enter the creation date.

---

# 🏷️ The `__str__()` Method

Our model also contains:

```python
def __str__(self):
    return self.name
```

This controls how a Student object is represented as text.

Without it, Django Admin might display something like:

```text
Student object (1)
Student object (2)
Student object (3)
```

With `__str__()`:

```text
Premal Shrestha
Kiran Thapa
Anisha Sharma
```

This makes our data much easier to understand.

---

# ⚠️ Common Beginner Mistake

Make sure your indentation is correct:

```python
class Student(models.Model):
    name = models.CharField(max_length=100)
```

Not:

```python
class Student(models.Model):
name = models.CharField(max_length=100)
```

Python uses indentation as part of its syntax.

---

# 🔄 6. Migrations

Creating the model does **not** immediately create the database table.

Django uses a migration system to manage changes to the database structure.

Think of migrations as instructions that tell Django:

> "The structure of my application has changed. Update the database accordingly."

The basic process is:

```text
models.py
   ↓
makemigrations
   ↓
Migration File
   ↓
migrate
   ↓
Database
```

---

# 🧪 7. Run `makemigrations`

Open your terminal.

Make sure you are in the directory containing `manage.py`.

Run:

```bash
python manage.py makemigrations
```

You should see output similar to:

```text
Migrations for 'students':
  students/migrations/0001_initial.py
    - Create model Student
```

### What happened?

Django detected our new model and generated a migration file.

You should now have something like:

```text
students/
│
├── migrations/
│   ├── __init__.py
│   └── 0001_initial.py
│
├── models.py
└── ...
```

---

# 🧠 `makemigrations` vs `migrate`

This is one of the most important concepts in Django.

### `makemigrations`

```bash
python manage.py makemigrations
```

Means:

> Create migration instructions based on changes to our models.

### `migrate`

```bash
python manage.py migrate
```

Means:

> Apply those migration instructions to the database.

Think:

```text
makemigrations
     =
Prepare the changes
```

and:

```text
migrate
     =
Apply the changes
```

---

# 🚀 8. Run `migrate`

Now run:

```bash
python manage.py migrate
```

Django will apply the migration files to the database.

You should see output similar to:

```text
Applying students.0001_initial... OK
```

Our Student model can now be stored in the database.

---

# 🔁 The Migration Workflow

Whenever you change a model, remember:

```text
1. Change models.py
        ↓
2. makemigrations
        ↓
3. migrate
```

For example:

```bash
python manage.py makemigrations
python manage.py migrate
```

### Important

Do not manually edit the database to reflect model changes during normal Django development.

Let Django's migration system manage the schema.

---

# 🧑‍💻 9. Django Admin

Django comes with a powerful administration interface.

It allows developers and administrators to manage database records without building every management interface themselves.

We can use it to:

* Add students
* View students
* Edit students
* Delete students

Before we can see our Student model in Admin, we need to register it.

---

# 📌 10. Register the Student Model

Open:

```text
students/admin.py
```

Add:

```python
from django.contrib import admin
from .models import Student


admin.site.register(Student)
```

Now Django Admin knows about our Student model.

---

# 👑 11. Create a Superuser

Django Admin requires an administrator account.

Run:

```bash
python manage.py createsuperuser
```

Django will ask for information such as:

```text
Username:
Email address:
Password:
Password (again):
```

Create your own credentials.

> **Workshop tip:** Use credentials you can remember during the session. Do not use passwords that you use for important personal accounts.

---

# ▶️ 12. Start the Development Server

Run:

```bash
python manage.py runserver
```

Then open:

```text
http://127.0.0.1:8000/admin/
```

You should see the Django Admin login page.

Log in using your superuser account.

---

# 🎓 13. Add Students Through Admin

After logging in, you should see:

```text
Students
```

Click:

```text
Students → Add Student
```

Enter some sample data.

For example:

```text
Name:       Premal Shrestha
Email:      premal@example.com
Phone:      9800000000
Faculty:    Computer Engineering
Semester:   6
```

Save the student.

Add several more students so we have enough records to test our application.

For example:

```text
Student 1
Student 2
Student 3
Student 4
Student 5
```

---

# 🔍 14. What Just Happened?

When you clicked **Save** in Django Admin:

```text
Admin Form
    ↓
Django
    ↓
Student Model
    ↓
Django ORM
    ↓
SQLite
```

The student information is now stored in:

```text
db.sqlite3
```

This is the first major transformation in our application.

Previously:

```text
HTML → Static content
```

Now:

```text
HTML
  ↑
Template
  ↑
View
  ↑
Model / ORM
  ↑
SQLite Database
```

---

# 🧠 15. What Is the Django ORM?

ORM stands for:

> **Object-Relational Mapping**

The ORM allows us to work with database records using Python instead of writing SQL for every operation.

For example, instead of manually writing SQL like:

```sql
SELECT * FROM students;
```

we can use Django:

```python
Student.objects.all()
```

Django translates our Python code into the appropriate database query.

---

# 🔎 16. Reading Students From the Database

Open:

```text
students/views.py
```

Import the model:

```python
from .models import Student
```

Then update the students view.

For example:

```python
from django.shortcuts import render
from .models import Student


def student_list(request):
    students = Student.objects.all()

    return render(
        request,
        "students/student_list.html",
        {"students": students}
    )
```

---

# 🧩 Understanding `Student.objects.all()`

This:

```python
Student.objects.all()
```

means:

> Get all Student records from the database.

The result is a Django QuerySet.

For example:

```text
Student 1
Student 2
Student 3
Student 4
```

We pass those records to the template:

```python
{"students": students}
```

---

# 🖥️ 17. Display Students in the Template

Create or update:

```text
students/templates/students/student_list.html
```

Example:

```html
{% extends "base.html" %}

{% block content %}

<div class="container mt-4">

    <h1 class="mb-4">Students</h1>

    <div class="table-responsive">
        <table class="table table-striped table-bordered">

            <thead>
                <tr>
                    <th>Name</th>
                    <th>Email</th>
                    <th>Phone</th>
                    <th>Faculty</th>
                    <th>Semester</th>
                </tr>
            </thead>

            <tbody>

                {% for student in students %}

                <tr>
                    <td>{{ student.name }}</td>
                    <td>{{ student.email }}</td>
                    <td>{{ student.phone }}</td>
                    <td>{{ student.faculty }}</td>
                    <td>{{ student.semester }}</td>
                </tr>

                {% empty %}

                <tr>
                    <td colspan="5" class="text-center">
                        No students found.
                    </td>
                </tr>

                {% endfor %}

            </tbody>

        </table>
    </div>

</div>

{% endblock %}
```

---

# 🔁 18. How Data Reaches the Browser

Let's understand the complete process.

When the browser requests:

```text
/students/
```

Django follows:

```text
Browser
   ↓
URL
   ↓
View
   ↓
Student.objects.all()
   ↓
SQLite Database
   ↓
Student records
   ↓
View
   ↓
Template
   ↓
HTML
   ↓
Browser
```

This is the core architecture we are learning in Session 2.

---

# 🔗 19. URL → View → Database → Template

Your URL configuration should point to the view.

For example, in:

```text
students/urls.py
```

you might have:

```python
from django.urls import path
from . import views


urlpatterns = [
    path("", views.student_list, name="student-list"),
]
```

And your project-level `urls.py` should include the students app as established in Session 1.

The important idea is:

```text
URL
 ↓
View
 ↓
Model
 ↓
Database
 ↓
Template
```

---

# 📝 20. Introducing CRUD

Our application now reads students from the database.

But a real Student Management System should allow us to manage the records.

This is where CRUD comes in.

## CRUD means:

| Operation | Meaning              | Example        |
| --------- | -------------------- | -------------- |
| Create    | Add new data         | Add a student  |
| Read      | Retrieve data        | View students  |
| Update    | Modify existing data | Edit student   |
| Delete    | Remove data          | Delete student |

Our application will implement all four.

---

# ➕ 21. Create — Adding a Student

There are several ways to create database records in Django.

For example:

```python
Student.objects.create(
    name="Premal Shrestha",
    email="premal@example.com",
    phone="9800000000",
    faculty="Computer Engineering",
    semester=6
)
```

However, we do not want users to write Python code to create students.

We need an HTML form.

Django provides a convenient solution:

> **ModelForm**

---

# 🧾 22. What Is a ModelForm?

A `ModelForm` is a Django form that is connected to a model.

It can automatically generate form fields based on our model.

Think of it as:

```text
Student Model
      ↓
   ModelForm
      ↓
   HTML Form
      ↓
     User
      ↓
    Submit
      ↓
    Model
      ↓
   Database
```

This saves us from manually creating every form field and validation rule.

---

# 📁 23. Create `forms.py`

Inside the `students` app, create:

```text
students/
├── admin.py
├── apps.py
├── forms.py
├── models.py
├── urls.py
├── views.py
└── ...
```

Create:

```text
students/forms.py
```

Add:

```python
from django import forms
from .models import Student


class StudentForm(forms.ModelForm):

    class Meta:
        model = Student
        fields = [
            "name",
            "email",
            "phone",
            "faculty",
            "semester",
        ]
```

---

# 🧠 Understanding the ModelForm

This tells Django:

```python
model = Student
```

Use the `Student` model.

And:

```python
fields = [
    "name",
    "email",
    "phone",
    "faculty",
    "semester",
]
```

These are the fields we want the user to enter.

We don't include:

```text
created_at
```

because Django automatically generates that value.

---

# ➕ 24. Create View

In:

```text
students/views.py
```

add:

```python
from django.shortcuts import render, redirect
from .forms import StudentForm


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
```

---

# 🧠 Understanding the Create View

The browser can make different types of requests.

For our form, we care about:

```text
GET
POST
```

### GET

A GET request is generally used to request or display a page.

When the user opens:

```text
/students/create/
```

we display an empty form.

### POST

A POST request is used when the user submits form data.

The flow becomes:

```text
User opens form
      ↓
GET request
      ↓
Empty form
      ↓
User enters data
      ↓
Submit
      ↓
POST request
      ↓
Validate form
      ↓
Save Student
      ↓
Database
```

---

# 🔗 25. Add the Create URL

In:

```text
students/urls.py
```

add:

```python
path(
    "create/",
    views.student_create,
    name="student-create"
),
```

Your URLs might now look like:

```python
from django.urls import path
from . import views


urlpatterns = [
    path("", views.student_list, name="student-list"),
    path(
        "create/",
        views.student_create,
        name="student-create"
    ),
]
```

---

# 🖼️ 26. Create the Form Template

Create:

```text
students/templates/students/student_form.html
```

Add:

```html
{% extends "base.html" %}

{% block content %}

<div class="container mt-4">

    <h1 class="mb-4">Add Student</h1>

    <form method="POST">

        {% csrf_token %}

        {{ form.as_p }}

        <button type="submit" class="btn btn-primary">
            Save Student
        </button>

        <a href="{% url 'student-list' %}" class="btn btn-secondary">
            Cancel
        </a>

    </form>

</div>

{% endblock %}
```

---

# 🔐 27. Understanding CSRF Protection

You will notice:

```django
{% csrf_token %}
```

This is extremely important.

CSRF means:

> **Cross-Site Request Forgery**

Django uses CSRF protection to help prevent unauthorized websites from submitting requests to your application on behalf of a user.

For Django forms that submit POST requests, we normally include:

```django
{% csrf_token %}
```

inside the form:

```html
<form method="POST">

    {% csrf_token %}

    ...
    
</form>
```

### Remember

If you create a Django form that uses:

```html
<form method="POST">
```

include:

```django
{% csrf_token %}
```

---

# ✅ 28. Form Validation

Our form contains:

```python
if form.is_valid():
```

This asks Django:

> "Is the submitted data valid?"

For example, our `EmailField` provides email-oriented validation.

If a user enters:

```text
hello
```

instead of something resembling an email address, Django can report a validation error.

This is one of the benefits of using:

```text
Model
   ↓
ModelForm
```

Django can use model field information to help construct and validate forms.

---

# 💾 29. Saving the Form

Once the form is valid:

```python
if form.is_valid():
    form.save()
```

Django saves the student to the database.

The process is:

```text
HTML Form
    ↓
POST Request
    ↓
StudentForm
    ↓
Validation
    ↓
form.save()
    ↓
Student Model
    ↓
SQLite
```

---

# 🔀 30. Why `redirect()`?

After saving the student:

```python
return redirect("student-list")
```

we redirect the user back to the student list.

This gives us a clean workflow:

```text
Create Student
      ↓
Save
      ↓
Redirect
      ↓
Student List
```

It also avoids unnecessarily resubmitting the same form if the user refreshes the page.

---

# ✏️ 31. Update — Editing a Student

Now we need to allow users to edit an existing student.

The basic process is:

```text
Select Student
      ↓
Load existing data
      ↓
Display form
      ↓
User edits data
      ↓
Submit
      ↓
Validate
      ↓
Save
      ↓
Database updated
```

---

# 🔍 32. Getting a Specific Student

To work with one student, we need to identify the record.

Every Django model automatically receives a primary key called:

```text
id
```

For example:

```text
Student
-------------------------------
id   name
-------------------------------
1    Premal
2    Kiran
3    Anisha
```

We can use the ID to retrieve a specific student.

Django provides:

```python
get_object_or_404()
```

Import it:

```python
from django.shortcuts import get_object_or_404
```

Then:

```python
student = get_object_or_404(Student, id=student_id)
```

This means:

> Find the Student with this ID. If it does not exist, return a 404 page.

---

# ✏️ 33. Update View

Add the following to:

```text
students/views.py
```

```python
def student_update(request, student_id):

    student = get_object_or_404(
        Student,
        id=student_id
    )

    if request.method == "POST":
        form = StudentForm(
            request.POST,
            instance=student
        )

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
```

---

# 🧠 What Does `instance=student` Do?

This is an important concept.

For a new student:

```python
form = StudentForm()
```

The form is empty.

For an existing student:

```python
form = StudentForm(instance=student)
```

Django loads that student's existing information into the form.

For example:

```text
Name: Premal Shrestha
Email: premal@example.com
Phone: 9800000000
Faculty: Computer Engineering
Semester: 6
```

The user can edit the values and save them.

---

# 🔗 34. Add the Update URL

In:

```text
students/urls.py
```

add:

```python
path(
    "<int:student_id>/edit/",
    views.student_update,
    name="student-update"
),
```

The URL might look like:

```text
/students/1/edit/
```

The:

```text
<int:student_id>
```

part captures the student's ID.

For example:

```text
/students/5/edit/
```

means:

```text
student_id = 5
```

---

# ✏️ 35. Add Edit Button

In:

```text
student_list.html
```

add an Actions column.

For example:

```html
<th>Actions</th>
```

Then inside the loop:

```html
<td>

    <a
        href="{% url 'student-update' student.id %}"
        class="btn btn-sm btn-warning"
    >
        Edit
    </a>

</td>
```

Now each student will have an Edit button.

---

# 🗑️ 36. Delete — Removing a Student

The final CRUD operation is Delete.

The basic flow is:

```text
Select Student
      ↓
Confirm deletion
      ↓
Delete record
      ↓
Database
      ↓
Student list
```

---

# 🗑️ 37. Delete View

Add:

```python
def student_delete(request, student_id):

    student = get_object_or_404(
        Student,
        id=student_id
    )

    if request.method == "POST":
        student.delete()
        return redirect("student-list")

    return render(
        request,
        "students/student_confirm_delete.html",
        {"student": student}
    )
```

---

# 🔗 38. Add Delete URL

In:

```text
students/urls.py
```

add:

```python
path(
    "<int:student_id>/delete/",
    views.student_delete,
    name="student-delete"
),
```

---

# ⚠️ 39. Why Use POST for Delete?

Deleting data changes the database.

We don't want a simple page visit to accidentally delete a student.

Instead of:

```text
GET → Delete
```

we use:

```text
POST → Delete
```

This is safer and follows normal web application practices.

---

# 🗑️ 40. Delete Confirmation Template

Create:

```text
students/templates/students/student_confirm_delete.html
```

Add:

```html
{% extends "base.html" %}

{% block content %}

<div class="container mt-4">

    <h1>Delete Student</h1>

    <p>
        Are you sure you want to delete
        <strong>{{ student.name }}</strong>?
    </p>

    <form method="POST">

        {% csrf_token %}

        <button type="submit" class="btn btn-danger">
            Yes, Delete
        </button>

        <a
            href="{% url 'student-list' %}"
            class="btn btn-secondary"
        >
            Cancel
        </a>

    </form>

</div>

{% endblock %}
```

Notice that we again use:

```django
{% csrf_token %}
```

because the form uses:

```html
method="POST"
```

---

# ✏️ 41. Add Delete Button

In the student list, add:

```html
<a
    href="{% url 'student-delete' student.id %}"
    class="btn btn-sm btn-danger"
>
    Delete
</a>
```

Now our Actions column can contain:

```text
Edit | Delete
```

---

# 🎯 42. Complete CRUD Flow

Our application can now perform:

```text
                 STUDENT
                    │
       ┌────────────┼────────────┐
       ↓            ↓            ↓
    CREATE         READ        UPDATE
       │            │            │
       └────────────┼────────────┘
                    ↓
                  DELETE
```

More practically:

```text
Create
  ↓
StudentForm
  ↓
Save to Database

Read
  ↓
Student.objects.all()
  ↓
Template

Update
  ↓
StudentForm(instance=student)
  ↓
Save Changes

Delete
  ↓
student.delete()
  ↓
Remove from Database
```

---

# 🏗️ 43. Final Project Structure

By the end of Session 2, your project should look approximately like:

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

Your exact structure may differ slightly depending on how Session 1 was organized.

---

# 🔄 44. The Complete Django Architecture

This is the most important concept to understand from Session 2.

When a user visits the student page:

```text
                    Browser
                       │
                       ↓
                     URL
                       │
                       ↓
                      View
                       │
                       ↓
                Django ORM / Model
                       │
                       ↓
                    SQLite
                       │
                       ↓
                 Student Data
                       │
                       ↓
                      View
                       │
                       ↓
                   Template
                       │
                       ↓
                    Browser
```

For creating a student:

```text
Browser
   ↓
Form
   ↓
POST Request
   ↓
View
   ↓
ModelForm
   ↓
Validation
   ↓
Model
   ↓
SQLite
   ↓
Redirect
   ↓
Student List
```

---

# 🧠 45. ORM Cheat Sheet

Here are some basic Django ORM operations worth remembering.

Assume:

```python
from .models import Student
```

### Get all students

```python
Student.objects.all()
```

### Get one student

```python
Student.objects.get(id=1)
```

### Create a student

```python
Student.objects.create(
    name="Premal",
    email="premal@example.com",
    phone="9800000000",
    faculty="Computer Engineering",
    semester=6
)
```

### Delete a student

```python
student.delete()
```

### Update a student

```python
student.name = "New Name"
student.save()
```

You don't need to memorize all of these today.

Focus first on understanding the pattern:

```text
Model.objects...
```

---

# 🧪 46. Workshop Practice

Now stop following the instructor for a few minutes and test your application.

Try the following tasks yourself.

### Task 1 — Add Students

Go to:

```text
/admin/
```

Create at least **5 students**.

---

### Task 2 — View Students

Open:

```text
/students/
```

Confirm that your students are displayed.

---

### Task 3 — Create Student

Open:

```text
/students/create/
```

Create a new student using your form.

Confirm that the student appears in the student list.

---

### Task 4 — Update Student

Choose a student.

Click:

```text
Edit
```

Change the student's semester.

Save the changes.

Confirm that the updated value appears.

---

### Task 5 — Delete Student

Choose a student.

Click:

```text
Delete
```

Confirm the deletion.

Check that the student disappears from the list.

---

# 🧩 47. Debugging Checklist

If your application is not working, don't panic.

Check these things first.

## Server not running?

Run:

```bash
python manage.py runserver
```

---

## Model changes not appearing?

Run:

```bash
python manage.py makemigrations
python manage.py migrate
```

---

## Model not appearing in Admin?

Check:

```text
students/admin.py
```

Make sure you have:

```python
from .models import Student

admin.site.register(Student)
```

---

## Template not found?

Check your template location:

```text
students/
└── templates/
    └── students/
        └── student_list.html
```

---

## URL not found?

Check:

```text
students/urls.py
```

and make sure the students URLs are included in the project URL configuration.

---

## Form submission gives CSRF error?

Make sure your POST form contains:

```django
{% csrf_token %}
```

---

## Student list is empty?

Check:

1. Did you create students?
2. Did you save them?
3. Did `Student.objects.all()` run?
4. Did you pass the students to the template?
5. Is your template looping over the correct variable?

For example:

```python
{"students": students}
```

and:

```django
{% for student in students %}
```

---

# 🚨 48. Common Beginner Mistakes

### Mistake 1 — Forgetting migrations

You changed:

```text
models.py
```

but didn't run:

```bash
python manage.py makemigrations
python manage.py migrate
```

---

### Mistake 2 — Forgetting to import the model

In `views.py`:

```python
from .models import Student
```

---

### Mistake 3 — Forgetting to register the model

In `admin.py`:

```python
admin.site.register(Student)
```

---

### Mistake 4 — Forgetting CSRF

For POST forms:

```django
{% csrf_token %}
```

---

### Mistake 5 — Wrong template variable

View:

```python
{"students": students}
```

Template:

```django
{% for student in students %}
```

The names must match.

---

### Mistake 6 — Using the wrong URL name

If your URL contains:

```python
name="student-update"
```

your template should use:

```django
{% url 'student-update' student.id %}
```

---

# 🔐 49. A Note About Validation

Validation exists at multiple levels.

For example:

```python
email = models.EmailField()
```

helps Django understand that this field represents an email address.

Forms can also provide validation.

For example:

```python
if form.is_valid():
```

checks whether the submitted form data satisfies the form's validation rules.

Later, you can create custom validation rules for requirements such as:

```text
Semester must be between 1 and 8
Phone number must have a specific format
Email must belong to a specific domain
```

For today's workshop, we will keep validation simple.

---

# 🧠 50. Important Concepts to Remember

## Model

A Python class representing the structure of data.

```python
class Student(models.Model):
```

---

## Field

A piece of information stored for each record.

```python
name = models.CharField(max_length=100)
```

---

## Migration

Instructions for changing the database structure.

```bash
python manage.py makemigrations
python manage.py migrate
```

---

## ORM

A way to interact with the database using Python/Django objects.

```python
Student.objects.all()
```

---

## ModelForm

A form connected to a Django model.

```python
class StudentForm(forms.ModelForm):
```

---

## CRUD

The four basic data operations:

```text
Create
Read
Update
Delete
```

---

# 🎯 51. Session 2 Challenge

Now try to improve the application without following the instructor step-by-step.

### Challenge 1 — Add a Student Count

Display something like:

```text
Total Students: 5
```

Hint:

```python
Student.objects.count()
```

---

### Challenge 2 — Add an Actions Column

Your table should look something like:

```text
Name | Email | Faculty | Semester | Actions
------------------------------------------------
John | ...   | ...     | 5        | Edit Delete
Jane | ...   | ...     | 3        | Edit Delete
```

---

### Challenge 3 — Add a "Back to Students" Button

Add navigation from the create/edit pages back to:

```text
/students/
```

---

### Challenge 4 — Improve the UI

Use Bootstrap classes to improve:

* Table
* Form
* Buttons
* Spacing
* Headings
* Alerts

---

# 🧠 52. Think Like a Developer

Don't just memorize:

```python
Student.objects.all()
```

Ask yourself:

> Where did the data come from?

Answer:

```text
SQLite Database
```

Ask:

> How did Django know what the database structure should look like?

Answer:

```text
Student Model
      ↓
Migrations
```

Ask:

> How did the data reach the HTML page?

Answer:

```text
Database
   ↓
ORM
   ↓
View
   ↓
Template
```

Ask:

> How did a user create a new record?

Answer:

```text
HTML Form
   ↓
POST
   ↓
ModelForm
   ↓
Validation
   ↓
Model
   ↓
Database
```

Understanding these connections is more important than memorizing individual lines of code.

---

# 📌 53. Session 2 Summary

In Session 1, we built a basic Django application.

Today, we transformed it into a database-backed application.

### Before Session 2

```text
Browser
   ↓
URL
   ↓
View
   ↓
Static Template
   ↓
Browser
```

### After Session 2

```text
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
```

And we added:

```text
Create
Read
Update
Delete
```

Our Student Management System can now manage actual student records.

---

# 🚀 54. What We Have Built

At the end of Session 2, our application supports:

* ✅ Student Model
* ✅ SQLite Database
* ✅ Migrations
* ✅ Django Admin
* ✅ Superuser
* ✅ Database records
* ✅ Student list
* ✅ ModelForm
* ✅ Form validation
* ✅ CSRF protection
* ✅ Create student
* ✅ Read students
* ✅ Update student
* ✅ Delete student

The application has now moved from:

> **A static website**

to:

> **A dynamic database-backed web application**

---

# 🔜 55. Coming Up in Session 3

Our application is functional, but we still have important things to add.

In **Session 3**, we will turn our project into a more realistic application.

We will cover:

```text
Authentication
      ↓
Login / Logout
      ↓
User Management
      ↓
Git & GitHub
      ↓
Project Version Control
      ↓
Deployment
      ↓
Live Application
```

We will learn how to:

* Add authentication
* Implement login
* Implement logout
* Protect pages
* Work with users
* Use Git
* Push the project to GitHub
* Prepare the project for deployment
* Deploy the Django application

The goal is to finish with a project that is not only working locally, but can be shared with others.

---

# 🏁 Final Session 2 Checklist

Before leaving the session, make sure you can answer **yes** to these questions:

* [ ] Do I understand what a Django Model is?
* [ ] Do I understand what a database does?
* [ ] Do I understand why we are using SQLite?
* [ ] Do I know where `db.sqlite3` is?
* [ ] Can I create a model?
* [ ] Do I understand Django model fields?
* [ ] Do I understand `max_length`?
* [ ] Do I understand `auto_now_add=True`?
* [ ] Do I understand `makemigrations`?
* [ ] Do I understand `migrate`?
* [ ] Can I register a model in Admin?
* [ ] Can I create a superuser?
* [ ] Can I add students through Admin?
* [ ] Can I retrieve students using the ORM?
* [ ] Can I display database records in a template?
* [ ] Do I understand CRUD?
* [ ] Can I create a `ModelForm`?
* [ ] Can I validate submitted data?
* [ ] Do I know why `{% csrf_token %}` is needed?
* [ ] Can I create a student?
* [ ] Can I update a student?
* [ ] Can I delete a student?
* [ ] Can I explain the Django database flow?

If you can check most of these boxes, you're ready for Session 3.

---

# 💡 The Big Idea

Don't leave this session thinking:

> "I learned some Django commands."

Instead, remember this:

```text
MODEL
  ↓
MIGRATION
  ↓
DATABASE
  ↓
ORM
  ↓
VIEW
  ↓
TEMPLATE
  ↓
BROWSER
```

And when a user submits data:

```text
BROWSER
  ↓
FORM
  ↓
POST
  ↓
VIEW
  ↓
MODELFORM
  ↓
VALIDATION
  ↓
DATABASE
```

This is the foundation of building dynamic Django applications.

---

## 🎓 Session 2 Complete

You have taken the Student Management System from a collection of static pages to a real application capable of storing and managing data.

**Next:** Authentication, GitHub & Deployment 🚀

**Session 3 — Turn It Into a Real Application**

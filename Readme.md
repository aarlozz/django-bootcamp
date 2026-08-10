Django Web Development Bootcamp

Build a complete Student Management System with Django — from your first Django project to a working web application.

This repository contains the code, learning guides, exercises, and project progression for a 3-session beginner-friendly Django Web Development Bootcamp designed for university students.

About the Bootcamp

This bootcamp is a hands-on introduction to web development with Django, a Python web framework.

Rather than learning Django through isolated examples, we will build one application throughout the entire bootcamp:

Student Management System

The application starts as a simple Django website and gradually evolves into a dynamic application with a database, CRUD operations, authentication, version control, and deployment.

Project progression
                    Student Management System
                              │
                              ▼
                  ┌───────────────────────┐
                  │       SESSION 1       │
                  │  Django Fundamentals  │
                  └───────────┬───────────┘
                              │
                     URLs + Views
                     Templates + UI
                              │
                              ▼
                  ┌───────────────────────┐
                  │       SESSION 2       │
                  │    Database + CRUD    │
                  └───────────┬───────────┘
                              │
                  Models + ORM + Forms
                    Admin + Validation
                              │
                              ▼
                  ┌───────────────────────┐
                  │       SESSION 3       │
                  │ Authentication + Git  │
                  │ GitHub + Deployment   │
                  └───────────┬───────────┘
                              │
                              ▼
                    Complete Web Application
Bootcamp Roadmap
Session	Topic	Main Focus	Outcome
01	Django Fundamentals	Project, Apps, URLs, Views, Templates	Build the application foundation
02	Database & CRUD	Models, SQLite, ORM, Forms, Admin	Make the application dynamic
03	Authentication, GitHub & Deployment	Auth, Git, GitHub, Deployment	Turn it into a real application
Session 1 — Django Fundamentals
Build Your First Web Application

We begin with the fundamentals of Django.

You will learn how a Django application receives a request, finds the appropriate URL, executes a view, renders a template, and returns a response to the browser.

Topics
What is Django?
Django project vs Django app
Project structure
Virtual environments
Django development server
URL routing
Views
Templates
Template inheritance
Basic MVT architecture
Bootstrap
Navigation
Pages built
/
├── Home
│
├── /about/
│   └── About
│
└── /students/
    └── Students
Start Session 1

👉 Open the Session 1 learning guide

Session 2 — Database & CRUD
Make the Application Dynamic

In Session 2, we take the foundation created in Session 1 and connect it to a database.

The static Students page will become a real student management interface.

Topics
Django Models
SQLite
Migrations
Django ORM
Django Admin
ModelForms
Form validation
CRUD operations

CRUD stands for:

Create
Read
Update
Delete

By the end of Session 2, participants will be able to create, view, update, and delete student records.

🚧 Session 2 documentation will be added here.

Session 3 — Authentication, GitHub & Deployment
Turn It Into a Real Application

The final session takes the application beyond local development.

Topics
Django authentication
Login and logout
User access
Git fundamentals
GitHub workflow
Repository management
Deployment
Preparing a Django application for production

By the end of Session 3, the Student Management System will have progressed from a local learning project to a deployable web application.

🚧 Session 3 documentation will be added here.

Learning Outcomes

After completing the bootcamp, participants should be able to:

Understand the fundamentals of Django.
Create Django projects and apps.
Configure URL routing.
Write Django views.
Create and reuse templates.
Understand basic MVT architecture.
Work with Django models and databases.
Use Django's ORM.
Create forms and validate user input.
Implement CRUD functionality.
Use Django Admin.
Implement basic authentication.
Use Git for version control.
Push a project to GitHub.
Deploy a Django application.
Prerequisites

This bootcamp is designed for beginner-level university students.

You do not need previous Django experience.

Recommended knowledge

Basic familiarity with:

Python
Functions
Variables
HTML
CSS
Command-line/terminal basics
You do not need to know
Django
SQL
REST APIs
React
PostgreSQL
Docker
Advanced JavaScript

Everything required for the bootcamp will be introduced progressively.

Required Software

Before starting the bootcamp, install:

Software	Purpose
Python 3	Programming language
VS Code	Code editor
Web Browser	Testing the application
Git	Version control

Git is optional during Session 1 but will become important in Session 3.

Technology Stack

The bootcamp intentionally uses a simple stack so that beginners can focus on understanding Django.

Backend
Python
Django
Database
SQLite
Frontend
HTML
CSS
Bootstrap
Development Tools
VS Code
Git
GitHub
Deployment

Deployment technology will be introduced in Session 3.

We deliberately do not introduce React, Django REST Framework, Docker, PostgreSQL, or other advanced technologies in this beginner bootcamp.

Repository Structure

The repository is organized by session.

student-management/
│
├── README.md
│
├── session-01/
│   ├── README.md
│   └── ...
│
├── session-02/
│   ├── README.md
│   └── ...
│
└── session-03/
    ├── README.md
    └── ...
What does each README contain?
Root README.md

This file provides:

Bootcamp overview
Roadmap
Project description
Prerequisites
Technology stack
Repository structure
Session navigation

It answers:

"What is this bootcamp and where should I start?"

Session README

Each session contains its own detailed learning guide.

For example:

session-01/README.md

contains the complete Session 1 instructions.

It answers:

"What do I need to do during this session?"

How to Use This Repository

If you are participating in the bootcamp, follow the sessions in order.

Step 1 — Start with Session 1

Open:

session-01/README.md

Follow the instructions from the beginning.

Do not skip the setup steps even if you already have Django installed.

They help establish a consistent environment.

Step 2 — Complete the Session 1 Project

By the end of Session 1, you should have:

Student Management System
│
├── Home
├── About
└── Students

The Students page will still be static.

That is intentional.

Step 3 — Continue to Session 2

Session 2 will build directly on the project from Session 1.

You will add:

Database
   ↓
Models
   ↓
ORM
   ↓
Forms
   ↓
CRUD
Step 4 — Continue to Session 3

Session 3 will build on the database-enabled application.

You will add:

Authentication
      +
Git / GitHub
      +
Deployment
Project Development Philosophy

The application is intentionally developed incrementally.

We do not try to build everything in the first session.

Instead:

Simple
  ↓
Understand
  ↓
Extend
  ↓
Test
  ↓
Improve

This is important when learning web development.

A beginner should understand why each component exists before adding more complexity.

What the Application Will Become

At the beginning:

Home
About
Students

After Session 2:

Students
│
├── View students
├── Add student
├── Edit student
└── Delete student

After Session 3:

Student Management System
│
├── Authentication
│   ├── Login
│   └── Logout
│
├── Dashboard
│
├── Students
│   ├── List
│   ├── Create
│   ├── Update
│   └── Delete
│
└── Deployed Application

The exact feature set may evolve as we build the project.

Session Navigation
Session 1
Django Fundamentals — Build Your First Web Application

Status: Available

👉 Go to Session 1

Session 2
Database & CRUD — Make the Application Dynamic

Status: Coming soon

The Session 2 guide will be added after Session 1 is completed and finalized.

Session 3
Authentication, GitHub & Deployment — Turn It Into a Real Application

Status: Coming soon

The Session 3 guide will be added after Session 2 is completed and finalized.

Bootcamp Schedule

Each session is approximately 3 hours.

Session	Duration
Session 1	~3 hours
Session 2	~3 hours
Session 3	~3 hours
Total	~9 hours

The sessions combine:

Short explanations
Live coding
Guided implementation
Hands-on exercises
Challenges
Troubleshooting
Recap
Recommended Learning Approach

During the workshop:

1. Type the code yourself

Do not simply copy and paste everything.

Typing the code helps you recognize:

Syntax
File structure
Django conventions
Errors
Relationships between files
2. Read the error messages

Errors are a normal part of programming.

When something fails:

Read
 ↓
Understand
 ↓
Locate
 ↓
Fix
 ↓
Run again
3. Experiment

Once the basic implementation works, change small things.

For example:

Change a page title.
Change Bootstrap button styles.
Add text.
Add another navigation link.
Change the layout.

The goal is understanding, not merely reproducing the instructor's code.

Important Scope Note

This bootcamp intentionally avoids advanced Django topics until they are needed.

We will not introduce everything Django can do.

Instead, we will learn the concepts necessary to build our application step by step.

Topics such as:

Django REST Framework
Advanced authentication
Custom user models
APIs
PostgreSQL
Docker
Advanced deployment
Complex frontend frameworks

are outside the initial scope of this bootcamp.

Project Milestones

Track the application as it evolves:

 Django project created
 students app created
 Basic pages working
 Template inheritance implemented
 Bootstrap added
 Navigation implemented
 Database added
 Student model created
 CRUD implemented
 Forms and validation added
 Authentication implemented
 Git repository configured
 GitHub repository created
 Application deployed
Final Goal

By the end of the bootcamp, you should not just have a working Django application.

You should understand how the pieces fit together.

The goal is to move from:

"I followed the tutorial."

to:

"I understand how this Django application works,
and I can build something similar myself."

Getting Started

Ready to begin?

Start with:

Session 1 — Django Fundamentals

You will create your first Django project and build the foundation of the Student Management System from scratch.

License

This repository is intended for educational and workshop purposes.
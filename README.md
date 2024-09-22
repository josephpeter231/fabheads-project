# Django Blog Application

This is a simple blog application built using Django. It provides features to create, read, update, and delete blog posts. The application also includes a REST API for managing blog posts using Django Rest Framework (DRF).

## **Features**

- User authentication for creating, editing, and deleting posts
- Admin interface for managing posts
- REST API endpoints for CRUD operations
- Post listing, detail view, create, edit, and delete functionalities

## **Technologies Used**

- Django
- Django Rest Framework (DRF)
- SQLite (default database)

## **Requirements**

- Python 3.8 or later
- Django 5.1 or the latest version
- Django Rest Framework

## **Installation and Setup**

### 1. Clone the repository
- git clone [https://github.com/josephpeter231/fabheads-project.git](https://github.com/josephpeter231/fabheads-project.git)
- cd blog_project

### 2. Install Dependencies
- pip install django djangorestframework (either in virtual env or globally)

### 3. Run Migrations
- python manage.py makemigrations
- python manage.py migrate

### 4. Create a Superuser
- python manage.py createsuperuser (To view the admin Interface)

### 5. Start the Server
- python manage.py runserver 
  (application can be accessed [http://127.0.0.1:8000/](http://127.0.0.1:8000/))

## **Application Features**

### Blog Posts
- Create: Navigate to /posts/new/ and fill out the form to create a new post.
- Read: View all posts at /posts/ or view a specific post at /posts/<slug>/.
- Update: Edit a post you created by going to /posts/<slug>/edit/.
- Delete: Delete a post by going to /posts/<slug>/delete/.
- Only respective authors can edit or delete the post.

# BlogForge

A Django REST Framework API for managing blog posts with authentication, CRUD operations, filtering, search, ordering, and pagination.

## Features

- Create blog posts
- Read blog posts
- Update blog posts
- Delete blog posts
- Authentication
- User-specific posts
- Search
- Filtering
- Ordering
- Pagination
- Django admin interface

## Tech Stack

- Python
- Django
- Django REST Framework
- django-filter
- SQLite

## Project Structure

```text
BlogForge/
├── blog/
│   ├── settings.py
│   ├── urls.py
│   ├── asgi.py
│   └── wsgi.py
│
├── helloworld/
│   ├── migrations/
│   ├── models.py
│   ├── serializers.py
│   ├── views.py
│   ├── filters.py
│   ├── pagination.py
│   ├── permissions.py
│   ├── urls.py
│   └── admin.py
│
├── manage.py
├── requirements.txt
├── .gitignore
└── README.md
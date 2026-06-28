# Django Application

This folder contains the Django version of the Academic Tracking Application.

## What this app does

- Manages learners, subjects, competencies, and assessment tasks
- Records learner results and feedback
- Shows dashboard and report pages for academic tracking
- Supports role-based behavior for users

## Project structure

- `manage.py` - Django management entry point
- `school_portal/` - Project settings and URL configuration
- `core/` - Main application logic (models, views, forms, templates)
- `templates/registration/` - Authentication templates (for example login)
- `db.sqlite3` - Local SQLite database file

## Requirements

- Python 3.10+ (recommended)
- pip

## Quick start (Windows PowerShell)

From this folder (`django-application`):

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver
```

Then open: http://127.0.0.1:8000/

## Helpful commands

```powershell
python manage.py createsuperuser
python manage.py test
python manage.py makemigrations
python manage.py migrate
```

## Notes

- Static file styling is in `core/static/core/style.css`
- Main HTML templates are in `core/templates/core/`
- The app uses SQLite by default for local development

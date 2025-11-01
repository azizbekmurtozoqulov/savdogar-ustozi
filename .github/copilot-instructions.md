## Repo snapshot

- Django project (Django 5.x used when scaffolded). Project root: `manage.py` + `project1/` (settings, urls, wsgi).
- Main app: `news_app/` (models, views, forms, urls, templates under `templates/`), DB: `db.sqlite3`.
- Uses a `Pipfile` (Python 3.13, pillow listed). Static assets in `static/`, media in `media/` (see `project1/settings.py`).

## What an AI agent should know up front

- Run & test environment: this repo uses a Pipfile — prefer using pipenv or a virtualenv with Python 3.13 to match the declared runtime.
  - Example (PowerShell):

```powershell
pipenv install      # installs packages from Pipfile
pipenv shell        # activate venv
python manage.py migrate
python manage.py runserver
```

- Quick facts pulled from code:
  - `project1/settings.py` sets `MEDIA_ROOT = <BASE_DIR>/media` and `STATICFILES_DIRS = [BASE_DIR / "static"]`.
  - `news_app/models.py` defines `News`, `Category`, `Contact`, `Resume`. `News` uses an ImageField upload path `news/images`.
  - Views reference `News.published` (e.g., `News.published.all()`), but no `published` manager is defined in `news_app/models.py` — watch for missing custom manager.
  - `STATIC_ROOT` contains an extra trailing space string (`'staticfiles '`), which looks like a bug. Prefer `os.path.join(BASE_DIR, 'staticfiles')`.

## Coding guidance (concise, actionable)

- When changing models:
  - Update `news_app/models.py` and run `python manage.py makemigrations` then `migrate`.
  - If you add a `published` manager, implement it in `News` (custom Manager or QuerySet) and confirm views using `News.published` work.

- Templates & static files:
  - Templates directory: `templates/` (configured in `TEMPLATES['DIRS']`).
  - Static files: `static/` (served during development by runserver). Media files are stored in `media/` with `MEDIA_URL = 'media/'`.
  - When updating image upload paths, remember to run collectstatic only when deploying and fix `STATIC_ROOT` first.

- Tests & running:
  - Unit tests live in `news_app/tests.py`. Run tests with `python manage.py test` (from venv).
  - Use `python manage.py runserver` for local development.

## Patterns and gotchas specific to this repo

- Duplicate view names and functions: `views.py` contains multiple `contact` and `resume` definitions in different places — be careful when editing or referencing them; unify duplicates.
- Missing custom manager: views call `News.published` but the manager isn't in `models.py` — search for `published` across the repo before assuming it exists.
- Settings anomalies:
  - `SECRET_KEY` is present (development use only). `DEBUG = True`.
  - `STATIC_ROOT` has a trailing space (likely unintended). Fix before running collectstatic.

## Useful file references (examples the agent can open immediately)

- `project1/settings.py` — runtime, static/media config, templates dir.
- `news_app/models.py` — model shapes (Category, News, Contact, Resume) and image fields.
- `news_app/views.py` — how pages are wired and which managers/views are assumed.
- `manage.py` — standard Django entrypoint; use it for migrations, tests, server.
- `Pipfile` — Python version (3.13) and an explicit dependency on `pillow`.

## When you change code: a tiny contract

- Inputs: code edits (models/views/templates). Outputs: migrations (if models change), passing test run, and manual verification of pages that rely on the change.
- Error modes to catch: missing managers (AttributeError), template variable errors (TypeError/KeyError), static/media path problems.

## If unsure or blocked

- Search for `published` or similar managers first (views expect `News.published`).
- Use `python manage.py shell` to inspect models at runtime (e.g., check `News._meta` and available managers).

---

If you want, I can:
- add a quick fix PR for the `STATIC_ROOT` trailing-space issue;
- implement a simple `published` manager on `News` and add a minimal test.

Please tell me which of those (if any) you'd like me to do next.

# Statistics about the majors world companies

## How to launch Backend (Windows)

First rename .env.example to .env and fill the variable `DJANGO_SECRET_KEY` with the secret key of your choice.

Then open a terminal and run the following commands:

```bash
cd backend
```
```bash
py -m venv .venv
```
```bash
.venv/Scripts/activate
```
```bash
pip install -r requirements.txt
```
```bash
py manage.py makemigrations
```
```bash
py manage.py migrate
```
```bash
py manage.py fill_database
```
```bash
py manage.py runserver
```

You can now access the API at:
http://127.0.0.1:8000/api/company

and apply your filters:
http://127.0.0.1:8000/api/company?country=france

You can also access the documentation at:
http://127.0.0.1:8000/api/docs
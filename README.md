--- FILE: README.md ---
# AI-SAER Web Application (Flask)


This app is a full-stack scaffold for the AI-Powered Sentinel for Aquatic Ecosystem Resilience (AI-SAER).


## Features
- User registration and login
- Admin interface to manage users, sensor data, and pollution events
- REST API to ingest sensor/time-series readings and to submit detected pollution events
- Role-based access (admin vs user)
- SQLite default database (switch to Postgres by changing DATABASE_URL)
- Placeholders to integrate CNN models and anomaly detection


## Quickstart (local)
1. Create a virtualenv and install requirements:


```bash
python -m venv venv
source venv/bin/activate # Windows: venv\Scripts\activate
pip install -r requirements.txt
```


2. Run the app (creates `ai_saer.db` automatically):


```bash
export FLASK_APP=app.py
export FLASK_ENV=development
flask run
```


3. Create an admin user:


```bash
python app.py create-admin --username admin --password AdminPass123
```


Open http://127.0.0.1:5000
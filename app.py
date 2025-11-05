"""
Single-file Flask application. Contains models, auth, admin, API endpoints, and templates.
This file is intentionally self-contained for quick testing. In production, split into
modules, add migrations, and move secret config to environment variables.
"""
import os
import sys
import argparse
from datetime import datetime
from flask import Flask, render_template, redirect, url_for, request, flash, jsonify, abort
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager, UserMixin, login_user, login_required, logout_user, current_user
from flask_admin import Admin
from flask_admin.contrib.sqla import ModelView
from werkzeug.security import generate_password_hash, check_password_hash


BASE_DIR = os.path.abspath(os.path.dirname(__file__))
DB_PATH = os.environ.get('DATABASE_URL') or 'sqlite:///' + os.path.join(BASE_DIR, 'ai_saer.db')


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = DB_PATH
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY', 'dev-secret-key-change-me')


db = SQLAlchemy(app)
login_manager = LoginManager(app)
login_manager.login_view = 'login'


# -----------------
# Models
# -----------------
class User(db.Model, UserMixin):
id = db.Column(db.Integer, primary_key=True)
username = db.Column(db.String(80), unique=True, nullable=False)
email = db.Column(db.String(120), unique=True, nullable=True)
password_hash = db.Column(db.String(128), nullable=False)
role = db.Column(db.String(20), default='user') # 'user' or 'admin'
created_at = db.Column(db.DateTime, default=datetime.utcnow)


def set_password(self, password):
self.password_hash = generate_password_hash(password)


def check_password(self, password):
return check_password_hash(self.password_hash, password)


def is_admin(self):
return self.role == 'admin'


class SensorReading(db.Model):
id = db.Column(db.Integer, primary_key=True)
sensor_id = db.Column(db.String(64), nullable=False)
timestamp = db.Column(db.DateTime, default=datetime.utcnow)
latitude = db.Column(db.Float, nullable=True)
longitude = db.Column(db.Float, nullable=True)
ph = db.Column(db.Float, nullable=True)

dissolved_oxygen = db.Column(db.Float, nullable=True)

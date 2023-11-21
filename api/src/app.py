from flask import Flask, jsonify, request, redirect, url_for, render_template_string
from flask_login import LoginManager, UserMixin, login_user, login_required, logout_user, current_user
from werkzeug.security import check_password_hash, generate_password_hash

app = Flask(__name__)

from asgiref.wsgi import WsgiToAsgi

asgi_app = WsgiToAsgi(app)

print("App initialized")
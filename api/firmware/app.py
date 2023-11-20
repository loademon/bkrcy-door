from flask import Flask, jsonify
app = Flask(__name__)

from asgiref.wsgi import WsgiToAsgi
asgi_app = WsgiToAsgi(app)
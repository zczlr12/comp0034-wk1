from flask import Flask
from markupsafe import escape

app = Flask(__name__)

@app.route('/<name>')
def home(name):
    return f'Hello {escape(name)} and welcome to my paralympics app'
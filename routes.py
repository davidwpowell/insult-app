import os
from flask import flask

app = Flask(__name__)
# Keeps Flask from swalowing error messages
app.config['PROPAGATE_EXCEPTIONS'] = True

@app.route("/")
def insult():
    return "Hello, Ryan the Butt-licker"

if __name__ == "__main__":
    app.run()

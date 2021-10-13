# Import dependencies
from flask import Flask, app

# Create a new Flask instance
app = Flask(__name__)

# Create Flask Routes
@app.route('/')
def hello_world():
    return 'Hello world'
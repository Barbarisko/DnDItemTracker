from Loging import configure_logging
configure_logging()

from flask import Flask, request
app = Flask(__name__)

from APIHandlers.UserAPI import *
from APIHandlers.CharacterAPI import *

@app.route("/")
def index():
    return "Send Boobs"

# @app.route('/api/item/<int:id>plus_text', methods=['GET', 'POST'])
# def func_with_id(id):
#     return { "new_id": id}


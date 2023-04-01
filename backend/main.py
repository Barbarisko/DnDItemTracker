import Constants

from flask import Flask
app = Flask(__name__)


@app.route("/")
def index():
    print("Hi Mom")
    global counter
    counter += 1
    return "Send Boobs" + str(counter)

app.add_url_rule("/", view_func=index)


# app.run()
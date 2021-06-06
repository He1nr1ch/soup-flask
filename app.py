from flask import Flask
from flask import render_template
import steam as status

app = Flask(__name__)


@app.route("/")
def hello_world():
    status.Misha()
    return render_template("default.html")

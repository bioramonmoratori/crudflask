from app import app
from flask import render_template

@app.route("/index")
@app.route("/")
def index():
    return "Hello World"

@app.route("/ola/", methods = ["GET"])
@app.route("/ola/<name>", methods = ["GET"])
def test(name = None):

    return render_template("blog.html", name = name)

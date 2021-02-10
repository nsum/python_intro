import os
from flask import Flask, render_template
# render_template is used for html rendering
# Capital F means it's a class
# Always create an instance of class like below
app = Flask(__name__)
# __name__ is built-in


# Below decorator makes the page go to index.html when there's / at the end
@app.route("/")
# This gets called from html files (in nav)
def index():
    # Below return can be used, but it's too long to write
    # return "<h1>Hello,</h1> <h2>World<h2>"
    # That's why we use render_template which takes tamplate from template dir
    return render_template("index.html")
    # Flask expects templates to be in dir "templates" in same dir as first.py


# Below decorator leads to about page
@app.route("/about")
def about():
    return render_template("about.html")


@app.route("/contact")
def contact():
    return render_template("contact.html")


@app.route("/careers")
def careers():
    return render_template("careers.html")


if __name__ == "__main__":
    app.run(
        host=os.environ.get("IP", "0.0.0.0"),
        port=int(os.environ.get("PORT", "5000")),
        debug=True)

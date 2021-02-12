import os
import json
# import json because we need it to run below code in about fun that uses json
from flask import Flask, render_template, request, flash
# render_template is used for html rendering
# Capital F means it's a class
# request is used for form in contact.html
# request finds the method we use, and contains our form object when we post it
# flash is used for displaying flash short messages, used after form submit
# Below if is explained in env.py
# Saving after adding below if will create pycache folder
# That folder should be added to gitignore together with env.py
if os.path.exists("env.py"):
    import env

# Always create an instance of class like below
app = Flask(__name__)
# __name__ is built-in

# Below is used to display flash message after form submit
app.secret_key = os.environ.get("SECRET_KEY")


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
    data = []
    with open("data/company.json", "r") as json_data:
        data = json.load(json_data)
        # Above 3 lines open json file as var json_data & loads it in var data
        # data is then assigned to var company here below
        # and then company var is used in about.html between {{}}

    return render_template("about.html", page_title="About", company=data)
    # page_title var injects its value where we call that var between {{}}
    # ref top of about page for relationship

# This is used for company info to open in
# member.html when name is clicked in about.html


@app.route("/about/<member_name>")
def about_member(member_name):
    member = {}
    with open("data/company.json", "r") as json_data:
        data = json.load(json_data)
        for obj in data:
            if obj["url"] == member_name:
                member = obj
    return render_template("member.html", member=member)
    # first member is var being passed into member.html
    # second member is object created in about_member fun


# methods is added in order to contact form to work
# even if we use just one method, we still name our list methodS
@app.route("/contact", methods=["GET", "POST"])
def contact():
    # if flashes a message after form submit
    if request.method == "POST":
        flash("Thanks {}, we have received your message!" .format(
            request.form.get("name")))
    # Below line is unrelated to if statement
    return render_template("contact.html", page_title="Contact")


@app.route("/careers")
def careers():
    return render_template("careers.html", page_title="Careers")


if __name__ == "__main__":
    app.run(
        host=os.environ.get("IP", "0.0.0.0"),
        port=int(os.environ.get("PORT", "5000")),
        debug=True)

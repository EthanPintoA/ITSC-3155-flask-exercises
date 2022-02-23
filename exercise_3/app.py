from flask import Flask, render_template, request

app = Flask(__name__)

registrant_DB = {}
VALID_ORGANIZATIONS = (
    "Charlotte Hack",
    "Code9",
    "CompSci Club",
    "Cool Coders",
    "Pragmatic Programmers",
)


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/registrants", methods=["GET", "POST"])
def registrants():
    name = request.form.get("name", "")
    organization = request.form.get("organization", "")
    print(organization)
    if name != "" and organization != "" and organization in VALID_ORGANIZATIONS:
        registrant_DB[name] = organization
    return render_template("registrants.html", registrant_DB=registrant_DB)

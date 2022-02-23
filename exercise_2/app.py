from flask import Flask, render_template, request

app = Flask(__name__)


@app.get("/")
def index():
    return render_template("index.html")


@app.get("/calculate")
def calculate():
    number = request.args.get("number", "")
    calculation: str

    if number == "":
        calculation = "No number provided!"
    elif number.isdecimal():
        parity = "even" if int(number) % 2 == 0 else "odd"
        calculation = f"{number} is {parity}"
    else:
        calculation = f"{number} is not an integer!"

    return render_template("calculate.html", calculation=calculation)

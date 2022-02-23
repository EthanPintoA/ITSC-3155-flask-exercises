from datetime import datetime

from flask import Flask, render_template

app = Flask(__name__)


@app.get("/")
def index():
    return render_template(
        "index.html", datetime=datetime.now().strftime("%A, %B %d %Y %H:%M:%S")
    )

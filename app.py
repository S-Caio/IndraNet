from flask import Flask, render_template, request

app = Flask(__name__)    

@app.route("/")
def index():
    return render_template("login.html")

@app.route("/profile", methods=["POST"])
def greet():
    name = request.form.get("name")
    return render_template("profile.html", placeholder = name)
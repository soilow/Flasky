from flask import Flask, request, redirect, abort, render_template
from flask_bootstrap import Bootstrap

app = Flask(__name__)
bootstrap = Bootstrap(app)

@app.route("/")
def index():
	return render_template("index.html")

@app.route("/user/<name>")
def user(name):
	if name == "windows":
		abort(404)

	user_agent = request.headers.get("User-Agent")
	return render_template("user.html", name=name, user_agent=user_agent)

@app.route("/division")
def a():
	a = 0
	return 1 / a

@app.route("/apple")
def apple():
	return redirect("https://apple.com")

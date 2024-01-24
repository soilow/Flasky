from flask import Flask, request, redirect, abort, render_template, url_for, session, flash
from flask_bootstrap import Bootstrap
from flask_moment import Moment
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired

from datetime import datetime

app = Flask(__name__)
app.config['SECRET_KEY'] = "adidas++"
bootstrap = Bootstrap(app)
moment = Moment(app)

class NameForm(FlaskForm):
	name = StringField("What is your name?", validators=[DataRequired()])
	submit = SubmitField("Submit")


@app.errorhandler(404)
def page_not_found(e):
	return render_template("404.html"), 404

@app.errorhandler(500)
def internal_server_error(e):
	return render_template("500.html"), 500

@app.route("/", methods = ['GET', 'POST'])
def index():
	form = NameForm()
	if form.validate_on_submit():
		old_name = session.get('name')
		if old_name is not None and old_name != form.name.data:
			flash("Looks like you have changed your name!")

		session['name'] = form.name.data
		return redirect(url_for('index'))

	return render_template("index.html", form=form, name=session.get("name"), current_time=datetime.utcnow())

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

from flask import Flask, render_template, session, redirect, url_for, flash
from flask import request
from flask_bootstrap import Bootstrap
from flask_moment import Moment
from datetime import datetime
from main.forms import NameForm

app = Flask(__name__)
app.config['SECRET_KEY'] = "fduaihduishfduiasfydiwshfbuidsdshuaifyaiusdui"  # 密匙
bootstrap = Bootstrap(app)  # init bootstrap
moment = Moment(app)


@app.route('/', methods=["GET", "POST"])
def hello_world():
    form = NameForm()
    if form.validate_on_submit():
        old_name = session.get("name")
        if (not old_name) and (old_name != form.name.data):
            flash("submit name changed!")
        session["name"] = form.name.data
        # return redirect(url_for("hello_world"))
        return redirect("/")
    return render_template("index.html", current_time=datetime.utcnow(), form=form, name=session.get("name"))


@app.route("/index")
def index():
    user_agent = request.headers.get("User-agent")
    return "<p>Your browser is {}</p>".format(user_agent)


@app.route("/user/<name>")
def user(name):
    """渲染模板"""
    return render_template("user.html", name=name)


@app.errorhandler(404)
def page_not_found(e):
    return render_template("404.html"), 404


@app.errorhandler(500)
def page_not_found(e):
    return render_template("500.html"), 500


if __name__ == '__main__':
    app.run(port=5000, debug=False)

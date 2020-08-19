from flask import Flask, render_template
from flask import request
from flask_bootstrap import Bootstrap
from flask_moment import Moment
from datetime import datetime

app = Flask(__name__)
bootstrap = Bootstrap(app)  # init bootstrap
moment = Moment(app)


@app.route('/')
def hello_world():
    return render_template("index.html", current_time=datetime.utcnow())


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

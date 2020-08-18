from flask import Flask, render_template
from flask import request

app = Flask(__name__)


@app.route('/')
def hello_world():
    user_agent = request.headers.get("User-agent")
    return "<p>Your browser is {}</p>".format(user_agent), 400


@app.route("/index")
def index():
    user_agent = request.headers.get("User-agent")
    return "<p>Your browser is {}</p>".format(user_agent)


# @app.route("/user/<name>")
# def user(name):
#     """动态路由"""
#     return "<h1>Hello {}!</h1>".format(name)

@app.route("/user/<name>")
def user(name):
    """渲染模板"""
    return render_template("user.html", name=name)


if __name__ == '__main__':
    app.run(port=5000, debug=False)

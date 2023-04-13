from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/")
def home():
    user_agent = request.user_agent
    if user_agent.platform == 'android' or user_agent.platform == 'iphone' or user_agent.platform == 'ipad':
        return render_template('mobile.html')
    else:
        return render_template("home.html")

@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/play")
def play():
    return render_template("play.html")



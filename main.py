from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/")
def home():
    user_agent = request.headers.get('User-Agent')
    user_agent = user_agent.lower()

    if "iphone" in user_agent:
        return render_template('mobile.html')
    elif "android" in user_agent:
        return render_template('mobile.html')
    elif "ipad" in user_agent:
        return render_template('mobile.html')
    else:
        return render_template("home.html")

@app.route("/about")
def about():
    user_agent = request.headers.get('User-Agent')
    user_agent = user_agent.lower()

    if "iphone" in user_agent:
        return render_template('mobile.html')
    elif "android" in user_agent:
        return render_template('mobile.html')
    elif "ipad" in user_agent:
        return render_template('mobile.html')
    else:
        return render_template("about.html")

@app.route("/play")
def play():
    user_agent = request.headers.get('User-Agent')
    user_agent = user_agent.lower()

    if "iphone" in user_agent:
        return render_template('mobile.html')
    elif "android" in user_agent:
        return render_template('mobile.html')
    elif "ipad" in user_agent:
        return render_template('mobile.html')
    else:
        return render_template("play.html")

app.run()
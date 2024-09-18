from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

# @app.route("/search")
# def search():
#     q = request.args.get("q")
#     fetch("https://google.com/search?q=" + q)
        
#     return render_template("search.html", html=html)

# @app.route("/lucky_search")
# def lucky_search():
#     q = request.args.get("q")
    # fetch("https://google.com/search?q=" + q + "&btnl")


@app.route("/image")
def image():
    return render_template("image.html")

@app.route("/advanced")
def advanced():
    return render_template("advanced.html")
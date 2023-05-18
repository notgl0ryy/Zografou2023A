from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<h1>Hello World -_-</h2>"

@app.route("/about")
def about():
    return '''<h1>About page</h1>
    <p>This page is about us</p>'''

@app.route("/robot")
def robot():
    return render_template("static.html")

if __name__ == "__main__":
    app.run(debug=True)

    
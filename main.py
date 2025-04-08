from lib2to3.fixes.fix_input import context

from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def films():
    context = {
        "link": "Узнать о фильме"
    }
    return render_template("index.html", **context)


@app.route("/person/")
def person():
    context = {
        "link": "Узнать о персонаже"
    }
    return render_template("main.html", **context)

if __name__ == "__main__":
    app.run()


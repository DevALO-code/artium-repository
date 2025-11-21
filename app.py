from flask import render_template, Flask

app = Flask(__name__)


@app.route("/")
def index() -> str:
    return render_template("index.html")


@app.route("/about-us")
def aboutUs() -> str:
    return render_template("aboutus.html")


# Expos
@app.route("/exposiciones/avant-garde")
def expoAvantGarde() -> str:
    return render_template("articles/avant-garde.html")


if __name__ == "__main__":
    app.Run(debug=True)

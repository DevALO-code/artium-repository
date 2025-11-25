from flask import render_template, Flask

app = Flask(__name__)


@app.route("/")
def index() -> str:
    return render_template("index.html")


@app.route("/about-us")
def aboutUs() -> str:
    return render_template("aboutus.html")


@app.route("/sugerencias")
def sugerencias() -> str:
    return render_template("sugerencias.html")

# Expos


@app.route("/exposiciones/avant-garde")
def expoAvantGarde() -> str:
    return render_template("articles/avant-garde.html")


@app.route("/exposiciones/automotriz")
def expoAutomotriz() -> str:
    return render_template("articles/automotriz.html")


@app.route("/exposiciones/ukiyo-e")
def expoUkiyo() -> str:
    return render_template("articles/ukiyo-e.html")


@app.route("/exposiciones/torture")
def expoTorture() -> str:
    return render_template("articles/torture.html")


if __name__ == "__main__":
    app.Run(debug=True)

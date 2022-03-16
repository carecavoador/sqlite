from flask import Flask, render_template, redirect

nomes = [
    ("Everton", "99999-9999", "Blumenau"),
    ("Priscila", "88888-8888", "São João"),
    ("Maria", "98888-7777", "Brusque")
]


# Flask App >------------------------------------------------------------------
app = Flask(__name__)


# Routes >---------------------------------------------------------------------
@app.route("/agenda")
def index():
    return render_template("index.html", agenda=nomes)


# Main >-----------------------------------------------------------------------
if __name__ == "__main__":
    app.run(debug=True)

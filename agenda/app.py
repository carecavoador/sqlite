from flask import Flask, render_template, redirect
from flask_sqlalchemy import SQLAlchemy

nomes = [
    ("Everton", "99999-9999", "Blumenau"),
    ("Priscila", "88888-8888", "São João"),
    ("Maria", "98888-7777", "Brusque")
]


# Flask App >------------------------------------------------------------------
app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///agenda.sqlite"
db = SQLAlchemy(app)

class Contato(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	nome = db.Column(db.String, nullable=False)
	telefone = db.Column(db.String, nullable=False)
	cidade = db.Column(db.String)


# Routes >---------------------------------------------------------------------
@app.route("/agenda")
def index():
    return render_template("index.html", agenda=nomes)


# Main >-----------------------------------------------------------------------
if __name__ == "__main__":
    app.run(debug=True)

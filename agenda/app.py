from flask import Flask, render_template, redirect
from flask_sqlalchemy import SQLAlchemy


# Flask App >------------------------------------------------------------------
app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///db/agenda.sqlite"
db = SQLAlchemy(app)


# DB Models >------------------------------------------------------------------
class Contato(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String, nullable=False)
    telefone = db.Column(db.String, nullable=False)
    cidade = db.Column(db.String)
    # telefones = db.relationship("Telefone", backref="pessoa", lazy=True)
    
    def __repr__(self):
        return f"Contato('{self.nome}', '{self.cidade}')"


class Telefone(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    numero = db.Column(db.Integer, nullable=False)
    id_contato = db.Column(db.Integer, db.ForeignKey("contato.id"), nullable=False)


# Routes >---------------------------------------------------------------------
@app.route("/agenda")
def index():
    nomes = [contato for contato in Contato.query.all()]
    return render_template("index.html", agenda=nomes)


# Main >-----------------------------------------------------------------------
if __name__ == "__main__":
    app.run(debug=True)

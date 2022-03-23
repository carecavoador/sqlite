from flask import Flask, render_template, redirect, request
from flask_sqlalchemy import SQLAlchemy


# Flask App >------------------------------------------------------------------
app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///db/coletas.sqlite"
db = SQLAlchemy(app)


# DB Models >------------------------------------------------------------------
class Coletas(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    coleta = db.Column(db.String, nullable=False)
    local = db.Column(db.String, nullable=False)
    usuario = db.Column(db.String, nullable=False)

    def __repr__(self):
        return f"Coleta('{self.id}', '{self.coleta}' em '{self.local}')"


# Routes >---------------------------------------------------------------------
@app.route("/")
def index():
    coletas = [coleta for coleta in Coletas.query.all()]
    return render_template("index.html", coletas=coletas)


@app.route("/adicionar", methods=["POST"])
def adicionar():
    coleta = request.form.get("nova_coleta")
    local = request.form.get("novo_local")
    usuario = request.form.get("novo_usuario")
    nova_coleta = Coletas(coleta=coleta, local=local, usuario=usuario)
    db.session.add(nova_coleta)
    db.session.commit()
    return redirect("/")


@app.route("/apagar", methods=["POST"])
def apagar():
    id_coleta = request.form.get("id_coleta")
    apagar_coleta = Coletas.query.filter_by(id=id_coleta).first()
    db.session.delete(apagar_coleta)
    db.session.commit()
    return redirect("/")


# Main >-----------------------------------------------------------------------
if __name__ == "__main__":
    app.run(debug=True)

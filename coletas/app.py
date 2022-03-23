from flask import Flask, render_template, redirect, request, send_file
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
# from io import StringIO


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
    data = db.Column(db.DateTime, default=datetime.utcnow)

    def __repr__(self):
        return f"Coleta('{self.id}', '{self.coleta}' em '{self.local}')"


# Routes >---------------------------------------------------------------------
@app.route("/")
def index():
    coletas = [coleta for coleta in Coletas.query.all()]
    return render_template("index.html", coletas=coletas)

@app.route("/adicionar", methods=["GET", "POST"])
def adicionar():
    coleta = request.form.get("nova_coleta")
    local = request.form.get("novo_local")
    usuario = request.form.get("novo_usuario")
    nova_coleta = Coletas(coleta=coleta, local=local, usuario=usuario)
    db.session.add(nova_coleta)
    db.session.commit()
    return redirect("/")

@app.route("/apagar/<int:id_coleta>")
def apagar(id_coleta):
    apagar_coleta = Coletas.query.filter_by(id=id_coleta).first()
    db.session.delete(apagar_coleta)
    db.session.commit()
    return redirect("/")

@app.route("/editar/<int:id_coleta>", methods=["GET", "POST"])
def editar(id_coleta):
    editar_coleta = Coletas.query.get_or_404(id_coleta)
    if request.method == "POST":
        editar_coleta.coleta = request.form["edita_coleta"]
        editar_coleta.local = request.form["edita_local"]
        db.session.commit()
        return redirect("/")
    else:
        return render_template("editar.html", coleta=editar_coleta)

# @app.route("/envia")
# def envia():
#     coletas = [coleta for coleta in Coletas.query.all()]
#     strIO = StringIO()
#     strIO.write(render_template("index.html", coletas=coletas))
#     strIO.seek(0)
#     with open('teste.txt', 'w') as arquivo:
#         buffer = strIO.getvalue()
#         buffer.encode('utf8')
#         arquivo.write(buffer)
#     return redirect("/")


# Main >-----------------------------------------------------------------------
if __name__ == "__main__":
    app.run(debug=True)

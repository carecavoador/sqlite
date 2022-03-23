from app import db

# DB Models >------------------------------------------------------------------
class Coletas(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    coleta = db.Column(db.String, nullable=False)
    local = db.Column(db.String, nullable=False)
    usuario = db.Column(db.String, nullable=False)
    data = db.Column(db.DateTime, default=datetime.utcnow)

    def __repr__(self):
        return f"Coleta('{self.id}', '{self.coleta}' em '{self.local}')"
from . import db


class Disciplina(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(100), nullable=False)
    semestre = db.Column(db.Integer, nullable=False)

    def __repr__(self):
        return f'<Disciplina {self.nome}>'

from flask_wtf import FlaskForm
from wtforms import StringField, RadioField, SubmitField
from wtforms.validators import DataRequired, Length


class DisciplinaForm(FlaskForm):

    nome = StringField(
        'Nome da disciplina',
        validators=[
            DataRequired(),
            Length(1, 100)
        ]
    )

    semestre = RadioField(
        'Semestre',
        choices=[
            (1, '1º semestre'),
            (2, '2º semestre'),
            (3, '3º semestre'),
            (4, '4º semestre'),
            (5, '5º semestre'),
            (6, '6º semestre')
        ],
        coerce=int,
        validators=[DataRequired()]
    )

    submit = SubmitField('Cadastrar')

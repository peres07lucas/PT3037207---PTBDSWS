import os

basedir = os.path.abspath(os.path.dirname(__file__))


class Config:
    SECRET_KEY = 'chave-secreta-flasky'

    STUDENT_NAME = 'Lucas Peres Gomes'
    STUDENT_ID = 'PT3037207'

    SQLALCHEMY_DATABASE_URI = (
        'sqlite:///' + os.path.join(basedir, 'disciplinas.sqlite')
    )

    SQLALCHEMY_TRACK_MODIFICATIONS = False
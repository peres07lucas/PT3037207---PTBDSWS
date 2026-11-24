
from flask import render_template, redirect, url_for, flash, request
from datetime import datetime

from . import main
from .forms import DisciplinaForm
from app import db
from app.models import Disciplina


@main.route('/')
def index():
    data_hora = datetime.now().strftime(
        '%B %d, %Y %I:%M %p'
    )

    pagina = request.args.get('pagina')

    return render_template(
        'index.html',
        data_hora=data_hora,
        pagina=pagina
    )


@main.route('/disciplinas', methods=['GET', 'POST'])
def disciplinas():
    form = DisciplinaForm()

    if form.validate_on_submit():
        disciplina = Disciplina(
            nome=form.nome.data,
            semestre=form.semestre.data
        )

        db.session.add(disciplina)
        db.session.commit()

        flash('Disciplina cadastrada com sucesso!')

        return redirect(url_for('main.disciplinas'))

    disciplinas = Disciplina.query.order_by(
        Disciplina.id
    ).all()

    return render_template(
        'disciplinas.html',
        form=form,
        disciplinas=disciplinas
    )

from flask import Blueprint, render_template, redirect, url_for, request
from database import Establishment, Session

establishment_blueprint = Blueprint('establishment', __name__)

@establishment_blueprint.route("/create", methods=['POST'])
def create_establishment():
    nome_estabelecimento = request.form.get('nome')
    email_estabelecimento = request.form.get('email')

    session = Session()
    existing_establishment = session.query(Establishment).filter_by(email_estabelecimento=email_estabelecimento).first()

    if existing_establishment:
        return render_template("erroremail.html")

    new_establishment = Establishment(nome_estabelecimento=nome_estabelecimento, email_estabelecimento=email_estabelecimento)
    session.add(new_establishment)
    session.commit()

    return redirect(url_for('establishment.thanks'))

@establishment_blueprint.route("/thanks", methods=['GET'])
def thanks():
    return render_template("thanks.html")
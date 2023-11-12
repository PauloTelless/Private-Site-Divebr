from flask import Flask, request, redirect, url_for, render_template
from database import Establishment, Session 

app = Flask(__name__, template_folder="templates", static_folder="static")

# Rota para criar um estabelecimento 
@app.route("/establishment/create", methods=['POST'])
def create_establishment():
    nome_estabelecimento = request.form.get('nome')
    email_estabelecimento = request.form.get('email')

    session = Session()
    existing_establishment = session.query(Establishment).filter_by(email_estabelecimento=email_estabelecimento).first() #query para filtrar se o email já é cadastrado

    if existing_establishment:
        # retorna para uma página de erro e depois é retornado para a landing page
        return render_template("erroremail.html")

    new_establishment = Establishment(nome_estabelecimento=nome_estabelecimento, email_estabelecimento=email_estabelecimento)
    session.add(new_establishment)
    session.commit()

    # Redireciona para a página de agradecimento
    return redirect(url_for('thanks'))

# Página de agradecimento
@app.route("/registeredsuccess", methods=['GET'])
def thanks():
    return render_template("thanks.html")

if __name__ == "__main__":
    app.run(debug=True)
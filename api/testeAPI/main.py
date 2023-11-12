from flask import Flask, request, redirect, url_for, render_template
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from database import Base, Establishment

app = Flask(__name__, template_folder="templates", static_folder="static")

# Configuração do SQLAlchemy
engine = create_engine('mysql+pymysql://root:@localhost:3306/establishment', echo=True) #Instância criada para fazer as configurações do SQLAlchemy
Base.metadata.create_all(engine)  # Cria todas a tabelas definidas em database.py
Session = sessionmaker(bind=engine) #Cria uma sessão de objetos

# Essa rota é onde irá ser criado um estabelecimento 
@app.route("/establishment/create", methods=['POST'])
def create_establishment():
    nome_estabelecimento = request.form.get('nome') #Pega a informação do input do HTML (nome)
    email_estabelecimento = request.form.get('email')#Pega a informação do input do HTML (email)

    session = Session() #Session é a que vai fazer a interação com o banco de dados.
    new_establishment = Establishment(nome_estabelecimento=nome_estabelecimento, email_estabelecimento=email_estabelecimento) # cria uma instância do estabelecimento (class Establishment)
    session.add(new_establishment) #Adiciona o objeto criado, mas ele ainda em standby
    session.commit() #Atualiza no banco de dados e insere os dados no banco de dados 

    return redirect(url_for('login'))  #Redireciona para a página de login 

# Página de Login
@app.route("/login", methods=['GET'])
def login():
    return render_template("login.html")

if __name__ == "__main__":
    app.run(debug=True)
from sqlalchemy import Column, Integer, String
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base() #Cria uma base modelo (Fazer classes padrões)
# Configuração do SQLAlchemy
senha = "Divesoosloucossabem!123"

engine = create_engine(f'mysql+pymysql://root:{senha}@localhost:3306/establishment', echo=True) #Instância criada para fazer as configurações do SQLAlchemy
Base.metadata.create_all(engine)  # Cria todas a tabelas definidas em database.py
Session = sessionmaker(bind=engine) #Cria uma sessão de objetos

class Establishment(Base):
    __tablename__ = 'establishment_data' #Cria a tabela 
    
    id = Column(Integer, primary_key=True)  #Cria os campos com os tipos e definições 
    nome_estabelecimento = Column(String)
    email_estabelecimento = Column(String)
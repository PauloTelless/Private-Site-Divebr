from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base() #Cria uma base modelo (Fazer classes padrões)

class Establishment(Base):
    __tablename__ = 'establishment_data' #Cria a tabela 
    
    id = Column(Integer, primary_key=True)  #Cria os campos com os tipos e definições 
    nome_estabelecimento = Column(String)
    email_estabelecimento = Column(String)
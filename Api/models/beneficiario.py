import db_connect
import pandas as pd

conn = db_connect.db_connect

def listAll():
    lista = pd.read_sql_query('SELECT * FROM beneficiarios ', conn)
    return lista

def updateId(id):
    teste = 0
    return teste


class beneficiario:
    def __init__(self, cpf, nome, dataNascimento, endereco, telefone, celular, rg, dataObito, email, cDocumentos) -> None:
        self.cpf= cpf

    def setNome(self, nome):
        self.nome = nome
    def setTeste(self, teste):
        self.teste = teste
    

print(listAll())


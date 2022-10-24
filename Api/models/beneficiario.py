from datetime import datetime
from typing import Any
import db_connect
import pandas as pd
import datetime

conn = db_connect.db_connect
tabBeneficiarios = 'beneficiarios'
tabDeficiente = 'deficiente'
tabIdoso = 'idoso'
tabProtocolo = 'protocolo'


class beneficiario:
    def __init__(self, cpf, nome, dataNascimento, endereco, celular, rg, email, cDocumentos, telefone="NULL", dataObito="NULL", repLegal="NULL") -> None:
        self.cpf = cpf
        self.nome = nome
        self.dataNascimento = dataNascimento
        self.endereco = endereco
        self.telefone = telefone
        self.celular = celular
        self.rg = rg
        self.dataObito = dataObito
        self.email = email
        self.cDocumentos = cDocumentos
        self.repLegal = repLegal

    def listAll():
        lista = pd.read_sql_query(
            'SELECT * FROM {0} '.format(tabBeneficiarios), conn)
        return lista

    def add(self):
        if self.telefone != "NULL" :
            self.telefone = '\''+self.telefone+"\'"

        if self.repLegal != "NULL" :
            self.repLegal = '\''+self.repLegal+"\'"
        
        teste=conn.execute(
                'INSERT INTO {0} (cpf, nome, data_nascimento, endereco, telefone, celular, rg, data_obito, email, c_documentos, representante_legal) VALUES (\'{1}\',\'{2}\',\'{3}\',\'{4}\',{5},\'{6}\',\'{7}\',{8},\'{9}\',\'{10}\',{11})'.format(
                    tabBeneficiarios, self.cpf, self.nome, self.dataNascimento, self.endereco, self.telefone, self.celular, self.rg, self.dataObito, self.email, self.cDocumentos, self.repLegal))
        return teste

    #def updateById(self):

date = datetime.date(2009, 5, 5)
ben=beneficiario(15445445,'gustavito', date,'teste',9533,16533,'teste.testeds25a','caminho',repLegal='osnidlo')
print(ben.add())


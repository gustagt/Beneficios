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

        if self.repLegal != "NULL":
            self.repLegal = '\''+self.repLegal+"\'"

        conn.execute(
            'INSERT INTO {0} (cpf, nome, data_nascimento, endereco, telefone, celular, rg, data_obito, email, c_documentos, representante_legal) VALUES (\'{1}\',\'{2}\',\'{3}\',\'{4}\',{5},{6},\'{7}\',{8},\'{9}\',\'{10}\',{11})'.format(
                tabBeneficiarios, self.cpf, self.nome, self.dataNascimento, self.endereco, self.telefone, self.celular, self.rg, self.dataObito, self.email, self.cDocumentos, self.repLegal))

        selecao = pd.read_sql_query(
            "SELECT * FROM {0} where cpf={1}".format(tabBeneficiarios, self.cpf), conn)
        return selecao

    def selectByCpf(cpf):
        selecao = pd.read_sql_query(
            "SELECT * FROM {0} where cpf={1}".format(tabBeneficiarios, cpf), conn)
        return selecao

    def updateByCpf(self):

        if self.repLegal != "NULL":
            self.repLegal = '\''+self.repLegal+"\'"

        if self.dataObito != "NULL":
            self.dataObito = '\''+self.dataObito+"\'"

        conn.execute(
            'UPDATE {0} SET nome=\'{1}\', data_nascimento=\'{2}\', endereco=\'{3}\', telefone={4}, celular={5}, rg=\'{6}\', data_obito={7}, email=\'{8}\', c_documentos=\'{9}\', representante_legal={10} WHERE cpf={11}'.format(
                tabBeneficiarios, self.nome, self.dataNascimento, self.endereco, self.telefone, self.celular, self.rg, self.dataObito, self.email, self.cDocumentos, self.repLegal, self.cpf))
        selecao = pd.read_sql_query(
            "SELECT * FROM {0} where cpf={1}".format(tabBeneficiarios, self.cpf), conn)
        return selecao

    def deleteByCpf(cpf):
        conn.execute("DELETE FROM {0} WHERE cpf={1}".format(
            tabBeneficiarios, cpf))
        selecao = pd.read_sql_query(
            "SELECT * FROM {0} where cpf={1}".format(tabBeneficiarios, cpf), conn)
        return selecao


date = datetime.date(2009, 5, 5)
ben = beneficiario(15445468455, 'gustavit', date, 'teste', 9533, 16533,
                   'teste.testeds24454a', 'caminho', repLegal='osnildo', telefone=45531)
print(beneficiario.deleteByCpf(15444))

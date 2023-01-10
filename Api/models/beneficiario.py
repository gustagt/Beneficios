# from models import db_connect
from models import db_connect
import pandas as pd

conn = db_connect.db_connect

tabBeneficiarios = 'beneficiarios'


class Beneficiario:

    def __init__(self, cpf, nome, dataNascimento,  rua, bairro, numComplemento, cidade, cep, celular, rg, email,  genero, cDocumentos, telefone="NULL", dataObito="NULL", repLegal="NULL") -> None:
        self.cpf = cpf
        self.nome = nome
        self.dataNascimento = dataNascimento
        self.rua = rua
        self.bairro = bairro
        self.numComplemento = numComplemento
        self.cidade = cidade
        self.cep = cep
        self.telefone = telefone
        self.celular = celular
        self.rg = rg
        self.dataObito = dataObito
        self.email = email
        self.cDocumentos = cDocumentos
        self.repLegal = repLegal
        self.genero = genero

    def listAll():
        conn = db_connect.db_connect
        lista = pd.read_sql_query(
            'SELECT * FROM {0} '.format(tabBeneficiarios), conn)
        return lista

    def add(self):

        if self.repLegal != "NULL":
            self.repLegal = '\''+self.repLegal+"\'"

        if self.dataObito != "NULL":
            self.dataObito = '\''+self.dataObito+"\'"

        conn.execute(
            'INSERT INTO {0} (cpf, nome, data_nascimento, genero, rua, telefone, celular, rg, data_obito, email, c_documentos, representante_legal, bairro, cidade, num_complemento, cep) VALUES ({1},\'{2}\',\'{3}\',\'{4}\',\'{5}\',{6},{7},\'{8}\',{9},\'{10}\',\'{11}\',{12},\'{13}\',\'{14}\',\'{15}\',\'{16}\')'.format(
                tabBeneficiarios, self.cpf, self.nome, self.dataNascimento, self.genero, self.rua, self.telefone, self.celular, self.rg, self.dataObito, self.email, self.cDocumentos, self.repLegal, self.bairro, self.cidade, self.numComplemento, self.cep))

        selecao = pd.read_sql_query(
            "SELECT * FROM {0} where cpf={1}".format(tabBeneficiarios, self.cpf), conn)
        beneficiario = Beneficiario.convertSelect(selecao)
        return beneficiario

    def selectByCpf(cpf):
        selecao = pd.read_sql_query(
            "SELECT * FROM {0} where cpf={1}".format(tabBeneficiarios, cpf), conn)
        beneficiario = Beneficiario.convertSelect(selecao)
        return beneficiario

    def updateByCpf(self):

        if self.repLegal != "NULL":
            self.repLegal = '\''+self.repLegal+"\'"

        if self.dataObito != "NULL":
            self.dataObito = '\''+self.dataObito+"\'"

        conn.execute(
            'UPDATE {0} SET nome=\'{1}\', data_nascimento=\'{2}\', rua=\'{3}\', genero=\'{4}\', telefone={5}, celular={6}, rg=\'{7}\', data_obito={8}, email=\'{9}\', c_documentos=\'{10}\', representante_legal={11}, bairro=\'{12}\', cidade=\'{13}\', num_complemento=\'{14}\', cep=\'{15}\' WHERE cpf={16}'.format(
                tabBeneficiarios, self.nome, self.dataNascimento, self.rua, self.genero, self.telefone, self.celular, self.rg, self.dataObito, self.email, self.cDocumentos, self.repLegal, self.bairro, self.cidade, self.numComplemento, self.numComplemento, self.cpf))
        selecao = pd.read_sql_query(
            "SELECT * FROM {0} where cpf={1}".format(tabBeneficiarios, self.cpf), conn)
        beneficiario = Beneficiario.convertSelect(selecao)
        return beneficiario

    def deleteByCpf(cpf):
        conn.execute("DELETE FROM {0} WHERE cpf={1}".format(
            tabBeneficiarios, cpf))
        selecao = pd.read_sql_query(
            "SELECT * FROM {0} where cpf={1}".format(tabBeneficiarios, cpf), conn)
        return selecao

    def emailDisponivel(email):
        selecao = pd.read_sql_query(
            "SELECT email FROM {0} where email=\'{1}\'".format(tabBeneficiarios, email), conn)
        if selecao.empty:
            return True

        return False
    
    def ValidarBeneficiario(cpf):
        selecao = pd.read_sql_query(
            "SELECT * FROM {0} where cpf={1}".format(tabBeneficiarios, cpf), conn)
        return selecao
    
    def credencialId(cpf):
        selecao = pd.read_sql_query(
            "SELECT MAX(n_protocolo) FROM tabela where beneficiarios_cpf = {1} and ".format(tabBeneficiarios, cpf), conn)
        
        return selecao
    def credencialDf(cpf):
        selecao = pd.read_sql_query(
            "SELECT * FROM {0} where  id = (SELECT MAX(id) FROM tabela)".format(tabBeneficiarios, cpf), conn)
        return selecao

    def convertSelect(selecao):
        beneficiario = Beneficiario(selecao['cpf'][0], selecao['nome'][0], selecao['data_nascimento'][0], selecao['rua'][0], selecao['bairro'][0], selecao['num_complemento'][0], selecao['cidade'][0], selecao['cep'][0],
                                    selecao['celular'][0], selecao['rg'][0], selecao['email'][0], selecao['genero'][0], selecao['c_documentos'][0], selecao['telefone'][0], selecao['data_obito'][0], selecao['representante_legal'][0])
        return beneficiario
    

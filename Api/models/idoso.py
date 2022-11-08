import db_connect
import pandas as pd

conn = db_connect.db_connect

tabIdoso = 'idoso'

class Idoso:
    def __init__(self, ocupacao, beneficiarioCpf, nCredencial="NULL", dataEmissao="NULL", dataValidade="NULL", segundaVia="NULL", terceiraVia="NULL", primeiroRecadastro="NULL",segundoRecadastro="NULL",terceiroRecadastro="NULL", observacoes="NULL",) -> None:
        self.nCredencial = nCredencial
        self.ocupacao = ocupacao
        self.beneficiarioCpf = beneficiarioCpf
        self.dataEmissao = dataEmissao
        self.dataValidade = dataValidade
        self.segundaVia = segundaVia
        self.terceiraVia = terceiraVia
        self.primeiroRecadastro = primeiroRecadastro
        self.segundoRecadastro = segundoRecadastro
        self.terceiroRecadastro = terceiroRecadastro
        self.observacoes = observacoes

    def listAll():
        lista = pd.read_sql_query(
            'SELECT * FROM {0} '.format(tabIdoso), conn)
        return lista

    def add(self):

        if self.observacoes != "NULL":
            self.observacoes = '\''+self.observacoes+"\'"

        conn.execute(
            'INSERT INTO {0} (n_credencial, ocupacao, data_emissao, data_validade, segunda_via, terceira_via, primeiro_recadastro, segundo_recadastro, terceiro_recadastro, observacoes, beneficiarios_cpf) VALUES ({1},\'{2}\',\'{3}\',\'{4}\',{5},{6},{7},{8},{9},{10},{11},{12},{13})'.format(
                tabIdoso, self.nCredencial, self.ocupacao, self.dataEmissao, self.dataValidade, self.segundaVia, self.terceiraVia, self.primeiroRecadastro, self.segundoRecadastro, self.terceiroRecadastro, self.observacoes, self.beneficiarioCpf))

        selecao = pd.read_sql_query(
            "SELECT * FROM {0} WHERE beneficiarios_cpf={1}".format(tabIdoso, self.beneficiarioCpf), conn)
        return selecao
    
    def selectByCpf(cpf):
        selecao = pd.read_sql_query(
            "SELECT * FROM {0} WHERE  beneficiarios_cpf={1}".format(tabIdoso, cpf), conn)
        return selecao
    
    def selectByNCredencial(nCredencial):
        selecao = pd.read_sql_query(
            "SELECT * FROM {0} WHERE  n_credencial={1}".format(tabIdoso, nCredencial), conn)
        return selecao

    def updateByCpf(self):

        if self.observacoes != "NULL":
            self.observacoes = '\''+self.observacoes+"\'"
            
        conn.execute(
            'UPDATE {0} SET ocupacao=\'{1}\', data_emissao={2}, data_validade={3}, segunda_via={4}, terceira_via={5}, primeiro_recadastro={6}, segundo_recadastro={7}, terceiro_recadastro={8}, observacoes={9} WHERE beneficiarios_cpf={10}'.format(
                tabIdoso, self.ocupacao, self.dataEmissao, self.dataValidade, self.segundaVia, self.terceiraVia, self.primeiroRecadastro, self.segundoRecadastro, self.terceiroRecadastro, self.observacoes, self.beneficiarioCpf))
        selecao = pd.read_sql_query(
            "SELECT * FROM {0} where beneficiarios_cpf={1}".format(tabIdoso, self.beneficiarioCpf), conn)
        return selecao

    def deleteByCpf(cpf):
        conn.execute("DELETE FROM {0} WHERE beneficiarios_cpf={1}".format(
            tabIdoso, cpf))
        selecao = pd.read_sql_query(
            "SELECT * FROM {0} where beneficiarios_cpf={1}".format(tabIdoso, cpf), conn)
        return selecao
    


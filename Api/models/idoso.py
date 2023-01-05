from models import db_connect
import pandas as pd

conn = db_connect.db_connect

tabIdoso = 'idoso'
tabProtocolo = 'protocolo'

class Idoso:
    def __init__(self, beneficiarioCpf, nCredencial="NULL", dataEmissao="NULL", dataValidade="NULL", segundaVia="NULL", terceiraVia="NULL", primeiroRecadastro="NULL", segundoRecadastro="NULL", terceiroRecadastro="NULL", observacoes="NULL",) -> None:
        self.nCredencial = nCredencial
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

    def listAllConcluidos():
        lista = pd.read_sql_query(
            'SELECT * FROM {0} as ID RIGHT JOIN {1} as PT on  ID.beneficiarios_cpf = PT.beneficiarios_cpf WHERE PT.status=\'Finalizado\' AND PT.tipo=\'Idoso\''.format(tabIdoso, tabProtocolo), conn)
        return lista

    def add(self):

        if self.observacoes != "NULL":
            self.observacoes = '\''+self.observacoes+"\'"

        if self.dataEmissao != "NULL":
            self.dataEmissao = '\''+self.dataEmissao+"\'"

        if self.dataValidade != "NULL":
            self.dataValidade = '\''+self.dataValidade+"\'"

        if self.segundaVia != "NULL":
            self.segundaVia = '\''+self.segundaVia+"\'"

        if self.terceiraVia != "NULL":
            self.terceiraVia = '\''+self.terceiraVia+"\'"

        if self.primeiroRecadastro != "NULL":
            self.primeiroRecadastro = '\''+self.primeiroRecadastro+"\'"

        if self.segundoRecadastro != "NULL":
            self.segundoRecadastro = '\''+self.segundoRecadastro+"\'"

        if self.terceiroRecadastro != "NULL":
            self.terceiroRecadastro = '\''+self.terceiroRecadastro+"\'"

        conn.execute(
            'INSERT INTO {0} (n_credencial, data_emissao, data_validade, segunda_via, terceira_via, primeiro_recadastro, segundo_recadastro, terceiro_recadastro, observacoes, beneficiarios_cpf) VALUES ({1},{2},{3},{4},{5},{6},{7},{8},{9},{10})'.format(
                tabIdoso, self.nCredencial, self.dataEmissao, self.dataValidade, self.segundaVia, self.terceiraVia, self.primeiroRecadastro, self.segundoRecadastro, self.terceiroRecadastro, self.observacoes, self.beneficiarioCpf))

        selecao = pd.read_sql_query(
            "SELECT * FROM {0} WHERE beneficiarios_cpf={1}".format(tabIdoso, self.beneficiarioCpf), conn)
        return selecao

    def selectByCpf(cpf):
        selecao = pd.read_sql_query(
            "SELECT * FROM {0} WHERE  beneficiarios_cpf={1}".format(tabIdoso, cpf), conn)
        idoso = Idoso.convertSelect(selecao)
        return idoso

    def selectByNCredencial(nCredencial):
        selecao = pd.read_sql_query(
            "SELECT * FROM {0} WHERE  n_credencial={1}".format(tabIdoso, nCredencial), conn)
        idoso = Idoso.convertSelect(selecao)
        return idoso

    def updateByCpf(self):
        if self.observacoes != "NULL":
            self.observacoes = '\''+self.observacoes+"\'"

        conn.execute(
            'UPDATE {0} SET , data_emissao={1}, data_validade={2}, segunda_via={3}, terceira_via={4}, primeiro_recadastro={5}, segundo_recadastro={6}, terceiro_recadastro={7}, observacoes={8} WHERE beneficiarios_cpf={9}'.format(
                tabIdoso, self.dataEmissao, self.dataValidade, self.segundaVia, self.terceiraVia, self.primeiroRecadastro, self.segundoRecadastro, self.terceiroRecadastro, self.observacoes, self.beneficiarioCpf))
        selecao = pd.read_sql_query(
            "SELECT * FROM {0} where beneficiarios_cpf={1}".format(tabIdoso, self.beneficiarioCpf), conn)
        return selecao
    
    def setData(cpf, dataValidade, dataEmissao):
        conn.execute(
            'UPDATE {0} SET  data_validade=\'{1}\', data_emissao=\'{2}\' WHERE beneficiarios_cpf={3}'.format(
                tabIdoso, dataValidade, dataEmissao, cpf))
        selecao = pd.read_sql_query(
            "SELECT * FROM {0} where beneficiarios_cpf={1}".format(tabIdoso, cpf), conn)
        idoso = Idoso.convertSelect(selecao)
        return idoso

    def deleteByCpf(cpf):
        conn.execute("DELETE FROM {0} WHERE beneficiarios_cpf={1}".format(
            tabIdoso, cpf))
        selecao = pd.read_sql_query(
            "SELECT * FROM {0} where beneficiarios_cpf={1}".format(tabIdoso, cpf), conn)
        return selecao

    def convertSelect(selecao):
        idoso = Idoso(selecao['beneficiarios_cpf'][0], selecao['n_credencial'][0], selecao['data_emissao'][0], selecao['data_validade'][0], selecao['segunda_via'][0], selecao['terceira_via'][0], selecao['primeiro_recadastro'][0], selecao['segundo_recadastro'][0],
                                    selecao['terceiro_recadastro'][0], selecao['observacoes'][0])
        return idoso
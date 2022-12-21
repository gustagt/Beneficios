from models.db_connect import db_connect
import pandas as pd


conn = db_connect

tabProtocolo = 'protocolo'


class Protocolo:
    def __init__(self, beneficiarioCpf, status, servico, dataAnalise, tipo, nProtocolo="NULL", dataDocpen="NULL", dataProducao="NULL", dataEnviado="NULL", dataEntregue="NULL") -> None:
        self.nProtocolo = nProtocolo
        self.status = status
        self.beneficiarioCpf = beneficiarioCpf
        self.servico = servico
        self.dataAnalise = dataAnalise
        self.tipo = tipo
        self.dataDocpen = dataDocpen
        self.dataProducao = dataProducao
        self.dataEnviado = dataEnviado
        self.dataEntregue = dataEntregue

    def listAll():
        lista = pd.read_sql_query(
            'SELECT * FROM {0} '.format(tabProtocolo), conn)
        return lista

    def add(self):

        if self.dataDocpen != "NULL":
            self.dataDocpen = '\''+self.dataDocpen+"\'"

        if self.dataProducao != "NULL":
            self.dataProducao = '\''+self.dataProducao+"\'"

        if self.dataEnviado != "NULL":
            self.dataEnviado = '\''+self.dataEnviado+"\'"

        if self.dataEntregue != "NULL":
            self.dataEntregue = '\''+self.dataEntregue+"\'"

        conn.execute(
            'INSERT INTO {0} (n_protocolo, servico, status, tipo, data_analise, data_docpen, data_producao, data_enviado, data_entregue, beneficiarios_cpf) VALUES ({1},\'{2}\',\'{3}\',\'{4}\',\'{5}\',{6},{7},{8},{9},{10})'.format(
                tabProtocolo, self.nProtocolo, self.servico, self.status, self.tipo, self.dataAnalise, self.dataDocpen, self.dataProducao, self.dataEnviado, self.dataEntregue, self.beneficiarioCpf))

        selecao = pd.read_sql_query(
            "SELECT * FROM {0} WHERE beneficiarios_cpf={1}".format(tabProtocolo, self.beneficiarioCpf), conn)
        protocolo = Protocolo.convertSelect(selecao)
        return protocolo

    def selectByCpf(cpf):
        selecao = pd.read_sql_query(
            "SELECT * FROM {0} WHERE  beneficiarios_cpf={1}".format(tabProtocolo, cpf), conn)
        protocolo = Protocolo.convertSelect(selecao)
        return protocolo

    def selectByNProtocolo(nProtocolo):
        selecao = pd.read_sql_query(
            "SELECT * FROM {0} WHERE  n_protocolo={1}".format(tabProtocolo, nProtocolo), conn)
        protocolo = Protocolo.convertSelect(selecao)
        return protocolo

    # aqui
    def updateByNProcolo(self):
        conn.execute(
            'UPDATE {0} SET servico=\'{1}\', status=\'{2}\' WHERE n_protocolo={3}'.format(
                tabProtocolo, self.servico, self.status, self.nProtocolo))
        selecao = pd.read_sql_query(
            "SELECT * FROM {0} where n_protocolo={1}".format(tabProtocolo, self.nProtocolo), conn)
        protocolo = Protocolo.convertSelect(selecao)
        return protocolo

    def deleteByNProcolo(nProtocolo):
        conn.execute("DELETE FROM {0} WHERE n_protocolo={1}".format(
            tabProtocolo, nProtocolo))
        selecao = pd.read_sql_query(
            "SELECT * FROM {0} where n_protocolo={1}".format(tabProtocolo, nProtocolo), conn)
        return selecao

    def validarProtocolo(cpf):
        selecao = pd.read_sql_query(
            "SELECT * FROM {0} WHERE  beneficiarios_cpf={1}".format(tabProtocolo, cpf), conn)
        return selecao

    def convertSelect(selecao):
        protocolo = Protocolo(selecao['beneficiarios_cpf'].iloc[-1], selecao['status'].iloc[-1],
                              selecao['servico'].iloc[-1], selecao['data_analise'].iloc[-1], selecao['tipo'].iloc[-1], selecao['n_protocolo'].iloc[-1],
                              selecao['data_docpen'].iloc[-1], selecao['data_producao'].iloc[-1], selecao['data_enviado'].iloc[-1], selecao['data_entregue'].iloc[-1])
        return protocolo




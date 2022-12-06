
from models import db_connect
import pandas as pd
from enum import Enum

conn = db_connect.db_connect

tabProtocolo = 'protocolo'


class Protocolo:
    def __init__(self, beneficiarioCpf, status, servico, nProtocolo="NULL") -> None:
        self.nProtocolo = nProtocolo
        self.status = status
        self.beneficiarioCpf = beneficiarioCpf
        self.servico = servico

    def listAll():
        lista = pd.read_sql_query(
            'SELECT * FROM {0} '.format(tabProtocolo), conn)
        return lista

    def add(self):
        conn.execute(
            'INSERT INTO {0} (n_protocolo, servico, status, beneficiarios_cpf) VALUES ({1},\'{2}\',\'{3}\',{4})'.format(
                tabProtocolo, self.nProtocolo, self.servico, self.status, self.beneficiarioCpf))

        selecao = pd.read_sql_query(
            "SELECT * FROM {0} WHERE beneficiarios_cpf={1}".format(tabProtocolo, self.beneficiarioCpf), conn)
        return selecao

    def selectByCpf(cpf):
        selecao = pd.read_sql_query(
            "SELECT * FROM {0} WHERE  beneficiarios_cpf={1}".format(tabProtocolo, cpf), conn)
        return selecao

    def selectByNProtocolo(nProtocolo):
        selecao = pd.read_sql_query(
            "SELECT * FROM {0} WHERE  n_protocolo={1}".format(tabProtocolo, nProtocolo), conn)
        return selecao

    def updateByNProcolo(self):
        conn.execute(
            'UPDATE {0} SET servico=\'{1}\', status=\'{2}\' WHERE n_protocolo={3}'.format(
                tabProtocolo, self.servico, self.status, self.nProtocolo))
        selecao = pd.read_sql_query(
            "SELECT * FROM {0} where n_protocolo={1}".format(tabProtocolo, self.nProtocolo), conn)
        return selecao

    def deleteByNProcolo(nProtocolo):
        conn.execute("DELETE FROM {0} WHERE n_protocolo={1}".format(
            tabProtocolo, nProtocolo))
        selecao = pd.read_sql_query(
            "SELECT * FROM {0} where n_protocolo={1}".format(tabProtocolo, nProtocolo), conn)
        return selecao
    

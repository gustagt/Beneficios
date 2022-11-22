from models import db_connect
import pandas as pd

conn = db_connect.db_connect

tabDeficiente = 'deficiente'

class Deficiente:
    def __init__(self,  deficiencia, beneficiarioCpf, tipoDeficiencia="NULL", nCredencial="NULL", dataEmissao="NULL", dataValidade="NULL", segundaVia="NULL", terceiraVia="NULL", primeiroRecadastro="NULL",segundoRecadastro="NULL",terceiroRecadastro="NULL", observacoes="NULL",) -> None:
        self.nCredencial = nCredencial
        self.deficiencia = deficiencia
        self.tipoDeficiencia = tipoDeficiencia
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
            'SELECT * FROM {0} '.format(tabDeficiente), conn)
        return lista

    def add(self):

        if self.observacoes != "NULL":
            self.observacoes = '\''+self.observacoes+"\'"
            
        if self.tipoDeficiencia != "NULL":
            self.tipoDeficiencia = '\''+self.tipoDeficiencia+"\'"

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
            'INSERT INTO {0} (n_credencial, deficiencia, tipo_deficiencia, data_emissao, data_validade, segunda_via, terceira_via, primeiro_recadastro, segundo_recadastro, terceiro_recadastro, observacoes, beneficiarios_cpf) VALUES ({1},\'{2}\',{3},{4},{5},{6},{7},{8},{9},{10},{11},{12})'.format(
                tabDeficiente, self.nCredencial, self.deficiencia, self.tipoDeficiencia, self.dataEmissao, self.dataValidade, self.segundaVia, self.terceiraVia, self.primeiroRecadastro, self.segundoRecadastro, self.terceiroRecadastro, self.observacoes, self.beneficiarioCpf))

        selecao = pd.read_sql_query(
            "SELECT * FROM {0} WHERE beneficiarios_cpf={1}".format(tabDeficiente, self.beneficiarioCpf), conn)
        return selecao
    
    def selectByCpf(cpf):
        selecao = pd.read_sql_query(
            "SELECT * FROM {0} WHERE  beneficiarios_cpf={1}".format(tabDeficiente, cpf), conn)
        return selecao
    
    def selectByNCredencial(nCredencial):
        selecao = pd.read_sql_query(
            "SELECT * FROM {0} WHERE  n_credencial={1}".format(tabDeficiente, nCredencial), conn)
        return selecao

    def updateByCpf(self):

        if self.observacoes != "NULL":
            self.observacoes = '\''+self.observacoes+"\'"
            
        if self.tipoDeficiencia != "NULL":
            self.tipoDeficiencia = '\''+self.tipoDeficiencia+"\'"

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
            'UPDATE {0} SET deficiencia=\'{1}\', tipo_deficiencia={2}, data_emissao={3}, data_validade={4}, segunda_via={5}, terceira_via={6}, primeiro_recadastro={7}, segundo_recadastro={8}, terceiro_recadastro={9}, observacoes={10} WHERE beneficiarios_cpf={11}'.format(
                tabDeficiente, self.deficiencia, self.tipoDeficiencia, self.dataEmissao, self.dataValidade, self.segundaVia, self.terceiraVia, self.primeiroRecadastro, self.segundoRecadastro, self.terceiroRecadastro, self.observacoes, self.beneficiarioCpf))
        selecao = pd.read_sql_query(
            "SELECT * FROM {0} where beneficiarios_cpf={1}".format(tabDeficiente, self.beneficiarioCpf), conn)
        return selecao

    def deleteByCpf(cpf):
        conn.execute("DELETE FROM {0} WHERE beneficiarios_cpf={1}".format(
            tabDeficiente, cpf))
        selecao = pd.read_sql_query(
            "SELECT * FROM {0} where beneficiarios_cpf={1}".format(tabDeficiente, cpf), conn)
        return selecao
    
    
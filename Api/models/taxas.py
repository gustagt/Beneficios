
from models import db_connect
import pandas as pd

conn = db_connect.db_connect

tab= 'taxas'
taxaSegVia = 'segunda_via_documentos'


class Taxas:
    
    def selectTaxa():
        selecao = pd.read_sql_query(
            "SELECT * FROM {0} WHERE  tipo_taxa=\'{1}\'".format(tab, taxaSegVia), conn)
        valor = selecao['valor'].values[0]
        return valor



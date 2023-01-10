from flask import Flask, request, render_template,session , redirect, send_file

# imports dos controladores funcionario
from controllers.funcionario.loginController import LoginController as lo
from controllers.funcionario.dashboardController import DashboardController as dsboard
from controllers.funcionario.opcoesController import OpcoesController as op


# imports dos controladores
from controllers.cliente.solicitarBoletoController import SolicitarBoletoController as slBoleto
from controllers.cliente.segundaViaController import SegundaViaController as sgVia
from controllers.cliente.consultaController import ConsultaController as cs
from controllers.cliente.formularioDeficienteController import FormularioDeficienteController as fd
from controllers.cliente.formularioIdosoController import FormularioIdosoController as fi
from helpers import helpers as hp

#



from flask_cors import CORS
from pathlib import Path
import secrets
from functools import wraps
import jwt
import os


app = Flask(__name__)
CORS(app)

app.secret_key = secrets.token_hex(32)
CAMINHO = Path().absolute()

# token
def verificarToken(func):
    @wraps(func)
    def decorate(*args, **kwargs):
        try:
            token = session['token']
        except:
            return redirect("/login", code=302)

        try:
            jwt.decode(token, app.secret_key, algorithms=["HS256"])
             
        except jwt.exceptions.ExpiredSignatureError:
            return redirect("/login", code=302)
        return func(*args, **kwargs)

    return decorate

# visualizar documentos
@app.route('/documentos/<string:tipoDocumento>', methods=['GET'])

def documentos(tipoDocumento):

    cpf = session["cpf"]
    caminhoD = CAMINHO / 'documentos' / str(cpf)
    
    for nomeArquivo in os.listdir(caminhoD):
        extensao = os.path.splitext(str(nomeArquivo))[1]
        enderecoArquivo = os.path.join(caminhoD, nomeArquivo)
        
        if(os.path.isfile(enderecoArquivo)):
            if tipoDocumento == 'oficial_foto':
                if nomeArquivo == 'oficial_foto' + extensao:
                    return send_file(enderecoArquivo)
            if tipoDocumento == 'comprovante_residencia':
                if nomeArquivo == 'comprovante_residencia'+ extensao:
                    return send_file(enderecoArquivo)
            if tipoDocumento == 'representante_legal':
                if nomeArquivo == 'representante_legal'+ extensao:
                    return send_file(enderecoArquivo)
            if tipoDocumento == 'laudo_perificial':
                if nomeArquivo == 'laudo_perificial'+ extensao:
                    return send_file(enderecoArquivo)
            if tipoDocumento == 'AR':
                if nomeArquivo == 'AR'+ extensao:
                    return send_file(enderecoArquivo)
    return render_template('cliente/erro.html')

# Navegação

@app.route('/', methods=['GET'])
def index():

    return render_template('cliente/index.html')




# funcionario
# opcoes
@app.route("/opcoes", methods=["POST", "GET"])
def opcoes():
    if request.method == 'GET':
        return op.opcoesGET()
    
    if request.method == "POST":
        return dsboard.dashboardLoginPOST(app.secret_key)
    
@app.route("/opcoes/protocolo", methods=["POST", "GET"])
def opcoesProtocolo():
    if request.method == 'POST':
        return op.opcoesCredencialPOST()
    
@app.route("/opcoes/credencial", methods=["POST", "GET"])
def opcoesCredencial():
    if request.method == 'GET':
        return op.opcoesCredencialGET()
    
@app.route("/opcoes/protocolo/credencial", methods=["POST", "GET"])
def opcoesCredencialProtocolo():
    if request.method == 'GET':
        return op.opcoesProtocoloGET()
    
@app.route("/opcoes/salvarAR", methods=["POST", "GET"])
def opcoesSalvarAR():
    if request.method == 'POST':
        return op.opcoesSalvarARPOST()
    
@app.route("/opcoes/anexarAR", methods=["POST", "GET"])
def opcoesAnexarAR():
    if request.method == 'POST':
        return op.opcoesAnexarARPOST()
    
@app.route("/opcoes/pendente", methods=["POST", "GET"])
def opcoesPendente():
    if request.method == 'POST':
        return op.opcoesPendentePOST()
    
@app.route("/opcoes/indeferir", methods=["POST", "GET"])
def opcoesIndeferir():
    if request.method == 'POST':
        return op.opcoesIndeferirPOST()


# credenciais
@app.route("/login", methods=["POST", "GET"])
def login():
    if request.method == 'GET':
        return lo.loginGET()
    
    if request.method == "POST":
        return dsboard.dashboardLoginPOST(app.secret_key)

@app.route("/credenciais/idosos", methods=["POST", "GET"])
@verificarToken
def credenciaisIdoso():
    if request.method == 'GET':
        return dsboard.credenciaisIdosoGET()

@app.route("/credenciais/deficientes", methods=["POST", "GET"])
@verificarToken
def credenciaisDeficiente():
    if request.method == 'GET':
        return dsboard.credenciaisDeficienteGET()
    
@app.route("/credencial", methods=["POST", "GET"])
def credencial():
    if request.method == 'GET':
        return op.credencialGET()
    


# protocolos
@app.route("/protocolos/finalizados", methods=["POST", "GET"])
@verificarToken
def protocolosFinalizados():
    if request.method == 'GET':
        return dsboard.protocoloFinalizadoGET()


@app.route("/protocolos/idosos", methods=["POST", "GET"])
@verificarToken
def protocolosIdoso():
    if request.method == 'GET':
        return dsboard.protocoloIdosoGET()


@app.route("/protocolos/deficientes", methods=["POST", "GET"])
@verificarToken
def protocolosDeficiente():
    if request.method == 'GET':
        return dsboard.protocoloDeficienteGET()


@app.route("/protocolos/boletos", methods=["POST", "GET"])
@verificarToken
def protocolosBoleto():
    if request.method == 'GET':
        return dsboard.protocoloBoletoGET()


@app.route("/protocolos", methods=["POST", "GET"])

def dashboard():
    if request.method == 'GET':
        return dsboard.protocoloGET()



# cliente
@app.route("/solicitar-boleto", methods=["GET", "POST"])
def solicitarBoleto():
    if request.method == "GET":
        return slBoleto.solicitarBoletoGET()


@app.route("/segunda-via", methods=["POST", "GET"])
def segundaVia():
    if request.method == 'GET':
        return sgVia.segundaViaGET()

    if request.method == "POST":
        return sgVia.segundaViaPOST()


@app.route('/consulta', methods=["POST", 'GET'])
def consulta():
    if request.method == 'GET':
        return cs.consultaGET()

    if request.method == "POST":
        return cs.consultaPOST()


@app.route("/formulario-deficiente", methods=['POST', 'GET'])
def FormularioDeficiente():
    if request.method == "GET":
        return fd.formularioDeficienteGET()

    if request.method == "POST":
        return fd.formularioDeficientePOST()


@app.route("/formulario-idoso", methods=['POST', 'GET'])
def FormularioIdoso():
    if request.method == "GET":
        return fi.formularioIdosoGET()

    if request.method == "POST":
        return fi.formularioIdosoPOST()

if __name__ == '__main__':    app.run(host='0.0.0.0', debug=True)

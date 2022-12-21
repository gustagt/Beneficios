from flask import Flask, request, render_template

# imports dos controladores funcionario
from controllers.funcionario.loginController import LoginController as lo

# imports dos controladores
from controllers.cliente.solicitarBoletoController import SolicitarBoletoController as slBoleto
from controllers.cliente.segundaViaController import SegundaViaController as sgVia
from controllers.cliente.consultaController import ConsultaController as cs
from controllers.cliente.formularioDeficienteController import FormularioDeficienteController as fd
from controllers.cliente.formularioIdosoController import FormularioIdosoController as fi

# 
from flask_cors import CORS
from pathlib import Path


path = Path().absolute()

app = Flask(__name__)
CORS(app)
app.secret_key = 'gusta'



# Navegação

@app.route('/', methods=['GET'])
def index():
    return render_template('cliente/index.html')


# funcionario

@app.route("/login", methods=["POST", "GET"])
def login():
    if request.method == 'GET':
        return lo.consultaGET()

    if request.method == "POST":
        return lo.consultaPOST(request)


# cliente
@app.route("/solicitar-boleto", methods=["GET", "POST"])
def solicitarBoleto():
    if request.method == "GET":
        return slBoleto.solicitarBoletoGET(request)
    

@app.route("/segunda-via", methods=["POST", "GET"])
def segundaVia():
    if request.method == 'GET':
        return sgVia.segundaViaGET()

    if request.method == "POST":
        return sgVia.segundaViaPOST(request)


@app.route('/consulta', methods=["POST", 'GET'])
def consulta():
    if request.method == 'GET':
        return cs.consultaGET()

    if request.method == "POST":
        return cs.consultaPOST(request)


@app.route("/formulario-deficiente", methods=['POST', 'GET'])
def FormularioDeficiente():
    if request.method == "GET":
        return fd.formularioDeficienteGET()

    if request.method == "POST":
       return fd.formularioDeficientePOST(request)


@app.route("/formulario-idoso", methods=['POST', 'GET'])
def FormularioIdoso():
    if request.method == "GET":
        return fi.formularioIdosoGET()
    
    if request.method == "POST":
        return fi.formularioIdosoPOST(request)  
        

if __name__ == '__main__':
    app.run(host='10.101.22.141',debug=True)

from flask import Flask, request, render_template, flash
from models import beneficiario as bn
from werkzeug.utils import secure_filename
import os


app = Flask(__name__)
app.secret_key = 'gusta'

caminho = 'C:/Users/0103250/Documents/Beneficios/Api/documentos/'

# Rota /devs -> LISTAR todos os desenvolvedores cadastrados


@app.route('/beneficiarios', methods=['GET'])
def beneficiarios():
    beneficiarios = bn.Beneficiario.listAll().to_json(orient='index')
    return beneficiarios, 200


@app.route('/', methods=['POST'])
def teste():
    # Verifica a formatação do CPF
        cpf = request.form['cpf']
        if cpf == '11111111111' :
            return('DEU')
        else:
            return('NÃO DEU')
  
   

# Rota /devs -> LISTAR todos os desenvolvedores cadastrados


@app.route('/beneficiarios/add', methods=['POST'])
def addBeneficiarios():
    # Check dos dados
    cpf = request.form['cpf']
    nome = request.form['nome']
    dataNascimento = request.form['dataNascimento']
    celular = request.form['celular']
    rg = request.form['rg']
    email = request.form['email']
    genero = request.form['sexo']

    cep = request.form['cep']
    rua = request.form['rua']
    num = request.form['num']
    complemento = request.form['complemento']
    bairro = request.form['bairro']
    cidade = request.form['cidade']
    arquivo = request.files['arquivo']

    endereco = rua + ' ' + num + ' ' + complemento + \
        " " + bairro + " " + cidade + ' ' + cep

    beneficiario = bn.Beneficiario(
        cpf, nome, dataNascimento, endereco, celular, rg, email, genero)
    retorno = beneficiario.add().to_json(orient="index")

    return 'ok'


if __name__ == '__main__':
    app.run(debug=True)

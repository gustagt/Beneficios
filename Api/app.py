from flask import Flask, request, render_template
from models import beneficiario as bn
from models import deficiente as df
from models import idoso as id
from models import protocolo as pt
from werkzeug.utils import secure_filename
# from flask_cors import CORS
from models import erros as e
import os


app = Flask(__name__)
# CORS(app)
app.secret_key = 'gusta'

caminhoDocumentos = 'C:/Users/0103250/Documents/Beneficios/Api/documentos/'

# Navegação


@app.route('/', methods=['GET'])
def index():
    return render_template("index.html")


# @app.route("/solicitar-boleto", methods=["GET", "POST"])
# def solicitarBoleto():
#     if request.method == "GET":

#         return render_template('solicitarBoleto.html', )


@app.route("/segunda-via", methods=["POST", "GET"])
def segundaVia():
    if request.method == 'GET':
        return render_template('segundaVia.html')

    elif request.method == "POST":
        nCredencial = request.form['nCredencial']
        cpf = request.form['cpf']
        tpCredencial = request.form['tpCredencial']

        if tpCredencial.lower() == 'deficiente':
            credencial = df.Deficiente.selectByCpf(cpf)
            if not (credencial.empty):
                nCredencialResp = credencial['n_credencial'].values[0]
                beneficiario = bn.Beneficiario.selectByCpf(cpf)
                nome = beneficiario['nome'].values[0]
                if nCredencialResp == int(nCredencial):
                    return render_template('solicitarBoleto.html', nCredencial=nCredencialResp, cpf=cpf, nome=nome), 200

        elif tpCredencial.lower() == 'idoso':
            credencial = id.Idoso.selectByCpf(cpf)
            if not (credencial.empty):
                nCredencialResp = credencial['n_credencial'].values[0]
                beneficiario = bn.Beneficiario.selectByCpf(cpf)
                nome = beneficiario['nome'].values[0]
                if nCredencialResp == int(nCredencial):
                    return render_template('solicitarBoleto.html', nCredencial=nCredencialResp, cpf=cpf, nome=nome), 200

        return render_template('erro.html', mensagem=e.Erros.consulta.value), 400


@app.route('/consulta', methods=["POST", 'GET'])
def consulta():
    if request.method == 'GET':
        return render_template('consulta.html'), 200

    if request.method == "POST":
        nProtocolo = request.form['protocolo']
        cpf = request.form['cpf']

        protocolo = pt.Protocolo.selectByCpf(cpf)
        if not (protocolo.empty):

            if protocolo['n_protocolo'].values[0] == int(nProtocolo):
                return renderConsula(nProtocolo), 200

        return render_template('erro.html', mensagem=e.Erros.consulta.value), 400


@app.route("/formulario-deficiente", methods=['POST', 'GET'])
def FormularioDeficiente():
    if request.method == "GET":
        return render_template('fCredencialDeficiente.html')

    elif request.method == "POST":
        cpf = request.form['cpf']

        duplicidade = df.Deficiente.selectByCpf(cpf)

        if duplicidade.empty:

            nome = request.form['nome']
            dataNascimento = request.form['dataNascimento']
            celular = request.form['celular']
            rg = request.form['rg']
            email = request.form['email']
            genero = request.form['sexo']
            telefone = request.form['telefone']

            deficiencia = request.form['tpDeficiencia']
            repLegal = request.form['Rep_Legal']

            cep = request.form['cep']
            rua = request.form['rua']
            num = request.form['num']
            num = num + request.form['complemento']
            bairro = request.form['bairro']
            cidade = request.form['cidade']

            cpResidencia = request.files['cpResidencia']
            laudoPericial = request.files['laudoPericial']
            dcOfFoto = request.files['dcOfFoto']

            caminho = caminhoDocumentos + 'deficientes/' + cpf

            os.mkdir(caminho)

            beneficiario = bn.Beneficiario(
                cpf, nome, dataNascimento, rua, bairro, num, cidade, cep, celular, rg, email, genero, caminho)
            credencialD = df.Deficiente(deficiencia, cpf)
            protocolo = pt.Protocolo(
                cpf, 'Aberto', 'Solicitação para Credencial de Deficiente')

            cpResidencia.save(os.path.join(
                caminho, secure_filename(cpResidencia.filename)))
            laudoPericial.save(os.path.join(
                caminho, secure_filename(laudoPericial.filename)))
            dcOfFoto.save(os.path.join(
                caminho, secure_filename(dcOfFoto.filename)))

            if telefone != '':
                beneficiario.telefone = telefone

            if repLegal.lower() == 'sim':
                nResponsavel = request.form['nResponsavel']
                dResponsavel = request.files['dResponsavel']
                dResponsavel.save(os.path.join(
                    caminho, secure_filename(dResponsavel.filename)))
                beneficiario.repLegal = nResponsavel

            if bn.Beneficiario.selectByCpf(cpf).empty:
                if bn.Beneficiario.emailDisponivel(email):
                    beneficiario.add()
                else:
                    return render_template('erro.html', mensagem=e.Erros.email.value), 400
            else:
                beneficiario.updateByCpf()

            credencialD.add()
            protocolo.add()

            nProtocolo = pt.Protocolo.selectByCpf(cpf)['n_protocolo'].values[0]
            return renderConsula(nProtocolo), 200

        else:
            return render_template('erro.html', mensagem=e.Erros.formularioDeficiente.value), 400


@app.route("/formulario-idoso", methods=['POST', 'GET'])
def FormularioIdoso():
    if request.method == "GET":
        return render_template('fCredencialIdoso.html')
    elif request.method == "POST":
        cpf = request.form['cpf']

        duplicidade = id.Idoso.selectByCpf(cpf)
       

        if duplicidade.empty:

            nome = request.form['nome']
            dataNascimento = request.form['dataNascimento']
            celular = request.form['celular']
            rg = request.form['rg']
            email = request.form['email']
            genero = request.form['sexo']
            telefone = request.form['telefone']

            repLegal = request.form['Rep_Legal']

            cep = request.form['cep']
            rua = request.form['rua']
            num = request.form['num']
            num = num + request.form['complemento']
            
            bairro = request.form['bairro']
            cidade = request.form['cidade']

            cpResidencia = request.files['cpResidencia']
            dcOfFoto = request.files['dcOfFoto']

            caminho = caminhoDocumentos + 'idosos/' + cpf

            os.mkdir(caminho)

            beneficiario = bn.Beneficiario(
                cpf, nome, dataNascimento, rua, bairro, num, cidade, cep, celular, rg, email, genero, caminho)
            credencialD = id.Idoso(cpf)
            protocolo = pt.Protocolo(
                cpf, 'Aberto', 'Solicitação para Credencial de Idoso')

            cpResidencia.save(os.path.join(
                caminho, secure_filename(cpResidencia.filename)))
            dcOfFoto.save(os.path.join(
                caminho, secure_filename(dcOfFoto.filename)))

            if telefone != '':
                beneficiario.telefone = telefone

            if repLegal.lower() == 'sim':
                nResponsavel = request.form['nResponsavel']
                dResponsavel = request.files['dResponsavel']
                dResponsavel.save(os.path.join(
                    caminho, secure_filename(dResponsavel.filename)))
                beneficiario.repLegal = nResponsavel

            if bn.Beneficiario.selectByCpf(cpf).empty:
                if bn.Beneficiario.emailDisponivel(email):
                    beneficiario.add()
                else:
                    return render_template('erro.html', mensagem=e.Erros.email.value), 400
            else:
                beneficiario.updateByCpf()

            protocolo.add()
            credencialD.add()

            nProtocolo = pt.Protocolo.selectByCpf(cpf)['n_protocolo'].values[0]
            return renderConsula(nProtocolo), 200

        else:
            return render_template('erro.html', mensagem=e.Erros.formularioIdoso.value), 400


def renderConsula(nProtocolo):

    return render_template("credencialEstacionamento.html", nProtocolo=nProtocolo )


if __name__ == '__main__':
    app.run(debug=True)

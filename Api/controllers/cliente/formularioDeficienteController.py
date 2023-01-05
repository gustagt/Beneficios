from flask import  request, render_template
from models.deficiente import Deficiente as df
from models.beneficiario import Beneficiario as bn
from models.protocolo import Protocolo as pt
from models import erros as e

from controllers.cliente.consultaController import ConsultaController as cs

import os
from werkzeug.utils import secure_filename
from pathlib import Path
import re
from datetime import date

dataAtual = date.today()
caminhoDocumentos = Path().absolute()

class FormularioDeficienteController:
    def formularioDeficienteGET():
        return render_template('cliente/fCredencialDeficiente.html'), 200
    
    def formularioDeficientePOST():
        cpf = re.sub("[^0-9]", "",str(request.form['cpf']))

        duplicidade = df.selectByCpf(cpf)

        if duplicidade.empty:

            nome = request.form['nome']
            dataNascimento = request.form['dataNascimento']
            celular = re.sub("[^0-9]", "",str(request.form['celular']))
            rg = request.form['rg']
            email = request.form['email']
            genero = request.form['sexo']
            telefone = re.sub("[^0-9]", "",str(request.form['telefone']))
            
            deficiencia = request.form['tpDeficiencia']
            repLegal = request.form['Rep_Legal']

            cep = request.form['cep']
            rua = request.form['rua']
            num = request.form['num']
            num = num + ' ' +request.form['complemento']
            bairro = request.form['bairro']
            cidade = request.form['cidade']

            cpResidencia = request.files['cpResidencia']
            laudoPericial = request.files['laudoPericial']
            dcOfFoto = request.files['dcOfFoto']

            caminho = caminhoDocumentos / 'documentos' / cpf

            os.mkdir(caminho)

            beneficiario = bn(
                cpf, nome, dataNascimento, rua, bairro, num, cidade, cep, celular, rg, email, genero, caminho.as_posix())
            credencialD = df(deficiencia, cpf)
            protocolo = pt(
                cpf, 'Em analise', 'Solicitação para Credencial', dataAtual,'Deficiente')

            cpResidencia.save(os.path.join(
                caminho, secure_filename('comprovante_residencia' + os.path.splitext(cpResidencia.filename)[1])))
            laudoPericial.save(os.path.join(
                caminho, secure_filename('laudo_perificial' + os.path.splitext(laudoPericial.filename)[1])))
            dcOfFoto.save(os.path.join(
                caminho, secure_filename('oficial_foto' + os.path.splitext(dcOfFoto.filename)[1])))

            if telefone != '':
                beneficiario.telefone = telefone

            if repLegal.lower() == 'sim':
                nResponsavel = request.form['nResponsavel']
                dResponsavel = request.files['dResponsavel']
                dResponsavel.save(os.path.join(
                    caminho, secure_filename('representante_legal' + os.path.splitext(dResponsavel.filename)[1])))
                beneficiario.repLegal = nResponsavel

            if bn.ValidarBeneficiario(cpf).empty:
                if bn.emailDisponivel(email):
                    beneficiario.add()
                else:
                    return render_template('cliente/erro.html', mensagem=e.Erros.email.value), 400
            else:
                beneficiario.updateByCpf()

            credencialD.add()
            rProtocolo = protocolo.add()
            
            return cs.renderConsula(rProtocolo.nProtocolo), 200

        else:
            return render_template('cliente/erro.html', mensagem=e.Erros.formularioDeficiente.value), 400
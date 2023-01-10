from flask import  request, render_template
from models.idoso import Idoso as id
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

class FormularioIdosoController:
    def formularioIdosoGET():
        return render_template('cliente/fCredencialIdoso.html'), 200
    
    def formularioIdosoPOST():
        
        try:
            cpf = re.sub("[^0-9]", "",str(request.form['cpf']))
            
            nome = request.form['nome']
            dataNascimento = request.form['dataNascimento']
            celular = re.sub("[^0-9]", "",str(request.form['celular']))
            rg = request.form['rg']
            email = request.form['email']
            genero = request.form['sexo']
            telefone = re.sub("[^0-9]", "",str(request.form['telefone']))

            repLegal = request.form['Rep_Legal']

            cep = request.form['cep']
            rua = request.form['rua']
            num = request.form['num']
            num = num + ' ' +request.form['complemento']
            
            bairro = request.form['bairro']
            cidade = request.form['cidade']

            cpResidencia = request.files['cpResidencia']
            dcOfFoto = request.files['dcOfFoto']

            

            caminho = caminhoDocumentos / 'documentos' / cpf

            try:
                validaBene = bn.selectByCpf(cpf)
                try:
                    id.selectByCpf(cpf)
                    return render_template('cliente/erro.html', mensagem=e.Erros.formularioIdoso.value), 400
                except:
                    pass
                
            except:                
                os.mkdir(caminho)

            beneficiario = bn(
                cpf, nome, dataNascimento, rua, bairro, num, cidade, cep, celular, rg, email, genero, caminho.as_posix())
            credencialD = id(cpf)
            protocolo = pt(
                cpf, 'Em Analise', 'Solicitação para Credencial', dataAtual, 'Idoso')

            cpResidencia.save(os.path.join(
                caminho, secure_filename('comprovante_residencia' + os.path.splitext(cpResidencia.filename)[1])))
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
                if validaBene.email == email:
                    beneficiario.updateByCpf()
                else:
                    if bn.emailDisponivel(email):
                        beneficiario.updateByCpf()
                    else:
                        return render_template('cliente/erro.html', mensagem=e.Erros.email.value), 400
                

            rProtocolo = protocolo.add()
            credencialD.add()

            return cs.renderConsula(rProtocolo.nProtocolo), 200

        except:
            return render_template('cliente/erro.html', mensagem=e.Erros.formularioIdoso.value), 400

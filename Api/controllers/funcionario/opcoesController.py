from flask import request, render_template, session, send_file, redirect
from models.protocolo import Protocolo as pt
from models.beneficiario import Beneficiario as bn
from models.idoso import Idoso as id
from models.deficiente import Deficiente as df

from helpers import helpers as hp
from models import erros as e

import openpyxl
from win32com import client
import win32com.client
import os
from pathlib import Path
import time
from datetime import date
from werkzeug.utils import secure_filename

from reportlab.pdfgen.canvas import Canvas
from PIL import Image,  ImageDraw, ImageFont


ptc = 'Protocolo'
crd = 'Credencial'

path = Path().absolute()
data = date.today()


class OpcoesController:

    # login
    def opcoesGET():

        numero = request.cookies.get("numero")

        protocolo = pt.selectByNProtocolo(int(numero))
        beneficiario = bn.selectByCpf(protocolo.beneficiarioCpf)
        session['cpf'] = str(protocolo.beneficiarioCpf)

        if protocolo.tipo == "Idoso":
            credencial = id.selectByCpf(protocolo.beneficiarioCpf)
            return render_template('funcionario/opcoes.html', subtitulo=ptc, numero=numero, credencial=credencial, protocolo=protocolo, beneficiario=beneficiario)

        if protocolo.tipo == "Deficiente":
            credencial = df.selectByCpf(protocolo.beneficiarioCpf)
            return render_template('funcionario/opcoes.html', subtitulo=ptc, numero=numero, credencial=credencial, protocolo=protocolo, beneficiario=beneficiario)

        if protocolo.tipo == "Boleto":
            tipo = str(protocolo.servico).replace(' ', '').split("-")[1]
            if tipo == 'Deficiente':
                credencial = df.selectByCpf(protocolo.beneficiarioCpf)
                return render_template('funcionario/opcoes.html', subtitulo=ptc, numero=numero, credencial=credencial, protocolo=protocolo, beneficiario=beneficiario, tipo=tipo)
            if tipo == 'Idoso':
                credencial = id.selectByCpf(protocolo.beneficiarioCpf)
                return render_template('funcionario/opcoes.html', subtitulo=ptc, numero=numero, credencial=credencial, protocolo=protocolo, beneficiario=beneficiario, tipo=tipo)

    def credencialGET():
        numero = request.cookies.get("numero")
        tipo = session['tipoCredencial']

        

        if tipo == "idoso":
            credencial = id.selectByNCredencial(numero)
            beneficiario = bn.selectByCpf(credencial.beneficiarioCpf)
            session['cpf'] = str(credencial.beneficiarioCpf)
            return render_template('funcionario/credenciais.html', subtitulo=crd, numero=numero, credencial=credencial, beneficiario=beneficiario, tipo=tipo)

        if tipo == "deficiente":
            credencial = df.selectByNCredencial(numero)
            beneficiario = bn.selectByCpf(credencial.beneficiarioCpf)
            session['cpf'] = str(credencial.beneficiarioCpf)
            return render_template('funcionario/credenciais.html', subtitulo=crd, numero=numero, credencial=credencial, beneficiario=beneficiario, tipo=tipo)
    
    def opcoesSalvarARPOST():
        ar = request.form['ar']
        nProtocolo = request.cookies.get("numero") 
        
        status = 'Enviado'
        pt.setAR(ar, nProtocolo)
        pt.setStatus(status, nProtocolo)
        
        return redirect('/opcoes')
    
    def opcoesAnexarARPOST():
        ar = request.files['arFile']
        nProtocolo = request.cookies.get("numero") 
        
        status = 'Finalizado'
        pt.setDataEntrega(data, nProtocolo)
        protocolo = pt.setStatus(status, nProtocolo)
        
        
        caminho = path / 'documentos' / str(protocolo.beneficiarioCpf)
        
        ar.save(os.path.join(
                caminho.__str__(), secure_filename('AR' + os.path.splitext(ar.filename)[1])))

        return redirect('/opcoes')
        
        
    def opcoesProtocoloGET():
        nProtocolo = request.cookies.get("numero")

        protocolo = pt.selectByNProtocolo(nProtocolo)
        
        beneficiario = bn.selectByCpf(protocolo.beneficiarioCpf)
        
        if protocolo.tipo == 'Idoso':
            credencial = id.selectByCpf(beneficiario.cpf)
            file = path / 'documentos' / str(beneficiario.cpf) / \
                '{0}-ido.pdf'.format(credencial.nCredencial)
        elif protocolo.tipo == 'Deficiente':
            credencial = df.selectByCpf(beneficiario.cpf)
            file = path / 'documentos' / str(beneficiario.cpf) / \
                '{0}-def.pdf'.format(credencial.nCredencial)
        elif str(protocolo.servico).replace(' ', '').split('-')[1] == 'Idoso':
            credencial = id.selectByCpf(beneficiario.cpf)
            file = path / 'documentos' / str(beneficiario.cpf) / \
                '{0}-ido.pdf'.format(credencial.nCredencial)
        else:
            credencial = df.selectByCpf(beneficiario.cpf)
            file = path / 'documentos' / str(beneficiario.cpf) / \
                '{0}-def.pdf'.format(credencial.nCredencial)
        return send_file(file)

    def opcoesCredencialGET():
        nCredencial = request.cookies.get("numero")
        tipo = request.cookies.get("tpCredencial")

        if tipo == 'idoso':
            credencial = id.selectByNCredencial(nCredencial)
            file = path / 'documentos' / str(credencial.beneficiarioCpf) / \
                '{0}-ido.pdf'.format(credencial.nCredencial)
        elif tipo == 'deficiente':
            credencial = df.selectByNCredencial(nCredencial)
            file = path / 'documentos' / str(credencial.beneficiarioCpf) / \
                '{0}-def.pdf'.format(credencial.nCredencial)

        return send_file(file)

    def opcoesCredencialPOST():
        valor = request.form['valor']
        nomeUsuario = session['nomeUsuario']
        if valor == 'aprovado':
            dataValidade = request.form['dataValidade']
            nProtocolo = request.cookies.get("numero")
            protocolo = pt.selectByNProtocolo(nProtocolo)
            beneficiario = bn.selectByCpf(protocolo.beneficiarioCpf)
            if protocolo.tipo == 'Idoso':
                credencial = id.setData(beneficiario.cpf, dataValidade, data)
                file = path / 'documentos' / str(beneficiario.cpf) / \
                '{0}-ido.pdf'.format(credencial.nCredencial)
                
            elif protocolo.tipo == 'Deficiente':
                tipoDeficiencia = request.form['tipoDeficiencia']
                credencial = df.setDados(beneficiario.cpf, dataValidade, data, tipoDeficiencia)
                file = path / 'documentos' / str(beneficiario.cpf) / \
                '{0}-def.pdf'.format(credencial.nCredencial)
            elif str(protocolo.servico).replace(' ', '').split('-')[1] == 'Idoso':
                credencial = id.setData(beneficiario.cpf, dataValidade, data)
                file = path / 'documentos' / str(beneficiario.cpf) / \
                '{0}-ido.pdf'.format(credencial.nCredencial)
            else:
                credencial = df.setDados(beneficiario.cpf, dataValidade, data)
                file = path / 'documentos' / str(beneficiario.cpf) / \
                '{0}-def.pdf'.format(credencial.nCredencial)
                
            OpcoesController.gerarCredencial(protocolo, beneficiario, credencial)
            pt.setStatus('Em Produção', protocolo.nProtocolo)
            return send_file(file)

        if valor == 'pendente':
            nProtocolo = request.cookies.get("numero")
            protocolo = pt.selectByNProtocolo(nProtocolo)
            
            return render_template("funcionario/feedback.html", protocolo=protocolo, nProtocolo=nProtocolo, valor=valor, nomeUsuario=nomeUsuario) 

        if valor == 'indeferir':
            nProtocolo = request.cookies.get("numero")
            protocolo = pt.selectByNProtocolo(nProtocolo)
            return render_template("funcionario/feedback.html", protocolo=protocolo, nProtocolo=nProtocolo, valor=valor, nomeUsuario=nomeUsuario) 
        
    def opcoesPendentePOST():
        nProtocolo = request.cookies.get("numero")

        pt.setStatus("Pendente", nProtocolo)
        # email
        # //
        # //
        return redirect('/protocolos')   
     
    def opcoesIndeferirPOST():
        nProtocolo = request.cookies.get("numero")
        protocolo = pt.setStatus("Indeferido", nProtocolo)
        if protocolo.tipo == 'Deficiente':
            df.deleteByCpf(protocolo.beneficiarioCpf)
        elif protocolo.tipo == 'Idoso':
            id.deleteByCpf(protocolo.beneficiarioCpf)
            
        # email
        # //
        # //
        
        return redirect('/protocolos')    
        
    # credencial

    def gerarCredencial(protocolo: pt, beneficiario: bn, credencial):

        if protocolo.tipo == 'Idoso':
            OpcoesController.credencialIdoso(credencial,protocolo, beneficiario)
            
        elif protocolo.tipo == 'Deficiente':
            OpcoesController.credencialDeficiente(credencial,protocolo, beneficiario)
        
        elif str(protocolo.servico).replace(' ', '').split('-')[1] == 'Idoso':
            OpcoesController.credencialIdoso(credencial,protocolo, beneficiario)
            
        else:
            OpcoesController.credencialDeficiente(credencial,protocolo, beneficiario)
            
        OpcoesController.pdfCredencial(protocolo, credencial)
        # delay para fechar e excluir os arquivos
        time.sleep(1)
        if os.path.exists(path / 'documentos' / 'templatesDocumentos' / '{0}.jpg'.format(protocolo.nProtocolo)):
            os.remove(path / 'documentos' / 'templatesDocumentos' /
                      '{0}.jpg'.format(protocolo.nProtocolo))

    def pdfCredencial(protocolo : pt, credencial):
        # Open the image
        im = Image.open(path / 'documentos' /
                         'templatesDocumentos' / "{0}.jpg".format(protocolo.nProtocolo))

        # Create a PDF with the same size as the image
        if protocolo.tipo == 'Idoso':
            pdf = Canvas((path / 'documentos' /
                         str(credencial.beneficiarioCpf) / "{0}-ido.pdf".format(credencial.nCredencial)).__str__(), pagesize=im.size)
            
        elif protocolo.tipo == 'Deficiente':
            pdf = Canvas((path / 'documentos' /
                         str(credencial.beneficiarioCpf) / "{0}-def.pdf".format(credencial.nCredencial)).__str__(), pagesize=im.size)
        
        elif str(protocolo.servico).replace(' ', '').split('-')[1] == 'Idoso':
            pdf = Canvas((path / 'documentos' /
                         str(credencial.beneficiarioCpf) / "{0}-ido.pdf".format(credencial.nCredencial)).__str__(), pagesize=im.size)
            
        else:
            pdf = Canvas((path / 'documentos' /
                         str(credencial.beneficiarioCpf) / "{0}-def.pdf".format(credencial.nCredencial)).__str__(), pagesize=im.size)


        # Draw the image on the PDF
        pdf.drawImage(path / 'documentos' /
                         'templatesDocumentos' / "{0}.jpg".format(protocolo.nProtocolo), 0, 0, im.size[0], im.size[1])

        im.close()
        # Save the PDF
        pdf.save()

    def credencialIdoso(credencial: id, protocolo: pt, beneficiario: bn):
        img = Image.open(path / 'documentos' /
                         'templatesDocumentos' / "crdIdoso.jpg")
        draw = ImageDraw.Draw(img)

        font = ImageFont.truetype("arial.ttf", 24,)

        # numeroCredencial
        draw.text((715, 375), str(credencial.nCredencial).zfill(
            7), (0, 0, 0), font=font)
        # DataValidade
        draw.text((975, 487), credencial.dataValidade.strftime("%d/%m/%Y"), (0, 0, 0), font=font)
        # DAtaEmissao
        draw.text((510, 487), credencial.dataEmissao.strftime("%d/%m/%Y"), (0, 0, 0), font=font)
        # nome
        draw.text((490, 880), str(beneficiario.nome).upper(), (0, 0, 0), font=font)
        img.save(path / 'documentos' /'templatesDocumentos' /
                 '{0}.jpg'.format(protocolo.nProtocolo))

    def credencialDeficiente(credencial: df, protocolo: pt, beneficiario: bn):
        img = Image.open(path / 'documentos' /
                         'templatesDocumentos' / "crdDeficiente.jpg")
        draw = ImageDraw.Draw(img)

        font = ImageFont.truetype("arial.ttf", 28,)

        # nCredencial
        draw.text((749, 378), str(credencial.nCredencial).zfill(
            7), (0, 0, 0), font=font)
        # datavalidade
        draw.text((375, 485), credencial.dataValidade.strftime("%d/%m/%Y"), (0, 0, 0), font=font)
        # nome
        draw.text((490, 880), str(beneficiario.nome).upper(), (0, 0, 0), font=font)
        img.save(path / 'documentos' / 'templatesDocumentos' / '{0}.jpg'.format(protocolo.nProtocolo))

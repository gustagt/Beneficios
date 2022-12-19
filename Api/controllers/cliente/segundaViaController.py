from flask import  request, render_template, make_response
from models.beneficiario import Beneficiario as bn
from models.deficiente import Deficiente as df
from models.idoso import Idoso as id    
from models import erros as e    

import re

class SegundaViaController:
    def segundaViaGET():
        return render_template('cliente/segundaVia.html')
    
    def segundaViaPOST(request: request):
        nCredencial = request.form['nCredencial']
        cpf = re.sub("[^0-9]", "",str(request.form['cpf']))
        tpCredencial = request.form['tpCredencial']

        if tpCredencial.lower() == 'deficiente':
            credencial = df.selectByCpf(cpf)
            if not (credencial.empty):
                nCredencialResp = credencial['n_credencial'].values[0]
                beneficiario = bn.selectByCpf(cpf)
                nome = beneficiario.nome
                if nCredencialResp == int(nCredencial):
                    resposta = make_response(render_template('cliente/solicitarBoleto.html', nCredencial=nCredencialResp, cpf=cpf, nome=nome), 200)
                    resposta.set_cookie("cpf", cpf)
                    resposta.set_cookie('tpCredencial', tpCredencial)
                    resposta.set_cookie('nCredencial', nCredencial)
                    return resposta

        elif tpCredencial.lower() == 'idoso':
            credencial = id.selectByCpf(cpf)
            if not (credencial.empty):
                nCredencialResp = credencial['n_credencial'].values[0]
                beneficiario = bn.selectByCpf(cpf)
                nome = beneficiario.nome
                if nCredencialResp == int(nCredencial):
                    resposta = make_response(render_template('cliente/solicitarBoleto.html', nCredencial=nCredencialResp, cpf=cpf, nome=nome),200)
                    resposta.set_cookie("cpf", cpf)
                    resposta.set_cookie('tpCredencial', tpCredencial)
                    resposta.set_cookie('nCredencial', nCredencial)
                    return resposta
                

        return render_template('cliente/erro.html', mensagem=e.Erros.consulta.value), 400
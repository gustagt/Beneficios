from flask import  request, render_template
from models.protocolo import Protocolo as pt
from models import erros as e

import re

class ConsultaController:
    def consultaGET():
        return render_template('cliente/consulta.html'), 200
    
    def consultaPOST(request: request):
        nProtocolo = request.form['protocolo']
        cpf = re.sub("[^0-9]", "",str(request.form['cpf']))

        if not (pt.validarProtocolo(cpf).empty):
            protocolo = pt.selectByCpf(cpf)
            if protocolo.nProtocolo == int(nProtocolo):
                return ConsultaController.renderConsula(nProtocolo)

        return render_template('cliente/erro.html', mensagem=e.Erros.consulta.value), 400
    
    def renderConsula(nProtocolo):
        return render_template("cliente/credencialEstacionamento.html", nProtocolo=nProtocolo )
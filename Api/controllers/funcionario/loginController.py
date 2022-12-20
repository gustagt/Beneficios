from flask import  request, render_template
from models.protocolo import Protocolo as pt
from models import erros as e

import re

class ConsultaController:
    def consultaGET():
        return render_template('cliente/consulta.html'), 200
    
    def consultaPOST(request: request):
        usuario = request.form['usuario']
        senha = request.form['senha']
        
        if True :
            return render_template("funcionario/login.html")


        return render_template('cliente/erro.html', mensagem=e.Erros.consulta.value), 400
    

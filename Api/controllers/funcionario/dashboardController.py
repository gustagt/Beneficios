from flask import request, render_template, session
from models.protocolo import Protocolo as pt
from models.beneficiario import Beneficiario as bn
from models.idoso import Idoso as id
from models.deficiente import Deficiente as df

from helpers import helpers as hp
from models import erros as e


from ldap3 import *

ptc = 'protocolo'
crd = 'credencial'


class DashboardController:

    # login
    def dashboardLoginPOST(key):
        usuario = request.form['usuario']
        senha = request.form['senha']

        server = Server('10.101.22.3', 389)

        conn = Connection(server,  user="pmc.intra\\"+usuario,
                          password=senha,  authentication=NTLM)
        if not conn.bind():

            return render_template('cliente/erro.html', mensagem=e.Erros.consulta.value), 400
        else:

            obj_inetorgperson = ObjectDef('user', conn)
            obj_inetorggroup = ObjectDef('group', conn)
            r = Reader(conn, obj_inetorggroup,
                       'cn=TRANSCON - BENEFICIOS,ou=GRUPOS,ou=TRANSCON,ou=PREFEITURA,dc=pmc,dc=intra')

            r.search()

            membro = r.entries[0].member

            for name in membro:

                p = Reader(conn, obj_inetorgperson, name)
                p.search()
                matricula = str(p[0].userPrincipalName).split('@')[0]

                if usuario == matricula:
                    lista = pt.listAll()
                    beneficiarios = bn.listAll().set_index('cpf')
                    nome2 = str(name).replace(',', ' ')
                    nome = str(name).split()[0][3:]
                    nome = nome + ' ' + str(nome2).split()[1]
                    session['nomeUsuario'] = nome
                    session['token'] = hp.auth(key)
                    return render_template("funcionario/dashboard.html", subtitulo='Protocolos', lista=lista, linhas=len(lista), beneficiarios=beneficiarios, nomeUsuario=nome, servico=ptc), 200

            conn.unbind()

        return render_template('cliente/erro.html', mensagem=e.Erros.consulta.value), 400
    
    # protocolos
    def protocoloGET():
        lista = pt.listNaoFinalizados()
        beneficiarios = bn.listAll().set_index('cpf')
        nome = session['nomeUsuario']
        return render_template("funcionario/dashboard.html", subtitulo='Protocolos', lista=lista, linhas=len(lista), beneficiarios=beneficiarios, nomeUsuario=nome, servico=ptc), 200
    
    def protocoloIdosoGET():
        lista = pt.listAllIdosos()
        beneficiarios = bn.listAll().set_index('cpf')
        nome = session['nomeUsuario']
        return render_template("funcionario/dashboard.html", subtitulo='Protocolos referente a Idosos', lista=lista, linhas=len(lista), beneficiarios=beneficiarios, nomeUsuario=nome, servico=ptc), 200
    
    def protocoloDeficienteGET():
        lista = pt.listAllDeficientes()
        beneficiarios = bn.listAll().set_index('cpf')
        nome = session['nomeUsuario']
        return render_template("funcionario/dashboard.html", subtitulo='Protocolos referente a Deficientes', lista=lista, linhas=len(lista), beneficiarios=beneficiarios, nomeUsuario=nome, servico=ptc), 200
    
    def protocoloBoletoGET():
        lista = pt.listAllBoletos()
        beneficiarios = bn.listAll().set_index('cpf')
        nome = session['nomeUsuario']
        return render_template("funcionario/dashboard.html", subtitulo='Protocolos referente a 2° Via', lista=lista, linhas=len(lista), beneficiarios=beneficiarios, nomeUsuario=nome, servico=ptc), 200
    
    def protocoloFinalizadoGET():
        lista = pt.listFinalizados()
        beneficiarios = bn.listAll().set_index('cpf')
        nome = session['nomeUsuario']
        return render_template("funcionario/dashboard.html", subtitulo='Protocolos Finalizados', lista=lista, linhas=len(lista), beneficiarios=beneficiarios, nomeUsuario=nome, servico=ptc), 200
    
    # credenciais
    
    def credenciaisIdosoGET():
        lista = id.listAllConcluidos()
        beneficiarios = bn.listAll().set_index('cpf')
        nome = session['nomeUsuario']
        session["tipoCredencial"] = "idoso"
        return render_template("funcionario/dashboard.html", subtitulo='Credenciais de Idoso', lista=lista, linhas=len(lista), beneficiarios=beneficiarios, nomeUsuario=nome, servico=crd), 200
    
    def credenciaisDeficienteGET():
        lista = df.listAllConcluidos()
        beneficiarios = bn.listAll().set_index('cpf')
        nome = session['nomeUsuario']
        session["tipoCredencial"] = "deficiente"
        return render_template("funcionario/dashboard.html", subtitulo='Credenciais de Deficiente', lista=lista, linhas=len(lista), beneficiarios=beneficiarios, nomeUsuario=nome, servico=crd), 200
    

    
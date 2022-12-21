from flask import request, render_template, Response
from models.protocolo import Protocolo as pt
from models import erros as e


from ldap3 import *


class LoginController:
    def consultaGET():
        return render_template('funcionario/login.html'), 200

    def consultaPOST(request: request):
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
                    return 'ok'

            conn.unbind()

        return render_template('cliente/erro.html', mensagem=e.Erros.consulta.value), 400






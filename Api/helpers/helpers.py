from flask import request, render_template, session
import jwt
import datetime




def auth(key):
    auth = request.form
    if auth:
    
        vencimento =datetime.datetime.now() + datetime.timedelta(hours=12)

        token = jwt.encode({'user': auth['usuario'],'exp': vencimento}, key, algorithm="HS256")
        return token


from flask import render_template



class LoginController:
    def loginGET():
        return render_template('funcionario/login.html'), 200






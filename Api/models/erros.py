from enum import Enum

class Erros(Enum):
    formularioIdoso = 'Já existe um cadastro com esse cpf para a Credencial de Idoso.'
    formularioDeficiente = 'Já existe um cadastro com esse cpf para a Credencial de Deficiente.'
    consulta = 'Dados inseridos não encontrados.'
    email = 'Email já está em uso. Tente usar outro email.'
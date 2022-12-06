from enum import Enum

class Erros(Enum):
    formularioIdoso = 'Já existe um cadastro com esse cpf ou email para a Credencial de Idoso.'
    formularioDeficiente = 'Já existe um cadastro com esse cpf ou email para a Credencial de Deficiente.'
    consulta = 'Dados inseridos não encontrados.'
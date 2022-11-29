from flask import Flask, request, render_template, flash
from models import beneficiario as bn
from models import deficiente as df
from models import idoso as id
from werkzeug.utils import secure_filename 
import os


app = Flask(__name__)
app.secret_key = 'gusta'

caminhoDocumentos = 'C:/Users/0103250/Documents/Beneficios/Api/documentos/'

# Rota /devs -> LISTAR todos os desenvolvedores cadastrados


@app.route('/beneficiarios', methods=['GET'])
def beneficiarios():
    beneficiarios = bn.Beneficiario.listAll().to_json(orient='index')
    return beneficiarios, 200


@app.route('/', methods=['POST'])
def teste():
    cpf = request.form["cpf"]
    
   
    return cpf
    

# Rota /devs -> LISTAR todos os desenvolvedores cadastrados


@app.route('/beneficiarios/deficiente/nova-credencial', methods=['POST'])
def novaCredencialDeficiente():
    # Check dos dados
    cpf = request.form['cpf']
    
    duplicidade = df.Deficiente.selectByCpf(cpf)
    
    if duplicidade.empty:
        
        nome = request.form['nome']
        dataNascimento = request.form['dataNascimento']
        celular = request.form['celular']
        rg = request.form['rg']
        email = request.form['email']
        genero = request.form['sexo']
        telefone = request.form['telefone']
        
        deficiencia = request.form['tpDeficiencia']
        repLegal = request.form['Rep_Legal']
        

        cep = request.form['cep']
        rua = request.form['rua']
        num = request.form['num']
        complemento = request.form['complemento']
        bairro = request.form['bairro']
        cidade = request.form['cidade']
        

        endereco = rua + ' ' + num + ' ' + complemento + \
            " " + bairro + " " + cidade + ' ' + cep
    
        cpResidencia = request.files['cpResidencia']
        laudoPericial = request.files['laudoPericial']
        dcOfFoto = request.files['dcOfFoto']
        
        caminho = caminhoDocumentos + 'deficientes/' + cpf
    
        os.mkdir(caminho)
        
        beneficiario = bn.Beneficiario(cpf, nome, dataNascimento, endereco, celular, rg, email, genero, caminho)
        credencialD =df.Deficiente(deficiencia, cpf)
               
        cpResidencia.save(os.path.join(caminho,secure_filename(cpResidencia.filename)))
        laudoPericial.save(os.path.join(caminho,secure_filename(laudoPericial.filename)))
        dcOfFoto.save(os.path.join(caminho,secure_filename(dcOfFoto.filename)))               

        if telefone != '':
            beneficiario.telefone = telefone
        
        if repLegal.lower() == 'sim':
            nResponsavel = request.form['nResponsavel']
            dResponsavel = request.files['dResponsavel']
            dResponsavel.save(os.path.join(caminho,secure_filename(dResponsavel.filename)))
            beneficiario.repLegal=nResponsavel
                       
        if bn.Beneficiario.selectByCpf(cpf).empty: 
            beneficiario.add()
        else:
            beneficiario.updateByCpf()
            
        credencialD.add()
        return 'ok', 200
    
    else:
        return 'Pedido ja existente', 400
    
    
@app.route('/beneficiarios/idoso/nova-credencial', methods=['POST'])
def novaCredencialIdoso():
  
    cpf = request.form['cpf']
    
    duplicidade = id.Idoso.selectByCpf(cpf)
    
    if duplicidade.empty:
        
        nome = request.form['nome']
        dataNascimento = request.form['dataNascimento']
        celular = request.form['celular']
        rg = request.form['rg']
        email = request.form['email']
        genero = request.form['sexo']
        telefone = request.form['telefone']
        
        repLegal = request.form['Rep_Legal']

        cep = request.form['cep']
        rua = request.form['rua']
        num = request.form['num']
        complemento = request.form['complemento']
        bairro = request.form['bairro']
        cidade = request.form['cidade']
        

        endereco = rua + ' ' + num + ' ' + complemento + \
            " " + bairro + " " + cidade + ' ' + cep
    
        cpResidencia = request.files['cpResidencia']
        dcOfFoto = request.files['dcOfFoto']
        
        caminho = caminhoDocumentos +'idosos/'+ cpf
    
        os.mkdir(caminho)
        
        beneficiario = bn.Beneficiario(cpf, nome, dataNascimento, endereco, celular, rg, email, genero, caminho)
        credencialD =id.Idoso(cpf)
        
               
        cpResidencia.save(os.path.join(caminho,secure_filename(cpResidencia.filename)))
        dcOfFoto.save(os.path.join(caminho,secure_filename(dcOfFoto.filename)))               

        if telefone != '':
            beneficiario.telefone = telefone
        
        if repLegal.lower() == 'sim':
            nResponsavel = request.form['nResponsavel']
            dResponsavel = request.files['dResponsavel']
            dResponsavel.save(os.path.join(caminho,secure_filename(dResponsavel.filename)))
            beneficiario.repLegal=nResponsavel
                       
        if bn.Beneficiario.selectByCpf(cpf).empty: 
            beneficiario.add()
        else:
            beneficiario.updateByCpf()
            
        credencialD.add()
        return 'ok', 200
    
    else:
        return 'Pedido ja existente', 400
    
    
if __name__ == '__main__':
    app.run(debug=True)

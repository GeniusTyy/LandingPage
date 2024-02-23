from datetime import datetime
from flask import render_template, request, redirect, session, jsonify
from core import app, models, PATH_DB

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        # Captura os dados do formulário
        email = request.form.get('email')

        currente_time = datetime.now().strftime("%d-%m-%Y")
        adiciona_email(email, currente_time)        

        # variavel responsavel por impedir que a rota "/success" seja acessada externamente.
        session['valid'] = True 

        # Pode redirecionar para outra rota, por exemplo, 'success'
        return redirect('/success')

    # Se o método for GET ou o formulário ainda não foi enviado, renderiza o template padrão
    return render_template('index.html')

# Função para adicionar o e-mail no banco de dados.
def adiciona_email(email:str, data:str):
    with models.DataBase(PATH_DB) as db:
        db._append(email, data)

@app.route('/success')
def success():
    if session.get('valid') == True:
        return render_template('success.html')

    return redirect('/')

# TODO: Restringir essa aberração.
@app.route('/data')
def data():
    response = {"data": {"users": []}}

    with models.DataBase(PATH_DB) as db:
        usuarios = db._get_all()

        for id, email, data in usuarios:
            user = {
                "id": id,
                "email":email,
                "data":data
            }
            
            response['data']['users'].append(user)

    return jsonify(response)

# Caso a rota solicitada não exista redireciona para a pagina inicial.
@app.errorhandler(404)
def page_not_found(e):
    return redirect('/')
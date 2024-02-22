from flask import render_template, request, redirect, session, jsonify
from core import app, models, PATH_DB

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        # Captura os dados do formulário
        email = request.form.get('email')

        adiciona_email(email)        

        # variavel responsavel por impedir que a rota "/success" seja acessada externamente.
        session['valid'] = True 

        # Pode redirecionar para outra rota, por exemplo, 'success'
        return redirect('/success')

    # Se o método for GET ou o formulário ainda não foi enviado, renderiza o template padrão
    return render_template('index.html')

# Função para adicionar o e-mail no banco de dados.
def adiciona_email(email:str):
    with models.DataBase(PATH_DB) as db:
        db._append(email)

@app.route('/success')
def success():
    if session.get('valid'):
        return render_template('success.html')

    return redirect('/')

@app.route('/data')
def data():
    response = {}
    with DataBase(PATH_DB) as db:
        cache = db._get_all()
        if cache:
            for id, email in cache:
                response["data"][id] = email
        return jsonify(response)

# Caso a rota solicitada não exista redireciona para a pagina inicial.
@app.errorhandler(404)
def page_not_found(e):
    return redirect('/')
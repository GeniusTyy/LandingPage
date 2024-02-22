from flask import render_template, request, redirect, session, jsonify
from core import app

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        # Captura os dados do formulário
        email = request.form.get('email')

        # Faça o que desejar com os dados, por exemplo, imprimir no console
        print(f'E-mail recebido: {email}')

        # variavel responsavel por impedir que a rota "/success" seja acessada externamente.
        session['valid'] = True 

        # Pode redirecionar para outra rota, por exemplo, 'success'
        return redirect('/success')

    # Se o método for GET ou o formulário ainda não foi enviado, renderiza o template padrão
    return render_template('index.html')


@app.route('/success')
def success():
    if session.get('valid'):
        return render_template('success.html')

    return redirect('/')

# Caso a rota solicitada não exista redireciona para a pagina inicial.
@app.errorhandler(404)
def page_not_found(e):
    return redirect('/')
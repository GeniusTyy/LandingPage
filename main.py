from flask import Flask, render_template, request, redirect

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        # Captura os dados do formulário
        email = request.form.get('email')

        # Faça o que desejar com os dados, por exemplo, imprimir no console
        print(f'E-mail recebido: {email}')

        # Pode redirecionar para outra rota, por exemplo, 'success'
        render_template('success.html')

    return render_template('index.html')



if __name__ == '__main__':
    app.run(debug=True)

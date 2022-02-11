from flask import Flask, render_template, request, escape  #Esse é o nome da Classe: "Flask" com "F" maiúsculo.
from vsearch import search4letters
#Este é o nome do módulo "flask" com "f" minúsculo.
app = Flask(__name__) #Cria uma instância de um objeto Flask e atribui à variável "app".


def log_request(req: 'flask_request', res: str) -> None:
    with open('vsearch.log', 'a') as log:
        print(req.form, req.remote_addr, req.user_agent, res, file=log, sep='|')


@app.route('/search4', methods=['POST'])
def do_search() -> 'html':
    phrase = request.form['phrase']
    letters = request.form['letters']
    title = 'Here are you results: '
    results = str(search4letters(phrase,letters))
    log_request(request, results)
    return render_template('results.html',
                           the_phrase=phrase,
                           the_letters=letters,
                           the_title=title,
                           the_results=results,)

@app.route('/')
@app.route('/entry')
def entry_page() -> 'html':
    return render_template('entry.html', the_title='Welcome to search4letters on the web!')


@app.route('/viewlog')
def view_the_log() -> str:
    with open('vsearch.log') as log:
        contents = log.read()
    return escape(contents)


if __name__ == '__main__':
    app.run(debug=True) #pede ao aplicativo web para começar a execução.

#-------------COMENTÁRIOS IMPORTANTE SOBRE A URL USADA--------------------

#1º#    127.0.0.1 é o LOCALHOST ----> é uma abreviação de: " meu computador, não suporta o endereço IP real."

#2º#  :5000 da URL indica o número de porta do protocolo na qual o seu servidor web está em execução. ( o padrão da
# Internet é a porta do protocolo 80.) Alguns usam :8080 como porta de protocolo teste, mas o Flask usa a porta de
# protocolo teste :5000.

#----------------------------------------------------------
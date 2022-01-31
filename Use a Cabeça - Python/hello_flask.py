from flask import Flask #Esse é o nome da Classe: "Flask" com "F" maiúsculo.
from vsearch import search4letters
#Este é o nome do módulo "flask" com "f" minúsculo.
app = Flask(__name__) #Cria uma instância de um objeto Flask e atribui à variável "app".


@app.route('/search4')  #Decorador da Função "hello()": ajusta o comportamento de uma função existênte(sem mudar o código)
def do_search() -> str: #uma função normal: a notação '-> str' retorna uma string.
    return str(search4letters('life, the universe, and everything.', 'eiru,!'))

app.run() #pede ao aplicativo web para começar a execução.

#-------------COMENTÁRIOS IMPORTANTE SOBRE A URL USADA--------------------

#1º#    127.0.0.1 é o LOCALHOST ----> é uma abreviação de: " meu computador, não suporta o endereço IP real."

#2º#  :5000 da URL indica o número de porta do protocolo na qual o seu servidor web está em execução. ( o padrão da
# Internet é a porta do protocolo 80.) Alguns usam :8080 como porta de protocolo teste, mas o Flask usa a porta de
# protocolo teste :5000.

#----------------------------------------------------------
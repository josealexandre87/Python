import os
import requests

def baixar_arquivo(url, endereco):
   # faz requisição ao servidor
    resposta =  requests.get(url)
    if resposta.status_code == requests.codes.OK:
        with open(endereco, 'wb') as novo_arquivo:
            novo_arquivo.write(resposta.content)
        print('Donwload finalizado. Salvo em: {}'.format(endereco))
    else:
        resposta.raise_for_status()
    
    
if __name__ == "__main__":
    BASE_URL = 'https://estacio.webaula.com.br/cursos/DIS079/galeria/aula1/anexo/aula{}.pdf'
    py_teste = 'py_teste'

    for i in range(0, 11):
        nome_arquivo = os.path.join(py_teste, 'aulas_{}'.format(i))
        baixar_arquivo(BASE_URL.format(i), nome_arquivo)
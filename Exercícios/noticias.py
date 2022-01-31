import requests
from bs4 import BeautifulSoup
import pandas as pd

lista_noticias = [] #criada variavel para armazenar uma lista com listas das Noticias(titulo, subtitulo e link).

response = requests.get('https://g1.globo.com/') #recebe a resposta de requisição para o site g1.
content = response.content #armazena o conteudo na variavel content.

site = BeautifulSoup(content, 'html.parser') #diz que o que vai ser usado é HTML.
#HTML da Notícia
noticias = site.findAll('div', attrs={'class': 'feed-post-body'}) #dentro da HTML vai procurar div com a class.

for noticia in noticias: #vai fazer loop em noticias para cada item dentro dela ancontrado e irá printar.
    #Título da Notícia
    titulo = noticia.find('a', attrs={'class': 'feed-post-link'})

    print(titulo.text)
    print(titulo['href']) #pega o link da notícia etorna executável dentro do PyCharm, abrindo no Browser.
    #Subtitulo da Notícia
    subtitulo = noticia.find('div', attrs={'class': 'feed-post-body-resumo'})

    if (subtitulo): #para caso encontre o texto, printa. Para ele não quebra o loop e continuar.
        print(subtitulo.text)
        lista_noticias.append([titulo.text, subtitulo.text, titulo['href']]) #add na variálvel se tiver subtitulo.
    else:
        lista_noticias.append([titulo.text, '', titulo['href']]) #se não tiver subtitilo, add a string ''.
    print()

news = pd.DataFrame(lista_noticias, columns=['Título', 'Subtítulo', 'Link']) #gera um DataFrame com 3 colunas.

news.to_excel('noticias.xlsx', index=False) #gera um arquivo em excel com os dado do DataFrame 'news'.

print(news)
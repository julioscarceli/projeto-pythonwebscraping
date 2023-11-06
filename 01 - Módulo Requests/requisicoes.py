import requests
from bs4 import BeautifulSoup
import pandas as pd


lista_noticias = []



response = requests.get('https://g1.globo.com/') #aqui eu solicitei ao servidor uma resposta do site do G1 com o metodo get


content = response.content  #aqui eu guardei o conteudo do site na variavel *content*


site = BeautifulSoup(content, 'html.parser', ) #aqui criei uma variavel chamada site, e joguei o proprio site dentro dela, vai ser o resultado do Beautiful 
#Soup que é o metodo que utilizamos.#
#PRIMEIRO PARAMETRO dentro do Beautiful Soup é o conteudo html que a gente requisitou (content), SEGUNDO PARAMETRO eu tenho que especificar o html e coloquei
#o 'html.parser' , estou entregando ao beautiful soup o conteudo html e alem disso eu quero que ele converta  ele pra html mesmo



#HTML DA NOTICIA
noticias = site.findAll('div', attrs= {'class': 'feed-post-body'} )  #esse metodo chama find, ele serve pra encontrar a tag em que voce esta interessado no html 
#nesse metodo find, coloquei o primeiro parametro que é a tag que estou interessado, no caso DIV, e o segundo parametro é qual é o atributo (attrs=)
#que vai nos ajudar achar aquela tag especifica, pois no html tem varias tags DIV


for noticia in noticias:

    #Titulo
    titulo = noticia.find('a', attrs= {'class': 'feed-post-link'})

    #print(titulo.text) 

    #Subtitulo
    subtitulo = noticia.find('div', attrs= {'feed-post-body-resumo'})

    if(subtitulo):
        #print(subtitulo.text)
        lista_noticias.append([titulo.text, subtitulo.text,titulo['href']])
    else:
        lista_noticias.append([titulo.text, '', titulo['href']])


news = pd.DataFrame(lista_noticias, columns=['Titulo', 'Subtitulo', 'Link'])

news.to_excel('noticias.xlsx' , index=False)

#print(news)

    






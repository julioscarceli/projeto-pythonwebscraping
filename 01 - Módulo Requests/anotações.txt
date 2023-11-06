import requests
from bs4 import BeautifulSoup

response = requests.get('https://g1.globo.com/') #aqui eu solicitei ao servidor uma resposta do site do G1 com o metodo get


content = response.content  #aqui eu guardei o conteudo do site na variavel *content*


site = BeautifulSoup(content, 'html.parser', ) #aqui criei uma variavel chamada site, e joguei o proprio site dentro dela, vai ser o resultado do Beautiful 
#Soup que é o metodo que utilizamos.#
#PRIMEIRO PARAMETRO dentro do Beautiful Soup é o conteudo html que a gente requisitou (content), SEGUNDO PARAMETRO eu tenho que especificar o html e coloquei
#o 'html.parser' , estou entregando ao beautiful soup o conteudo html e alem disso eu quero que ele converta  ele pra html mesmo



#HTML DA NOTICIA
noticia = site.find('div', attrs= {'class': 'feed-post-body'} )  #esse metodo chama find, ele serve pra encontrar a tag em que voce esta interessado no html 
#nesse metodo find, coloquei o primeiro parametro que é a tag que estou interessado, no caso DIV, e o segundo parametro é qual é o atributo (attrs=)
#que vai nos ajudar achar aquela tag especifica, pois no html tem varias tags DIV

#Titulo da noticia
titulo = noticia.find('a', attrs= {'feed-post-link'})

print(titulo.text)


#Subtitulo 
subtitulo = noticia.find('div', attrs= {'class': 'bstn-fd-relatedtext'})

print(subtitulo.text)
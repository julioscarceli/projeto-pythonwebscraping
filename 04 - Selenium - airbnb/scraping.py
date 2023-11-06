import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.firefox.options import Options

options = Options()
options.add_argument('window-size=400,800')



navegador = webdriver.Firefox(options=options)

navegador.get('https://www.airbnb.com')

print(navegador.page_source)


#response = requests.get('https://www.airbnb.com.br/')


#print(site.prettify())
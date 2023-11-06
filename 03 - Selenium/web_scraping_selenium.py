from selenium import webdriver
var = webdriver.Firefox(executable_path=r'C:\Users\user\Documents\projetos\webscraping-python\projeto-pythonwebscraping\03 - Selenium')


navegador = webdriver.Firefox()

navegador.get('https://www.walissonsilva.com/blog')


# Encontre um elemento de entrada (input) por nome da tag
elemento = navegador.find_element('input')

# Ou, encontre um elemento de entrada (input) por ID
# elemento = navegador.find_element(By.ID, 'id_do_campo_input')

print(elemento)

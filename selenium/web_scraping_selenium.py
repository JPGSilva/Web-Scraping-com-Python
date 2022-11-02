from selenium import webdriver
from time import sleep
from requisicoes import requisicoes

navegador = webdriver.Chrome()

navegador.get('https://www.walissonsilva.com/posts/diferentes-formas-de-criar-um-dataframe')
elemento = navegador.find_element_by_tag_name('input')
elemento.send_keys('data')
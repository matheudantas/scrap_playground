from urllib.request import urlopen
from bs4 import BeautifulSoup

html = urlopen('http://pythonscraping.com/pages/page1.html')
# html.parser é built-in em python3
bs = BeautifulSoup(html.read(), 'html.parser')
print(bs)
print(bs.h1)
print(bs.body.h1)

"""
    Como opção de parser temos o lxml, sendo mais vantajoso
    para HTMLs confusos ou mal formatados, porém depende de 
    bibliotecas C terceiros para funcionar.
    Outra opção conhecida é o html5lib, também vantajoso
    para correção de HTML com falhas, porém mais lento
    comparado ao lxml e ao html.parser
"""
html = urlopen('http://pythonscraping.com/pages/page1.html')
bs = BeautifulSoup(html.read(), 'lxml')
print('usando lxml:', bs.html.body)

html = urlopen('http://pythonscraping.com/pages/page1.html')
bs = BeautifulSoup(html.read(), 'html5lib')
print('usando html5lib:', bs.h1)

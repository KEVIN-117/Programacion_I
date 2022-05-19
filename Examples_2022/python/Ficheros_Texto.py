from io import open
import urllib.request
from bs4 import BeautifulSoup
#from nbformat import read
datos = urllib.request.urlopen('https://www.w3schools.com/js/js_const.asp').read().decode()
soup = BeautifulSoup(datos)
tags = soup('li')
#archivo = open("python\contenedor.txt", "w")
for tag in tags:
  print(tag)
  #archivo.write(tag.text+"\n")
#archivo.close()
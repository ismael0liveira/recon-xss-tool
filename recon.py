import requests
from bs4 import BeautifulSoup
import urllib3     
import sys     
import pyfiglet
import os

banner = pyfiglet.figlet_format("HIDDENS!!")
print('\033[32;1m')
print(banner)
print('\033[m')

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)     
     
url=sys.argv[1]     
     
requisicao = requests.get(url, verify=False)

html=BeautifulSoup(requisicao.content, 'html.parser')


inputs=html.findAll('input', attrs={'type':'hidden'})

with open('urls.txt', 'a') as arquivo:
    for i in inputs:
        arquivo.write(url+'/?'+i['name']+'='+'\n')


os.system('cat urls.txt | dalfox pipe')







import requests
from bs4 import BeautifulSoup

res = requests.get('https://www.ptt.cc/bbs/Tech_Job/index.html')
res.encoding = 'utf8'
soup = BeautifulSoup(res.text, "html.parser")

for i in soup.findAll('a'):
    if "正".decode('big5') in i.get_text():
        print i


from .const import URL, headers
from bs4 import BeautifulSoup
import requests

def fetch_word(payload):
    a_words = payload.find_all("a", "load_word")
    words = payload.find_all("span", style="padding: 0")
    a = []
    for word in words:
        if(word.text != ', '):
            a.append(word.text)
    for word in a_words:
        a.append(word.text)
    return a

def scrap_page(keyword):
    x = str(keyword)
    url = "%s%s/"%(URL,x)
    page = requests.get(url, headers=headers)
    soup = BeautifulSoup(page.content, 'html.parser')
    
    return soup
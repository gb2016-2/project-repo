import urllib.request
from bs4 import BeautifulSoup as Soup
import re
import codecs
from time import gmtime, strftime
from datetime import datetime
from Append_DB import Write_DB


count = 1
deep = 5
def search(parents):
    global count
    Urls = []
    if str(type(parents)) == "<class 'str'>":
        parents = [parents]
    
    
    for parent in parents:
        print(len(parents))
        
        ufile = urllib.request.urlopen(parent)
        url_soup = Soup(ufile , "html.parser")
        for a in url_soup.find_all('a', href=True):
            if parent in a['href']:
                Urls.append(str(a['href']))
            elif 'http' and '.' not in a['href']:
                Urls.append(parent + str(a['href']))
        if deep != count:
            count += 1
            search(Urls)
        URLS = [('1' , x , str(datetime.now().strftime("%Y-%m-%d")))for x in Urls]    
        x = Write_DB(URLS)
        x.write_db()
    print(Urls)
        
            

if __name__ == '__main__':
    search('http://lenta.ru')

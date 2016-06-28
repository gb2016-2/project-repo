from requests import get as getData
import urllib.request
import re
import codecs
from bs4 import BeautifulSoup as Soup
import gzip
from time import gmtime, strftime
from datetime import datetime
import sys


class Linklist(): 
    def __init__(self, id_parent, id_url, url_site , lastSD): # check the start of the original string on 'http'
        if 'http' in url_site:
            self.url_site = url_site
        else:
            self.url_site = 'http://' + self.url_site # add a protocol 
        self.id_parent = id_parent
        self.lastSD = lastSD
        self.id_url = id_url

    def url_chek(self): # available of a page
        try:
            ufile = urllib.request.urlopen(self.url_site)
            url_soup = Soup(ufile , "html.parser")
            if '404' in url_soup.findAll(name='title'):
                return False
            else:
                print(str(self.url_site) + ' good url')
                return True
                
                      
        except urllib.error.HTTPError:
            print('urllib.error.HTTPError')
            return False
           
    
        
    def extract(self): 
        if Linklist.url_chek(self):
            ufile = urllib.request.urlopen(self.url_site)
            #file_i = open('text.txt', 'a')
            try:
                url_string = gzip.open(ufile, 'rb').read().decode('UTF-8')
                url_soup = Soup(url_string , "html.parser")
                List = []
                for i in url_soup.findAll(name='url'):
                    url = ''.join(re.findall(r'<.*?>(http.*?)<.*?>', str(i)))
                    lastmod = ''.join(re.findall(r'<lastmod>(http.*?)</lastmod>', str(i)))	
                    #file_i.write(self.id_parent + ',' + self.id_url + ',' + url + ' ' + datetime.now().strftime("%d-%m-%Y %H:%M") + lastmod +'\n')
                    List.append(tuple( [self.id_parent, self.id_url, url , datetime.now().strftime("%d-%m-%Y %H:%M"), self.lastSD]))
                return List   
            except:
                print(str(self.url_site) + ' not a gzipped file')
                pass  
        else:
            pass
        

def main(x):
    z = Linklist('1', '1', x, 'empty')
    y = z.extract()
    file = open('test_log.txt', 'a')
    for x in y:
        file.write(str(x) + '\n')
     
"""if __name__ == '__main__':
    print('Its testing run. Enter you xml as http://sitemap.xml.gz')
    x = input()
    main(x)"""

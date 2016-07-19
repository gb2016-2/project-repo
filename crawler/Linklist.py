import re
import codecs
import sys
import threading
import time
import urllib.request
from time import gmtime, strftime
from datetime import datetime

from requests import get as getData
from bs4 import BeautifulSoup as Soup
import gzip


class Linklist():
    
    def __init__(self, ID, url_site):
        #check the start of the original string on 'http'
        if 'http' in url_site: 
            self.url_site = url_site
        else:
            self.url_site = 'http://' + self.url_site # add a protocol 
        self.ID = ID
        

    def url_chek(self): # available of a page
        try:
            ufile = urllib.request.urlopen(self.url_site)
            url_soup = Soup(ufile , "html.parser")
            
            if '404' in url_soup.findAll(name='title'):
                return False
            else:
                return True             
        except urllib.error.HTTPError:
            print('urllib.error.HTTPError')
            return False
           
        
    def extract(self):
        
        List = []

        def tread_add_list(url):
            date = str(datetime.now().strftime("%Y-%m-%d"))
            List.append(tuple( [self.ID, url , date]))

            
        def extr(ufile,List):
            print('start thread')
            try:
                print('try open gz')
                url_string = gzip.open(ufile, 'rb').read().decode('UTF-8')
                url_soup = Soup(url_string , "html.parser")
                THR = [] 
                
                for i in url_soup.findAll(name='url'):
                    url = ''.join(re.findall(r'<.*?>(http.*?)<.*?>', str(i)))
                    refind = re.findall(r'<lastmod>(http.*?)</lastmod>',str(i))
                    lastmod = ''.join(refind)
                    
                    x = threading.Thread(target=tread_add_list, args=(url,))
                    x.start()
                    THR.append(x)
                    
                for t in THR:
                    t.join()
                print( str(len(url_soup.findAll(name='url'))) \
                       + 'added data tuple in' + str(len(List)))  
            except:
                print(str(ufile) + ' not a gzipped file')
                pass  
        
        if Linklist.url_chek(self):
            ufile = urllib.request.urlopen(self.url_site)
            extr(ufile,List)       
        else:
            pass
        
        print(len(List))
        return List
        
def main():
    z = Linklist('1','http://lenta.ru/news/sitemap.xml.gz')
    y = z.extract()
    file = open('test_log.txt', 'a')
    
    for x in y:
        file.write(str(x) + '\n')
    print('File whith url white')
    file.close()
if __name__ == '__main__':
    print('Its testing run. Enter to start')
    x = input()
    main()

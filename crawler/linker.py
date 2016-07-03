from requests import get as getData
import re
import codecs
from bs4 import BeautifulSoup as Soup
from Linklist import Linklist
from Append_DB import Write_DB
import threading
import time

def url_chek(url_site): # available of a page #добавить проверку на специфичный xml
        try:
            ufile = getData(url_site)
            if str(ufile) == '<Response [404]>':
                return False
            elif str(ufile) == '<Response [200]>':
                return True
        except TypeError:
            return False     
        except:
            print('404')
            return False
        


def append_DB(id_parent, url_site):



    if url_chek(url_site):  # check links 
        ufile = getData(url_site).content #get conten of data file
        url_soup = Soup( str(ufile) , "html.parser") # parse the structur
        List_Urls = []
        for i in url_soup.findAll(name='loc'): #find all urls
            
            url = ''.join(re.findall(r'<.*?>(http.*?)<.*?>', str(i))) #get http
            
            
            if 'sitemap' in url: #check template entry
                x = Linklist(id_parent, url)
                """try:"""
                ex = threading.Thread(target=List_Urls.extend, args=(x.extract(),))
                ex.start()
                
                """except TypeError:
                    print('TypeError')
                    pass"""
            else:
                print('fucking shit')
                pass
        while threading.activeCount() > 1:
            time.sleep(20)
            print('In linker: ' + str(threading.activeCount()))
            
        x = Write_DB(List_Urls)
        x.write_db()
        
                
        print('All good')
if __name__ == '__main__':
    while 1:
        append_DB('1' , 'http://lenta.ru/sitemap.xml')
        time.sleep(86400)

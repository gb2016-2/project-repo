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
                print('404')
                return False
            elif str(ufile) == '<Response [200]>':
                print('200')
                return True
        except TypeError:
            return False     
        except:
            print('404')
            return False
        


def append_DB(id_parent, url_site):

        print('started') 
        
        

        def run_search(id_parent, url_site):
                ufile = getData(url_site).content #get conten of data file
                url_soup = Soup( str(ufile) , "html.parser") # parse the structur
                List_Urls = []
                THR = [] 
                for i in url_soup.findAll(name='loc'): #find all urls
                        url = ''.join(re.findall(r'<.*?>(http.*?)<.*?>', str(i))) #get http
            
                
                        if 'sitemap' in url: #check template entry
                                print('good') 
                                
                                
                                
                                print(url)
                                x = Linklist(id_parent, url)
                                ex = threading.Thread(target=List_Urls.extend, args=(x.extract(),))
                                ex.start()
                                THR.append(ex)
                                
                        else:
                                print('fucking shit')
                                pass
                for t in THR:
                        t.join()

                
                
        
                print(len(List_Urls))
                x = Write_DB(List_Urls)
                x.write_db()
                
        while url_chek(url_site) == False: # check links
                time.sleep(50)
        else:
               run_search(id_parent, url_site)
               pass
                
        print('All good')
if __name__ == '__main__':
   while 1:
        print('Search started')
        append_DB('1' , 'http://lenta.ru/sitemap.xml')
        print('Wait new day for update')
        sleep(86400)
        

"""The program is designed to parse and
extract data from the sitemap. Here it
is the main control unit, coordinating
act which all the others."""

import threading
import time
import re
import codecs
from requests import get as getData
from bs4 import BeautifulSoup as Soup
from Linklist import Linklist
from Append_DB import Write_DB



def url_chek(url_site): # available of a page 
        try:
            ufile = getData(url_site)
            if str(ufile) == '<Response [404]>':
                print('404 not available data \n')
                return False
            elif str(ufile) == '<Response [200]>':
                print('200 data available \n')
                return True
        except TypeError:
            return False     
        except:
            print('404 not available url \n')
            return False


def append_DB(id_parent, url_site):
        
    def run_search(id_parent, url_site):
        List_Urls = []
        THR = []
        
        ufile = getData(url_site).content #get conten of data file
        url_soup = Soup( str(ufile) , "html.parser") # parse the structur
         
        for i in url_soup.findAll(name='loc'): #find all urls
            url = ''.join(re.findall(r'<.*?>(http.*?)<.*?>', str(i))) #get http
                
            if 'sitemap' in url: #check template entry
                print('Finde sitemap url \n')      
                print(url)
                x = Linklist(id_parent, url)
                ex = threading.Thread(target=List_Urls.extend, \
                                      args=(x.extract(),))
                ex.start()
                THR.append(ex) 
            else:
                print('Url is not a sitemap url \n')
                pass
                        
        for t in THR: # waiting for the completion of all the processes
            t.join()

        print(len(List_Urls))
        x = Write_DB(List_Urls)
        x.write_db()
                
    while url_chek(url_site) == False: # link availability check
        time.sleep(50)
    else:
        print('Parsing started') 
        run_search(id_parent, url_site)
        pass
                
    print('The program ended successfully ... probably')

        
if __name__ == '__main__':
   while 1:
        print('Search started')
        append_DB('1' , 'http://lenta.ru/sitemap.xml')
        print('Wait new day for update \n')
        sleep(86400)

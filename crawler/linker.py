from requests import get as getData
import re
import codecs
from bs4 import BeautifulSoup as Soup
from Linklist import Linklist
import pymysql
import pymysql.cursors


def connect():
    """ Connect to MySQL database """
    try:
        db = pymysql.connect(host='localhost',
                             user='user',
                             password='pass',
                             db='db',
                             charset='utf8mb4',
                             cursorclass=pymysql.cursors.DictCursor)
        
        if db.is_connected():
            print('Connected to MySQL database')
        else:
            print('wrong is connected')

        try:
            with db.cursor() as cursor:
                cursor.execute('CREATE TABLE IF NOT EXISTS Pages ( SiteID INT PRIMARY AUTO_INCREMENT, ID INT , Url TEXT,  FoundDateTime TEXT, LastScanDate TEXT)')
                data = cursor.fetchone()
                print("Database version : {0} ".format(data))
                    
                print('TABLE Pages CREATED')
        except:
            print('nope')
            pass
        return db.cursor()
    except:
        print('cant connect')
        return False




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
        

def append_DB(id_parent, id_url, url_site , lastSD):
    cursor = connect()
        
    if url_chek(url_site):
        ufile = getData(url_site).content
        url_soup = Soup( str(ufile) , "html.parser")
        file_db = open('db.txt', 'a')
        List_Urls = []
        for i in url_soup.findAll(name='loc'):
            
            url = ''.join(re.findall(r'<.*?>(http.*?)<.*?>', str(i)))
            
            
            if 'sitemap' in url:
                x = Linklist(id_parent, id_url, url , lastSD)
                try:
                    List_Urls.extend(x.extract())
                except TypeError:
                    print('TypeError')
                    pass
            else:
                print('fucking shit')
                pass


        for id_parent, id_url, url , date_check , lastSD in List_Urls:
            cursor.execute('INSERT INTO Pages(ID,Url,FoundDateTime,LastScanDate) VALUES ({0},{1},{2},{3})'.format(int(id_parent), str(url) , str(date_check) , str(lastSD),))
                
            
        print('All good')
    db.close()
if __name__ == '__main__':
    append_DB('1', '0' , 'http://lenta.ru/sitemap.xml', 'None')

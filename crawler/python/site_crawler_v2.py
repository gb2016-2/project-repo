import requests
import pymysql
from bs4 import BeautifulSoup
import re


class SiteCrawler(object):

    def __init__(self, host, port, user, password, db, site):
        self.site = site
        self._all_urls = set()
        self._config = {'host': host,
                        'port': int(port),
                        'user': user,
                        'password': password,
                        'database': db,
                        'charset': 'utf8'}

    def create_table(self):
        """ First method - table creation """
        cnx = pymysql.connect(**self._config, autocommit=True)
        cur = cnx.cursor()

        pat_site_name = "(\w*).ru"
        self.site_name = re.findall(pat_site_name, self.site)[0]
        sql_create_table = "CREATE TABLE IF NOT EXISTS {} \
                            LIKE site_template;".format(self.site_name)
        cur.execute(sql_create_table)
        print('--------------------')
        print('success. db {} created or already exists'.format(self.site_name))

        cur.close()
        cnx.close()

    def get_done_urls_from_db(self):
        """ Second method - getting url which we already have in the db """

        self._done_urls = set()

        cnx = pymysql.connect(**self._config)
        cur = cnx.cursor()

        sql_get_urls = "SELECT page_url FROM {};".format(self.site_name)
        try:
            cur.execute(sql_get_urls)
            for url in cur:
                self._all_urls |= set([url[0]])
        except:
            self._all_urls = set()
        self._done_urls |= self._all_urls

        cur.close()
        cnx.close()

        self.count_pages = len(self._all_urls)
        print('--------------------')
        print("you've got {} urls already in db".format(self.count_pages))

    def parsing_site(self):
        """ Third method - get urls from site """

        current_urls = set()
        if self.count_pages == 0:
            current_urls |= self._get_urls(self.site)
        else:
            current_urls |= self._all_urls

        print('--------------------')
        print('parsing {} ...'.format(self.site))
        try:
            while len(current_urls) != 0:
                temp_current_urls = set()
                for url in current_urls:
                    temp_urls = self._get_urls(url) - self._all_urls
                    temp_current_urls |= temp_urls
                    self._all_urls |= temp_urls
                    print('\r\t', len(self._all_urls), end=' pages found      ')
                    if len(self._all_urls - self._done_urls) >= 1000:
                        break
                current_urls = temp_current_urls
        except KeyboardInterrupt:
            pass
        except Exception:
            pass

        self.count_pages = len(self._all_urls)
        print("\nok, we've found {} pages from {}".format(self.count_pages,
                                                          self.site))

    def _get_urls(self, page):
        try:
            resp = requests.get(page)
            soup = BeautifulSoup(resp.content, 'lxml')
            urls = soup.findAll('a')
        except Exception:
            return set()

        pat = '//\S*?\.((ru)|(com)).*'
        lenta = set()
        for url in urls:
            href = url.get('href')
            found_url = None
            try:
                match = re.search(pat, href).group()
                if '.lenta.ru' in match or '//lenta.ru' in match:
                    found_url = match[match.index('.ru')+3:]. \
                                       rstrip('/').lstrip('/')
            except AttributeError:
                if href is None or href is '/':
                    continue
                found_url = href.rstrip('/').lstrip('/')
            except TypeError:
                if href is None or href is '/':
                    continue
                found_url = href.rstrip('/').lstrip('/')
            if found_url is None or \
               found_url.endswith('.jpg') or \
               found_url.endswith('.jpeg'):
                continue
            lenta |= {self.site + '/' + found_url}
        return lenta

    def write_to_db(self):
        """ Fourth method - finally, saving results to db"""

        new_urls = self._all_urls - self._done_urls
        count_new_urls = len(new_urls)
        print('--------------------')
        print("we've found {} new urls".format(count_new_urls))
        if count_new_urls > 0:
            cnx = pymysql.connect(**self._config, autocommit=True)
            cur = cnx.cursor()

            print('writing pages to db...')
            for url in new_urls:
                print('\r\t', count_new_urls, end=' pages written        ')
                try:
                    sql_insert_url = "INSERT \
                                    INTO {} (page_url) \
                                    VALUES ('{}');".format(self.site_name, url)
                    cur.execute(sql_insert_url)
                except Exception:
                    continue
                except KeyboardInterrupt:
                    break
                count_new_urls -= 1
            cur.close()
            cnx.close()
            print("\nfinished")


if __name__ == '__main__':
    sc = SiteCrawler('178.250.245.70', '3306', 'admin',
                     'arkpa55', 'new_ark', 'http://lenta.ru')
    sc.create_table()
    while len(sc._all_urls) <= 100000:
        sc.get_done_urls_from_db()
        sc.parsing_site()
        sc.write_to_db()

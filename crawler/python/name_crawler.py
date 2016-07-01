import requests
import re
import pymysql
from bs4 import BeautifulSoup
from collections import namedtuple


class NameCrawler(object):
    def __init__(self, user, password, db):
        self._sites = {}
        self._persons = {}
        self._pages = []
        self._names = {}
        self._config = {'user': user,
                        'password': password,
                        'database': db,
                        'charset': 'utf8'}

    def _get_sites(self):
        cnx = pymysql.connect(**self._config)
        cur = cnx.cursor()

        cur.execute("SELECT * FROM coriander_sites;")
        for row in cur:
            self._sites[row[1]] = row[0]

        Page = namedtuple('Page', ['page_id', 'url', 'site_id'])

        for site_id in self._sites.values():
            cur.execute("SELECT id, url, site_id \
                         FROM coriander_pages \
                         WHERE site_id='" + str(site_id) + "';")
            for row in cur:
                page = Page(*row)
                self._pages.append(page)

        cur.close()
        cnx.close()

    def _get_persons(self):
        cnx = pymysql.connect(**self._config)
        cur = cnx.cursor()

        cur.execute("SELECT * FROM coriander_persons;")
        for row in cur:
            self._persons[row[1]] = row[0]

        for person, person_id in self._persons.items():
            self._names[person] = []
            cur.execute("SELECT name \
                         FROM coriander_keywords \
                         WHERE person_id='" + str(person_id) + "';")
            for row in cur:
                self._names[person].append(row[0])

        cur.close()
        cnx.close()

    def _get_visibles_from_page(self, page):
        try:
            resp = requests.get(page.url)
            soup = BeautifulSoup(resp.content, 'lxml')

            # --------- plagiat --------- #
            texts = soup.findAll(text=True)

            def visible(element):
                if element.parent.name in ['style', 'script',
                                           '[document]', 'head', 'title']:
                    return False
                elif re.match('<!--.*-->', str(element)):
                    return False
                return True

            visible_texts = filter(visible, texts)
            self._texts_by_page[page.url] = visible_texts
            # ----- end of plagiat ------ #
        except Exception:
            return 0

    def count_persons(self):
        self._get_sites()
        self._get_persons()

        self._texts_by_page = {}
        page_num = 0
        for page in self._pages:
            self._get_visibles_from_page(page)
            page_num += 1
            if page_num % 100 == 0:
                print(page_num, end=' ')

        self._count = {}
        for pers in self._persons.keys():
            self._count[pers] = {}
        for page, texts in self._texts_by_page.items():
            for pers in self._count.keys():
                self._count[pers][page] = 0
            for text in texts:
                for person in self._persons.keys():
                    for word in self._names[person]:
                        match = re.findall(word, text, flags=re.IGNORECASE)
                        self._count[person][page] += len(match)

    def write_to_db(self):
        cnx = pymysql.connect(**self._config, autocommit=True)
        cur = cnx.cursor()
        page_num = 0
        for page in self._pages:
            page_num += 1
            if page_num % 100 == 0:
                print(page_num, end=' ')
            for pers, id in self._persons.items():
                select_test = False
                sql_test = "SELECT * \
                            FROM coriander_personpagerank \
                            WHERE (person_id='" + str(id) + "') \
                            AND (page_id='" + str(page.page_id) + "');"
                cur.execute(sql_test)
                for row in cur:
                    select_test = True
                if select_test:
                    sql_update = "UPDATE coriander_personpagerank \
                                  SET \
                                  rank='" + str(self._count[pers][page.url]) + "' \
                                  WHERE (person_id='" + str(id) + "') \
                                  AND (page_id='" + str(page.page_id) + "');"
                    cur.execute(sql_update)
                else:
                    sql = "INSERT \
                           INTO coriander_personpagerank(rank, page_id, \
                                                         person_id, site_id) \
                           VALUES \
                           (" + str(self._count[pers][page.url]) + ", " \
                              + str(page.page_id) + ", " + str(id) + ", " \
                              + str(page.site_id) + ");"
                    cur.execute(sql)
        cur.close()
        cnx.close()

if __name__ == '__main__':
    crawler = NameCrawler('root', 'r00tpa551', 'ark')
    crawler.count_persons()
    crawler.write_to_bd()

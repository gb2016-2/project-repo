import requests
import re
import pymysql
from bs4 import BeautifulSoup
from collections import namedtuple


class NameCrawler(object):
    def __init__(self, user, db):
        self._sites = {}
        self._persons = []
        self._pages = []
        self._config = {'user': user,
                        'database': db,
                        'charset': 'utf8'}

    def add_site(self, site):
        if site not in self._sites:
            cnx = pymysql.connect(**self._config)
            cur = cnx.cursor()

            cur.execute("SELECT id FROM sites WHERE name='" + site + "';")
            for row in cur:
                site_id = row[0]
                if site_id:
                    self._sites[site] = site_id

            cur.close()
            cnx.close()

    def add_person(self, person):
        self._persons.append(person)

    def get_pages(self):
        Page = namedtuple('Page', ['page_id', 'url', 'site_id'])

        cnx = pymysql.connect(**self._config)
        cur = cnx.cursor()

        for site_id in self._sites.values():
            cur.execute("SELECT * \
                         FROM pages \
                         WHERE site_id='" + str(site_id) + "';")
            for row in cur:
                page = Page(*row[:3])
                self._pages.append(page)

        cur.close()
        cnx.close()

    def count_persons(self):
        texts_by_page = {}
        for page in self._pages:
            resp = requests.get(page.url)
            soup = BeautifulSoup(resp.content, 'lxml')
            texts = soup.findAll(text=True)

            def visible(element):
                if element.parent.name in ['style', 'script',
                                           '[document]', 'head', 'title']:
                    return False
                elif re.match('<!--.*-->', str(element)):
                    return False
                return True

            visible_texts = filter(visible, texts)
            texts_by_page[page.url] = visible_texts

        self._count = {}
        for pers in self._persons:
            self._count[pers] = {}
        for page, texts in texts_by_page.items():
            for pers in self._count.keys():
                self._count[pers][page] = 0
            for text in texts:
                for person in self._count.keys():
                    match = re.findall(person, text, flags=re.IGNORECASE)
                    self._count[person][page] += len(match)

    def print_results(self):
        for pers, pages in self._count.items():
            print(pers)
            res = 0
            for page, num in pages.items():
                print('\t', page, num)
                res += num
            print('Total: {}\n'.format(res))

    def write_to_bd(self):
        cnx = pymysql.connect(**self._config, autocommit=True)
        cur = cnx.cursor()
        for page in self._pages:
            for pers in self._persons:
                sql = "INSERT \
                       INTO person_page_rank(person_id, page_id, rank) \
                       VALUES \
                       (" + str(1) + ", " + str(page.page_id) + ", " \
                          + str(self._count[pers][page.url]) + ");"
                cur.execute(sql)
        cur.close()
        cnx.close()

if __name__ == '__main__':
    putin = 'путин'
    zhir = 'жириновск'

    crawler = NameCrawler('bla-user', 'tmp')
    crawler.add_site('lenta.ru')
    crawler.get_pages()
    print(crawler._sites)
    print(crawler._pages)

    crawler.add_person(putin)
    crawler.add_person(zhir)
    crawler.count_persons()
    crawler.print_results()
    crawler.write_to_bd()

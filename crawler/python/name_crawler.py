import requests
import re
import pymysql
from bs4 import BeautifulSoup
from collections import namedtuple


class NameCrawler(object):
    def __init__(self, user, db):
        self._sites = {}
        self._persons = {}
        self._pages = []
        self._names = {}
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
        if person not in self._persons:
            cnx = pymysql.connect(**self._config)
            cur = cnx.cursor()

            cur.execute("SELECT id FROM persons WHERE name='" + person + "';")
            for row in cur:
                person_id = row[0]
                if person_id:
                    self._persons[person] = person_id

            cur.close()
            cnx.close()

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

    def get_names(self):
        cnx = pymysql.connect(**self._config)
        cur = cnx.cursor()

        for person, person_id in self._persons.items():
            self._names[person] = []
            cur.execute("SELECT name \
                         FROM keywords \
                         WHERE person_id='" + str(person_id) + "';")
            for row in cur:
                self._names[person].append(row[0])

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
        for pers in self._persons.keys():
            self._count[pers] = {}
        for page, texts in texts_by_page.items():
            for pers in self._count.keys():
                self._count[pers][page] = 0
            for text in texts:
                for person in self._persons.keys():
                    for word in self._names[person]:
                        match = re.findall(word, text, flags=re.IGNORECASE)
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
            for pers, id in self._persons.items():
                select_test = False
                sql_test = "SELECT * \
                            FROM person_page_rank \
                            WHERE (person_id='" + str(id) + "') \
                            AND (page_id='" + str(page.page_id) + "');"
                cur.execute(sql_test)
                for row in cur:
                    select_test = True
                if select_test:
                    sql_update = "UPDATE person_page_rank \
                                  SET \
                                  rank='" + str(self._count[pers][page.url]) + "' \
                                  WHERE (person_id='" + str(id) + "') \
                                  AND (page_id='" + str(page.page_id) + "');"
                    cur.execute(sql_update)
                else:
                    sql = "INSERT \
                           INTO person_page_rank(person_id, page_id, rank) \
                           VALUES \
                           (" + str(id) + ", " + str(page.page_id) + ", " \
                              + str(self._count[pers][page.url]) + ");"
                    cur.execute(sql)
        cur.close()
        cnx.close()

if __name__ == '__main__':
    pass

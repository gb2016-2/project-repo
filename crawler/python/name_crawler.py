import requests
import re
import pymysql
from bs4 import BeautifulSoup
from collections import namedtuple
from dateutil import parser


class NameCrawler(object):
    def __init__(self, user, password, db):
        self._sites = {}
        self._persons = {}
        self._pages = []
        self._names = {}
        self._count = {}
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

        Page = namedtuple('Page', ['page_id', 'url', 'site_id', 'page_date'])

        for site_id in self._sites.values():
            cur.execute("SELECT id, url, site_id, found_date_time \
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
        for pers in self._persons.keys():
            self._count[pers] = {}

    def _get_visibles_from_page(self, page_url, page_date):
        try:
            resp = requests.get(page_url)
            soup = BeautifulSoup(resp.content, 'lxml')

            def get_date(str_date):
                dt = parser.parse(str_date)
                result = str(dt.year) + str("{:02}".format(dt.month)) \
                                      + str("{:02}".format(dt.day))
                return result

            try:
                new_date = get_date(resp.headers['Last-Modified'])
            except Exception:
                new_date = page_date
            self._page_dates[page_url] = new_date

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
            # ----- end of plagiat ------ #

            return visible_texts

        except Exception:
            return []

    def count_persons(self):
        self._get_sites()
        self._get_persons()

        self._page_dates = {}
        page_num = len(self._pages)

        cnx = pymysql.connect(**self._config, autocommit=True)
        cur = cnx.cursor()

        for page in self._pages:

            # sql_test_page

            print('\r\tPages left:', page_num, end='          ')
            visible_texts = self._get_visibles_from_page(page.url,
                                                         page.page_date)
            # for page, texts in self._texts_by_page.items():
            for person in self._count.keys():
                self._count[person][page.url] = 0
            for text in visible_texts:
                for person in self._persons.keys():
                    for word in self._names[person]:
                        match = re.findall(word, text, flags=re.IGNORECASE)
                        self._count[person][page.url] += len(match)

            sql_upd_page = "UPDATE coriander_pages \
                            SET found_date_time='" \
                                        + str(self._page_dates[page.url]) + "' \
                            WHERE id='" + str(page.page_id) + "';"
            cur.execute(sql_upd_page)

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

            page_num -= 1

        print('\n')
        cur.close()
        cnx.close()

    """
    def write_to_db(self):
        cnx = pymysql.connect(**self._config, autocommit=True)
        cur = cnx.cursor()

        page_num = len(self._pages)
        for page in self._pages:
            page_num -= 1
            print('\rPages left:', page_num, end='          ')

            sql_upd_page = "UPDATE coriander_pages \
                            SET found_date_time='" \
                                        + str(self._page_dates[page.url]) + "' \
                            WHERE id='" + str(page.page_id) + "';"
            cur.execute(sql_upd_page)

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
    """


if __name__ == '__main__':
    crawler = NameCrawler('root', 'r00tpa551', 'ark')
    crawler.count_persons()
    crawler.write_to_bd()

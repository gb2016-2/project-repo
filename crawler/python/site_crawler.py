import requests
import pymysql
from bs4 import BeautifulSoup
import re


class SiteCrawler(object):
    def __init__(self, user, password, db, site):
        self._topics = {}
        self._all_urls = set()
        self._site = site
        self._config = {'user': user,
                        'password': password,
                        'database': db,
                        'charset': 'utf8'}

    def _get_urls(self, page):
        try:
            resp = requests.get(page)
        except Exception:
            return set()

        soup = BeautifulSoup(resp.content, 'lxml')
        urls = soup.findAll('a')

        pat = '//\S*?\.((ru)|(com)).*'
        lenta = []
        for url in urls:
            href = url.get('href')
            try:
                match = re.search(pat, href).group()
                if '.lenta.ru' in match or '//lenta.ru' in match:
                    lenta.append(match[match.index('.ru')+3:].
                                 rstrip('/').lstrip('/'))
            except AttributeError:
                if href is None or href is '/':
                    continue
                lenta.append(href.rstrip('/').lstrip('/'))
            except TypeError:
                if href is None or href is '/':
                    continue
                lenta.append(href.rstrip('/').lstrip('/'))
        return set(lenta)

    def _get_pages_by_topics(self, depth):
        self._sitemap[depth] = set()
        for high_url in self._sitemap[depth-1]:
            whole_url = self._site + '/' + high_url
            self._sitemap[depth] |= (self._get_urls(whole_url) - self._all_urls)
        for url in self._sitemap[depth]:
            split_url = url.split('/')
            topic = self._site + '/' + split_url[0]
            whole_url = self._site + '/' + url
            if topic in self._topics:
                self._topics[topic] |= set([whole_url])
        self._all_urls |= self._sitemap[depth]
        print(len(self._all_urls))

    def get_sitemap_with_depth(self, depth):
        self._sitemap = {}
        self._sitemap[0] = self._get_urls(self._site)
        for url in self._sitemap[0]:
            split_url = url.split('/')
            topic = self._site + '/' + split_url[0]
            whole_url = self._site + '/' + url
            if topic not in self._topics:
                self._topics[topic] = set()
            self._topics[topic] |= set([whole_url])
            self._all_urls |= set([whole_url])

        for i in range(depth):
            self._get_pages_by_topics(i+1)

    def write_to_db(self):
        cnx = pymysql.connect(**self._config, autocommit=True)
        cur = cnx.cursor()

        cur.execute("SELECT id FROM coriander_sites \
                     WHERE name='" + self._site + "';")
        site_id = False
        for row in cur:
            site_id = row[0]
        if site_id is False:
            cur.execute("INSERT INTO coriander_sites(name) \
                         VALUES('" + str(self.site) + "');")
            cur.execute("SELECT id FROM coriander_sites \
                         WHERE name='" + self.site + "';")
            for row in cur:
                site_id = row[0]

        for key in self._topics.keys():
            for url in self._topics[key]:
                select_test = False
                sql_test = "SELECT * \
                            FROM coriander_pages \
                            WHERE (url='" + url + "');"
                cur.execute(sql_test)
                for row in cur:
                    select_test = True
                if select_test is False:
                    sql = "INSERT \
                           INTO coriander_pages(url, found_date_time, \
                                                last_scan_date, site_id) \
                           VALUES \
                           ('" + str(url) + "', '20160628', '20160628', '" \
                            + str(site_id) + "');"
                    cur.execute(sql)
        cur.close()
        cnx.close()


if __name__ == '__main__':
    sc = SiteCrawler('root', 'r00tpa551', 'ark', 'http://lenta.ru')
    sc.get_sitemap_with_depth(5)
    sc.write_to_db()

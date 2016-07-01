import requests
import pymysql
from bs4 import BeautifulSoup
import re


class SiteCrawler(object):
    def __init__(self, user, password, db, site):
        self.topics = {}
        self.all_urls = set()
        self.site = site
        self._config = {'user': user,
			'password': password,
                        'database': db,
                        'charset': 'utf8'}

    def get_urls(self, page):
        try:
            resp = requests.get(page)
        except Exception:
            return set()

        soup = BeautifulSoup(resp.content, 'html.parser')
        urls = soup.findAll('a')

        pat = '//\S*?\.((ru)|(com)).*'
        lenta = []
        for url in urls:
            href = url.get('href')
            try:
                # if '@' in href or ':' in href or '#' in href:
                #     continue
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

    def get_pages_by_topics(self, depth):
        self.sitemap[depth] = set()
        for high_url in self.sitemap[depth-1]:
            whole_url = self.site + '/' + high_url
            self.sitemap[depth] |= (self.get_urls(whole_url) - self.all_urls)
        for url in self.sitemap[depth]:
            split_url = url.split('/')
            topic = self.site + '/' + split_url[0]
            whole_url = self.site + '/' + url
            if topic in self.topics:
                self.topics[topic] |= set([whole_url])
        self.all_urls |= self.sitemap[depth]
        print(len(self.all_urls))

    def get_sitemap(self, depth):
        self.sitemap = {}
        self.sitemap[0] = self.get_urls(self.site)
        for url in self.sitemap[0]:
            split_url = url.split('/')
            topic = self.site + '/' + split_url[0]
            whole_url = self.site + '/' + url
            if topic not in self.topics:
                self.topics[topic] = set()
            self.topics[topic] |= set([whole_url])
            self.all_urls |= set([whole_url])

        for i in range(depth):
            self.get_pages_by_topics(i+1)

        return self.topics

    def write_to_db(self):
        cnx = pymysql.connect(**self._config, autocommit=True)
        cur = cnx.cursor()

        cur.execute("SELECT id FROM coriander_sites WHERE name='" + self.site + "';")
        site_id = False
        for row in cur:
            site_id = row[0]
        if site_id is False:
            cur.execute("INSERT INTO coriander_sites(name) \
                         VALUES('" + str(self.site) + "');")
            cur.execute("SELECT id FROM coriander_sites WHERE name='" + self.site + "';")
            for row in cur:
                site_id = row[0]

        for key in self.topics.keys():
            for url in self.topics[key]:
                select_test = False
                sql_test = "SELECT * \
                            FROM coriander_pages \
                            WHERE (url='" + url + "');"
                cur.execute(sql_test)
                for row in cur:
                    select_test = True
                if select_test is False:
                    sql = "INSERT \
                           INTO coriander_pages(url, site_id, \
                                      found_date_time, last_scan_date) \
                           VALUES \
                           ('" + str(url) + "', '" + str(site_id) + "', " \
                              + "'20160628', '20160628');"
                    cur.execute(sql)
        cur.close()
        cnx.close()


if __name__ == '__main__':
    sc = SiteCrawler('root', 'r00tpa551', 'ark', 'http://lenta.ru')
    sc.get_sitemap(5)
    sc.write_to_db()

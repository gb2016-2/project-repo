import pymysql
from collections import namedtuple


class UserInterface(object):
    def __init__(self, user, db):
        self.sites = {}
        self.persons = []
        self._config = {'user': user,
                        'database': db,
                        'charset': 'utf8'}

    def show_persons(self):
        cnx = pymysql.connect(**self._config)
        cur = cnx.cursor()

        sql_person = "SELECT * FROM persons;"
        cur.execute(sql_person)
        for row in cur:
            print(row)

        cur.close()
        cnx.close()

    def show_sites(self):
        cnx = pymysql.connect(**self._config)
        cur = cnx.cursor()

        sql_site = "SELECT * FROM sites;"
        cur.execute(sql_site)
        for row in cur:
            print(row)

        cur.close()
        cnx.close()

    def add_person(self, person):
        for pers in self.persons:
            if pers.name == person:
                print(person, 'is already here')
                return 0

        Person = namedtuple('Person', ['person_id', 'name', 'keywords'])

        cnx = pymysql.connect(**self._config)
        cur = cnx.cursor()
        sql_person = "SELECT id FROM persons WHERE name='" + person + "';"
        cur.execute(sql_person)
        sql_person_test = False
        for row in cur:
            person_id = row[0]
            sql_person_test = True

        if sql_person_test is False:
            print(person, 'is not in base')
            cur.close()
            cnx.close()
            return 0
        else:
            sql_keywords = "SELECT name FROM keywords \
                           WHERE person_id='" + str(person_id) + "';"
            cur.execute(sql_keywords)
            keywords = []
            for row in cur:
                keywords.append(row[0])

            self.persons.append(Person(person_id, person, keywords))

            cur.close()
            cnx.close()

    def add_site(self, site):
        if site not in self.sites.keys():
            cnx = pymysql.connect(**self._config)
            cur = cnx.cursor()

            sql_site = "SELECT id FROM sites WHERE name='" + site + "';"
            cur.execute(sql_site)
            sql_site_test = False
            for row in cur:
                self.sites[site] = row[0]
                sql_site_test = True

            if sql_site_test is False:
                print(site, 'is not in base')
                return 0

            cur.close()
            cnx.close()
        else:
            print(site, 'is already here')

    def print_results(self):
        pass


if __name__ == "__main__":
    # tests
    pass

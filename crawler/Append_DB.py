import pymysql
import pymysql.cursors
import threading


def connect(c_host, c_port, c_user, c_pass, c_db):
    """ Connect to MySQL database """
    db = pymysql.connect(host = c_host,
                             port = int(c_port),
                             user = c_user,
                             password = c_pass,
                             db = c_db)
    
    
    
    with db.cursor() as cursor:
        cursor.execute("""CREATE TABLE
                        IF NOT EXISTS Pages(ID INTEGER,
                                            Url VARCHAR(2048),
                                            SiteID INTEGER
                                            PRIMARY KEY AUTO_INCREMENT,
                                            FoundDateTime DATE,
                                            LastScanDate DATE)""")
        data = cursor.fetchone()
        print("Database version : {0} ".format(data))
        print('TABLE Pages CREATED')


    
    return db

class Write_DB():
    def __init__(self, DataList):
        self.DataList = DataList
        
    def write_db(self):
        conect = connect('178.250.245.70', \
                         '3306', \
                         'admin' , \
                         'arkpa55', \
                         'new_ark')
        cursor = conect.cursor()
        end = len(self.DataList)
        count = 0

        def extr(ID, Url, FoundDateTime):
            nonlocal count
            if cursor.execute("""SELECT Url FROM Pages
                                    WHERE Url LIKE "{0}"
                                    LIMIT 10000""".format(Url)) == 0:
                cursor.execute("""INSERT INTO Pages(ID,
                                                    Url,
                                                    FoundDateTime)
                                                    VALUES
                                                    ("{0}","{1}","{2}")""" \
                               .format(ID, Url, FoundDateTime,))
                count += 1
                if count%1000 == 0:
                    print(count, '/', str(len(self.DataList)))
            else:
                cursor.execute('UPDATE Pages \
                               SET FoundDateTime = "{0}" \
                               WHERE Url = "{1}"'.format(FoundDateTime, Url))
                count += 1
                if count%1000 == 0:
                    print(count, '/', str(len(self.DataList)))
        count2 = 0
        for ID, Url, FoundDateTime in self.DataList:
            count2 += 1
            extr(ID, Url, FoundDateTime)
            if count == 100000:
                break
            
        print("Data added to table")
        
        conect.commit()
        
        print('Commit')
        
        
        """
        for ID, Url, FoundDateTime in self.DataList:
            p = threading.Thread(target=extr, args=(ID, Url, FoundDateTime,))
            p.start()
            
        while 1:
            print('In Append_DB: ' + str(threading.activeCount()))
            if threading.activeCount() == 0:
                connect().close()
                break
            else: continue
        """
if __name__ == '__main__':
    print('Введите "IP, port, user, password, databasename"')
    x = [z.strip() for z in input().split(',')]
    connect(x[0],x[1],x[2],x[3],x[4])
    

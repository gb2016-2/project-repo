import pymysql
import pymysql.cursors
import threading


def connect():
    """ Connect to MySQL database """
    db = pymysql.connect(host='178.250.245.70',
                             port=int('3306'),
                             user='admin',
                             password='arkpa55',
                             db='new_ark',
                             cursorclass=pymysql.cursors.DictCursor)
    
    return db
    
    

    
    

class Write_DB():
    def __init__(self, DataList):
        self.DataList = DataList
        
    def write_db(self):
        
        cursor = connect().cursor()
        end = len(self.DataList)
        count = 0

        def extr(ID, Url, FoundDateTime):
            
            nonlocal count
            if cursor.execute("""SELECT Url FROM Pages WHERE Url LIKE "{0}" LIMIT 10000""".format(Url)) == 0:
                cursor.execute("""INSERT INTO Pages(ID,
                                                    Url,
                                                    FoundDateTime)
                                                    VALUES ("{0}","{1}","{2}")""".format(ID, Url, FoundDateTime,))
                count += 1
                if count%1000 == 0:
                    print(count, str(len(self.DataList)))
            else:
                cursor.execute('UPDATE Pages SET FoundDateTime = "{0}" WHERE Url = "{1}"'.format(FoundDateTime, Url))
                count += 1
                if count%1000 == 0:
                    print(count, str(len(self.DataList)))
         
        for ID, Url, FoundDateTime in self.DataList:
            if count == 15000:
                break
            extr(ID, Url, FoundDateTime)
        
        print("Data added to table")
        cursor().close()
        
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

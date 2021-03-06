#-*-coding:utf-8-*-
import sys
reload(sys)
sys.setdefaultencoding('utf-8')
import MySQLdb
import ConfigParser

class Profile_Db(object):
    def __init__(self):
        self.host = None
        self.user = None
        self.passwd = None
        self.port = None
        self.db = None
        self.charset = None
        self.use_unicode = None
        self.table = 'profile'
        self.initParams()
        self.conn = None
        self.cur = None
        self.initDb()

    #从配置文件中初始化参数变量
    def initParams(self):
        cf = ConfigParser.ConfigParser()
        cf.read('C:\Users\Administrator\Desktop\config.ini')
        self.host = cf.get('db', 'host')
        self.port = int(cf.get('db', 'port'))
        self.user = cf.get('db', 'user')
        self.passwd = cf.get('db', 'passwd')
        self.db = cf.get('db', 'db')
        self.charset = cf.get('db', 'charset')
        self.use_unicode = cf.get('db', 'use_unicode')

    def initDb(self):
        try:
            self.conn = MySQLdb.connect(host=self.host, port=self.port, user=self.user, passwd=self.passwd, db=self.db, charset=self.charset, use_unicode=self.use_unicode)
            self.cursor = self.conn.cursor()
        except MySQLdb.Error, e:
            print 'Mysql Error %d: %s' % (e.args[0], e.args[1])
            print 'Failed to connect to database! Please check your config file and confirm your database is open'
            sys.exit(-1)
        print 'Success connect database'

    #判断
    def findExists(self, weiboid):
        clause = 'select * from %s where weiboid = %s;' % (self.table, weiboid)
        count = self.cursor.execute(clause)
        return count

    #将给定的Profile对象插入到数据库中，注意，不能增加原先已经含有的记录
    def insertIntoDB(self, obj):
        if self.findExists(obj.weiboid) == 0:
            self.cursor.execute('replace into profile(weiboid, nickname, is_education) values(%s, %s, %s)', \
                                (obj.weiboid, obj.nickname, obj.is_education))
        self.conn.commit()

    def updateDB(self, weiboid):
        pass

    def describeRows(self, weiboid=None):
        if weiboid:
            clause = 'select * from %s where weiboid = %s;' % (self.table, weiboid)
        else:
            clause = 'select * from %s;' % self.table;

        count = self.cursor.execute(clause)
        print 'There has %d rows record' % count
        return count

    def describeProfile(self, weiboid=None):
        count = self.describeRows(weiboid=weiboid)
        if count != 0:
            results = self.cursor.fetchall()
            return results
        else:
            return None

    def closeResource(self):
        if self.cur:
            self.cur.close()
        if self.conn:
            self.conn.close()


def main():
    p_d = Profile_Db()
    p_d.describeRows()
    p_d.describeProfile()
    print p_d.findExists('1007343***')
    p_d.closeResource()



if __name__ == '__main__':
    main()
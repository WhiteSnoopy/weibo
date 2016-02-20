#-*-coding:utf-8-*-
import sys
reload(sys)
import ConfigParser
sys.setdefaultencoding('utf-8')
import MySQLdb

class Education_db(object):
    def __init__(self):
        self.host = None
        self.port = None
        self.user = None
        self.passwd = None
        self.db = None
        self.table = 'education'
        self.charset = None
        self.initparams()
        self.conn = None
        self.cursor = None
        self.connectDB()


    #从配置文件中初始化参数变量
    def initparams(self):
        config = ConfigParser.ConfigParser()
        #从桌面读取配置文件
        config.read("C:\Users\Administrator\Desktop\config.ini")
        self.host = config.get("db", "host")
        self.port =int(config.get("db", "port"))
        self.user = config.get("db", "user")
        self.passwd = config.get("db", "passwd")
        self.db = config.get("db", "db")
        self.charset = config.get("db", "charset")

    def connectDB(self):
        try:
            self.conn = MySQLdb.connect(host=self.host, port=self.port, user=self.user, passwd=self.passwd, db=self.db, charset=self.charset)
            self.cursor = self.conn.cursor()
        except MySQLdb.Error, e:
            print 'Mysql error %d: %s' % (e.args[0], e.args[1])
            print 'Failed to connect to database'
            sys.exit(-1)
        print 'Succeed connect to the database'

    #判断是否有记录存在
    def isExists(self, weiboid):
        sql = 'select * from %s where weiboid = %s;' % (self.table, weiboid)
        count = self.cursor.execute(sql)
        return count

    #将education对象插入到数据库中去
    def insertintoDB(self, obj):
        if self.isExists(obj.weiboid)==0:
            try:
                self.cursor.execute('replace into education(wmd5, weiboid, school, enrolltime) values(%s ,%s, %s, %s )',(obj.wmd5, obj.weiboid, obj.school, obj.enrolltime))
                self.conn.commit()
            except Exception, e:
                print 'Mysql Error %d: %s' % (e.args[0], e.args[1])

    def describeRows(self, weiboid=None):
        if weiboid:
            sql = 'select * from %s where weiboid = %s;' % (self.table, weiboid)
        else:
            sql = 'select * from %s;' % self.table
        count = self.cursor.execute(sql)
        print 'There has %d records' % count
        return count

    def describeeducation(self, weiboid=None):
        count = self.describeRows(weiboid=weiboid)
        if count!=0:
            results = self.cursor.fetchall()
            for r in results:
                print r[0], r[1]

    def closeconnect(self):
        if self.cursor:
            self.cursor.close()
        if self.conn:
            self.conn.close()

def main():
    ed = Education_db()
    ed.describeRows()
    ed.describeeducation()
    ed.closeconnect()

if __name__ == '__main__':
	main()
#-*-coding=utf-8-*-
import sys
reload(sys)
sys.setdefaultencoding('utf-8')
from md5util import md5
class Education(object):
    def __init__(self, weiboid=None, school=None, enrolltime=None):
        self.weiboid = weiboid
        self.school = school
        self.enrolltime = enrolltime
        self.wmd5 = None

    def setWmd5(self):
        print 'come in'
        self.wmd5 = md5(str(self.weiboid)+str(self.school)+str(self.enrolltime))

    def __str__(self):
        self.wmd5 = self.wmd5 if self.wmd5 else '未知'
        self.weiboid = self.weiboid if self.weiboid else '未知'
        self.school = self.school if self.school else '未知'
        self.enrolltime = self.enrolltime if self.enrolltime else '未知'
        return '微博号：' + self.weiboid + '\tmd5值：' + self.wmd5 + '\t学校名称：' + self.school + '\t入学时间：' + self.enrolltime

def main():
    e = Education()
    e.weiboid = '1002061768409523'
    e.school = '南京大学'
    e.enrolltime = '2010'
    e.setWmd5()
    print e

if __name__=='__main__':
    main()




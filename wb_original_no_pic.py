#-*-coding:utf-8-*-
import sys
reload(sys)
sys.setdefaultencoding('utf-8')
from md5util import md5
#微博原创无图

class Wb_Original_No_Pic(object):
    def __init__(self, weiboid=None, ftime=None, content=None, upvotes=None, forwards=None, reviews=None):
        #微博md5值
        self.wmd5 = None
        #微博ID
        self.weiboid = weiboid
        #微博的发布时间
        self.ftime = ftime
        #微博的内容
        self.content = content
        #赞数目
        self.upvotes = upvotes
        #转发的数目
        self.forwards = forwards
        #评论数
        self.reviews = reviews

    def setWmd5(self):
        self.wmd5 = md5(str(self.weiboid)+str(self.content)+str(self.ftime)+str(self.upvotes)+str(self.forwards)+str(self.reviews))


    def __str__(self):
        self.wmd5 = self.wmd5 if self.wmd5 is not None else '未知'
        self.weiboid = self.weiboid if self.weiboid is not None else '未知'
        self.ftime = self.ftime if self.ftime is not None else '未知'
        self.content = self.content if self.content is not None else '未知'
        self.upvotes = self.upvotes if self.upvotes is not None else '未知'
        self.forwards = self.forwards if self.forwards is not None else '未知'
        self.reviews = self.reviews if self.reviews is not None else '未知'
        return '微博号：' + self.weiboid + '\tmd5值：' + self.wmd5 + '\t时间：' + self.ftime + '\n\t微博内容：' + self.content + '\n\t赞：' + str(self.upvotes) + '\t评论：' + str(self.reviews) + '\t转发数：' + str(self.forwards)


##########################################测试
def main():
    wp = Wb_Original_No_Pic()
    wp.weiboid = '1231234234'
    wp.content = '新年快乐'
    wp.ftime = '2016-01-12'
    wp.setWmd5()
    print wp

if __name__=='__main__':
    main()



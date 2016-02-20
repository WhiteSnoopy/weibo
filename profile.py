#-*-coding:utf-8-*-
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

class Profile(object):
    def __init__(self, weiboid=None, nickname=None):
        self.weiboid = weiboid
        self.nickname = nickname
        #是否有教育经历 默认为-1 没有
        self.is_education = -1

    def __str__(self):
        self.weiboid = self.weiboid if self.weiboid is not None else '未知'
        self.nickname = self.nickname if self.nickname is not None else '未知'
        if self.is_education ==1:
            str_is_education = '有'
        else:
            str_is_education = '没有'
        return '微博号：' + self.weiboid + '\t昵称：' + self.nickname+ '\t是否下载过教育信息：' + str_is_education



def main():
    p = Profile()
    p.weiboid = '234233526'
    p.nickname = 'chan'
    print p

if __name__=='__main__':
    main()
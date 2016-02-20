#-*-coding=utf-8-*-
import sys
reload(sys)
sys.setdefaultencoding('utf-8')
#detailprofile.py
import urllib2


class DetailProfile(object):
    def __init__(self, weiboid=None, gender=-1, description=None, address=None, birthday=None, blog=None, relation=None, sexuality=-1, bloodtype=None, fashion=None):
        self.weiboid = weiboid
        self.gender = gender
        self.description = description
        self.address = address
        self.birthday = birthday
        self.blog = blog
        self.relation = relation
        self.sexuality = sexuality
        self.bloodtype = bloodtype
        self.fashion = fashion

    #overwrite __str__
    def __str__(self):
        self.weiboid = self.weiboid if self.weiboid else '未知'
        self.gender = self.gender if self.gender else '未知'
        self.description = self.description if self.description else '未知'
        self.address = self.address if self.address else '未知'
        self.birthday = self.birthday if self.birthday else '未知'
        self.blog = self.blog if self.blog else '未知'
        self.relation = self.relation if self.relation else '未知'
        self.sexuality = self.sexuality if self.sexuality else '未知'
        self.bloodtype = self.bloodtype if self.bloodtype else '未知'
        self.fashion = self.fashion if self.fashion else '未知'
        if self.gender == -1:
            strgender = '未知'
        elif self.gender == 2:
            strgender = '女'
        elif self.gender == 1:
            strgender = '男'

        if self.sexuality == -1:
            strsexuality = '未知'
        elif self.sexuality == 0:
            strsexuality = u'女'
        else:
            strsexuality = u'男'

        return '\n\t微博号：' + self.weiboid + '\t性别：' + strgender + '\t个人简介：' + self.description+'\n\t地址：' + self.address + '\t生日：' + self.birthday +'\t博客：' + self.blog + '\n\t感情状况：' + self.relation + '\t性取向：' + strsexuality +'\t血型：' + self.bloodtype + '\t达人：' + self.fashion

def main():
    profile = DetailProfile()
    profile.weiboid = '18751979168'
    profile.gender = '男'
    print profile

if __name__ == '__main__':
    main()

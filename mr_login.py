# -*- coding:utf-8 -*-
from urllib import request,parse
import urllib
import http.cookiejar
from bs4 import BeautifulSoup
import re
class mr_login(object):
    
    viewstate=''
    img_code=''
    loginAndCheckUrl="http://jw.hzau.edu.cn/default2.aspx"
    codeURL='http://jw.hzau.edu.cn/CheckCode.aspx'
    
    def __init__(self):
        self.cj=http.cookiejar.LWPCookieJar()
        self.cookie_support=urllib.request.HTTPCookieProcessor(self.cj)
        self.opener=urllib.request.build_opener(self.cookie_support,urllib.request.HTTPHandler)
        urllib.request.install_opener(self.opener)
    
    def preLogin(self):
        f=urllib.request.urlopen(self.loginAndCheckUrl,timeout=3)
        html=f.read().decode('gbk')
        soup=BeautifulSoup(html,'html.parser')
        soup=soup.find_all(attrs={'name':'__VIEWSTATE'})[0]
        self.viewstate=soup.get('value')
        f=urllib.request.urlopen(self.codeURL,timeout=3)
        path='D:\\aaaaa\\code.gif'
        fl=open(path,'wb')
        fl.write(f.read())
        fl.close()
        self.img_code=input("please input code: ")
    def login(self):
        headers={
            'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
            'Accept-Encoding':'gzip, deflate',
            'Accept-Language':'zh-CN,zh;q=0.8',
            'Cache-Control':'no-cache',
            'Connection':'keep-alive',
            'Content-Type':'application/x-www-form-urlencoded',
            'Host':'jw.hzau.edu.cn',
            'Origin':'http://jw.hzau.edu.cn',
            'Pragma':'no-cache',
            'Referer':'http://jw.hzau.edu.cn/default2.aspx',
            'Upgrade-Insecure-Requests':1,
            'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/47.0.2526.106 Safari/537.36,'
        }
        form={
            '__VIEWSTATE':self.viewstate,
            'txtUserName':'2013307201006',
            'TextBox2':'qq520.1314',
            'txtSecretCode':self.img_code,
            'RadioButtonList1':'学生',
            'Button1':'',
            'lbLanguage':'',
            'hidPdrs':'',
            'hidsc':'',
        }
        post_data=urllib.parse.urlencode(form).encode(encoding='utf-8')
        req=urllib.request.Request(self.loginAndCheckUrl,post_data,headers)
        html=urllib.request.urlopen(req).read().decode('gbk')
        result=re.findall(r'程书意同学', html)
        if not result:
            return False
        else:
            self.cj.save('D:\\workspace\\python\\hzau\\course\\config\\cookie.conf', ignore_discard=True, ignore_expires=True)
            return True
    def door(self):
        self.preLogin()
        return self.login()
# -*- coding:utf-8 -*-
from urllib import request,parse
import urllib
import http.cookiejar
from bs4 import BeautifulSoup
import re
from http.cookiejar import FileCookieJar
'''
login in hzau
step 1:open loginAndCheckUrl for getting viewstate and cookies
step 2:open codeURL for getting code image and get check code
step 3:generate form and headers before open loginAndCheckUrl for login
'''
class mr_login(object):
    viewstate=None
    img_code=None
    loginAndCheckUrl="http://jw.hzau.edu.cn/default2.aspx"
    codeURL='http://jw.hzau.edu.cn/CheckCode.aspx'
    
    #save cookies and code image
    cookieFile='D:\\workspace\\python\\hzau\\course\\config\\cookie.conf'
    codeImg='D:\\aaaaa\\code.gif'
    
    #username and password
    username=''
    password=''
    
    #init fileCookieJar and install_opener
    def __init__(self):
        self.cj=http.cookiejar.LWPCookieJar(self.cookieFile)
        self.cookie_support=urllib.request.HTTPCookieProcessor(self.cj)
        self.opener=urllib.request.build_opener(self.cookie_support,urllib.request.HTTPHandler)
        urllib.request.install_opener(self.opener)
    
    def getViewAndCode(self):
        while self.viewstate is None:
            try:
                html=urllib.request.urlopen(self.loginAndCheckUrl,timeout=3).read().decode('gbk')
                soup=BeautifulSoup(html,'html.parser')
                soup=soup.find_all(attrs={'name':'__VIEWSTATE'})[0]
                self.viewstate=soup.get('value')
            except:
                print('the login.aspx has not response')
                continue
        while self.img_code is None:
            fl=open(self.codeImg,'wb')
            try:
                fl.write(urllib.request.urlopen(self.codeURL,timeout=3).read())
            except:
                print('the code.aspx has not response')
                continue
            finally:
                fl.close()
            self.img_code=input("please input code: ")#must wait for fl.close()
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
            'txtUserName':self.username,
            'TextBox2':self.password,
            'txtSecretCode':self.img_code,
            'RadioButtonList1':'%D1%A7%C9%FA',
            'Button1':'',
            'lbLanguage':'',
            'hidPdrs':'',
            'hidsc':'',
        }
        post_data=urllib.parse.urlencode(form).encode(encoding='utf-8')
        req=urllib.request.Request(self.loginAndCheckUrl,post_data,headers)
        html=urllib.request.urlopen(req).read().decode('gbk')
        result=re.findall(r'返回首页', html)
        if not result:
            return False
        else:
            self.cj.save(ignore_discard=True, ignore_expires=True)
            return True
    #start here    return value:true or false
    def door(self):
        self.getViewAndCode()
        return self.login()

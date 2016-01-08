# -*- coding:utf-8 -*-
from urllib import request,parse
import urllib
import http.cookiejar
from bs4 import BeautifulSoup

cj=http.cookiejar.LWPCookieJar()
cookie_support=urllib.request.HTTPCookieProcessor(cj)
opener=urllib.request.build_opener(cookie_support,urllib.request.HTTPHandler)
urllib.request.install_opener(opener)
def login():
    loginURL="http://jw.hzau.edu.cn/default2.aspx"
    checkURL="http://jw.hzau.edu.cn/default2.aspx"
    codeURL='http://jw.hzau.edu.cn/CheckCode.aspx'
    user_agent="Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/47.0.2526.106 Safari/537.36"
    f=urllib.request.urlopen(loginURL)
    html=f.read().decode('gbk')
    soup=BeautifulSoup(html,'html.parser')
    soup=soup.find_all(attrs={'name':'__VIEWSTATE'})[0]
    viewstate=soup.get('value')
    f=urllib.request.urlopen(codeURL)
    path='D:\\aaaaa\\code.gif'
    fl=open(path,'wb')
    fl.write(f.read())
    fl.close()
    img_code=input("please input code: ")
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
            'User-Agent':user_agent,
        }
    form={
        '__VIEWSTATE':viewstate,
        'txtUserName':'2013307201006',
        'TextBox2':'qq520.1314',
        'txtSecretCode':img_code,
        'RadioButtonList1':'学生',
        'Button1':'',
        'lbLanguage':'',
        'hidPdrs':'',
        'hidsc':'',
    }
    post_data=urllib.parse.urlencode(form).encode(encoding='utf-8')
    req=urllib.request.Request(checkURL,post_data,headers)
    f=urllib.request.urlopen(req)
    #print(f.read().decode('gbk'))
def getView():
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
        'Referer':'http://jw.hzau.edu.cn/xs_main.aspx?xh=2013307201006',
        'Upgrade-Insecure-Requests':1,
        'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/47.0.2526.106 Safari/537.36'
    }
    xkURL='http://jw.hzau.edu.cn/xf_xsqxxxk.aspx?xh=2013307201006&xm=%B3%CC%CA%E9%D2%E2&gnmkdm=N121111'
    req=urllib.request.Request(xkURL,headers=headers)
    f=urllib.request.urlopen(req)
    html=f.read().decode('gbk')
    print(html)
    soup=BeautifulSoup(html,'html.parser')
    soup=soup.find_all(attrs={'name':'__VIEWSTATE'})[0]
    viewstate=soup.get('value')
    return viewstate
def choseClass():
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
        'Referer':'http://jw.hzau.edu.cn/xf_xsqxxxk.aspx?xh=2013307201006&xm=%B3%CC%CA%E9%D2%E2&gnmkdm=N121111',
        'Upgrade-Insecure-Requests':1,
       ' User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/47.0.2526.106 Safari/537.36'
    }
    reqURL='http://jw.hzau.edu.cn/xf_xsqxxxk.aspx?xh=2013307201006&xm=%B3%CC%CA%E9%D2%E2&gnmkdm=N121111',
    viewstate=getView()
    form={
        '__EVENTTARGET':'',
        '__EVENTARGUMENT':'',
        '__VIEWSTATE':viewstate,
        'ddl_kcxz':'',
        'ddl_ywyl':'有',
        'ddl_kcgs':'自然科学',#select sort
        'ddl_xqbs':1,
        'ddl_sksj':'',
        'TextBox1':'',
        'kcmcGrid:_ctl2:jcnr':'|||',
        'kcmcGrid:_ctl3:jcnr':'|||',
        'kcmcGrid:_ctl4:xk':'on',
        'kcmcGrid:_ctl4:jcnr':'|||',
        'kcmcGrid:_ctl5:xk':'on',
        'kcmcGrid:_ctl5:jcnr':'|||',
        'kcmcGrid:_ctl6:jcnr':'|||',
        'kcmcGrid:_ctl7:jcnr':'|||',
        'kcmcGrid:_ctl8:jcnr':'|||',
        'kcmcGrid:_ctl9:jcnr':'|||',
        'kcmcGrid:_ctl10:jcnr':'|||',
        'kcmcGrid:_ctl11:jcnr':'|||',
        'kcmcGrid:_ctl12:jcnr':'|||',
        'kcmcGrid:_ctl13:jcnr':'|||',
        'kcmcGrid:_ctl14:jcnr':'|||',
        'kcmcGrid:_ctl15:jcnr':'|||',
        'kcmcGrid:_ctl16:jcnr':'|||',
        'dpkcmcGrid:txtChoosePage':4,
        'dpkcmcGrid:txtPageSize':15,
        'Button1':'提交'
    }
if __name__=='__main__':
    login()
    choseClass()
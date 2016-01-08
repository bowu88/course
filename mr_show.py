# -*- coding:utf-8 -*-
from urllib import request,parse
import urllib
import http.cookiejar
from bs4 import BeautifulSoup
import re
class mr_show(object):
    def __init__(self):
        FileCookie='D:\\workspace\\python\\hzau\\course\\config\\cookie.conf'
        self.cj=http.cookiejar.LWPCookieJar()
        self.cookie_support=urllib.request.HTTPCookieProcessor(self.cj)
        self.opener=urllib.request.build_opener(self.cookie_support,urllib.request.HTTPHandler)
        urllib.request.install_opener(self.opener)
        self.cj.load(FileCookie, ignore_discard=True, ignore_expires=True)
    def getView(self):
        reqURL='http://jw.hzau.edu.cn/xf_xsqxxxk.aspx?xh=2013307201006&xm=%B3%CC%CA%E9%D2%E2&gnmkdm=N121111'
        headers={
            'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
            'Accept-Encoding':'gzip, deflate, sdch',
            'Accept-Language':'zh-CN,zh;q=0.8',
            'Cache-Control':'no-cache',
            'Connection':'keep-alive',
            'Host':'jw.hzau.edu.cn',
            'Pragma':'no-cache',
            'Referer':'http://jw.hzau.edu.cn/xs_main.aspx?xh=2013307201006',
            'Upgrade-Insecure-Requests':'1',
            'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/47.0.2526.106 Safari/537.36'
        }
        req=urllib.request.Request(reqURL,headers=headers)
        f=urllib.request.urlopen(req,timeout=10)
        html=f.read().decode('gbk')
        soup=BeautifulSoup(html,'html.parser')
        soup=soup.find_all(attrs={'name':'__VIEWSTATE'})[0]
        viewstate=soup.get('value')
        #print(html)
        return viewstate
        form={
            '__EVENTTARGET':'',
            '__EVENTARGUMENT':'',
            '__VIEWSTATE':viewstate,
            'ddl_kcxz':'',
            'ddl_ywyl':'有',
            'ddl_kcgs':'自然科学',#select sort 人文科学
            'ddl_xqbs':1,
            'ddl_sksj':'',
            'TextBox1':'',
            'kcmcGrid:_ctl2:jcnr':'|||',#11
            'kcmcGrid:_ctl3:jcnr':'|||',
            'kcmcGrid:_ctl4:xk':'|||',
            'kcmcGrid:_ctl4:jcnr':'|||',
            'kcmcGrid:_ctl5:xk':'|||',
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
        }
        #post_data=urllib.parse.urlencode(form).encode(encoding='utf-8')
        #req=urllib.request.Request(reqURL,post_data,headers)
        #f=urllib.request.urlopen(req,timeout=10)
        #html=f.read().decode('gbk')
        #soup=BeautifulSoup(html,'html.parser')
        #soup=soup.find_all(attrs={'name':'__VIEWSTATE'})[0]
        #viewstate=soup.get('value')
        return viewstate
    def choseClass(self,qid=10):
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
            'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/47.0.2526.106 Safari/537.36'
        }
        reqURL='http://jw.hzau.edu.cn/xf_xsqxxxk.aspx?xh=2013307201006&xm=%B3%CC%CA%E9%D2%E2&gnmkdm=N121111'
        while True:
            viewstate=self.getView()
            if viewstate:
                break
        form={
            '__EVENTTARGET':'',
            '__EVENTARGUMENT':'',
            '__VIEWSTATE':viewstate,
            'ddl_kcxz':'',
            'ddl_ywyl':'有',
            'ddl_kcgs':'自然科学',#select sort 人文科学
            'ddl_xqbs':1,
            'ddl_sksj':'',
            'TextBox1':'',
            'kcmcGrid:_ctl2:jcnr':'|||',#11
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
            'dpkcmcGrid:txtChoosePage':2,
            'dpkcmcGrid:txtPageSize':15,
            'Button1':'提交'
        }
        post_data=urllib.parse.urlencode(form).encode(encoding='utf-8')
        req=urllib.request.Request(reqURL,post_data,headers)
        try:
            f=urllib.request.urlopen(req,timeout=10)
            if qid%10==0:
                html=f.read().decode('gbk')
                print(html)
                if qid%1000==0:
                    path='D:\\workspace\\python\\hzau\\course\\config\\allCourse.conf'
                    file=open(path,'w')
                    file.write(html)
                    print('已经写入文件')
                    file.close()
                soup=BeautifulSoup(html,'html.parser')
                try:
                    print(soup.find_all('fieldset')[1])
                except:
                    print('soup list index out of range')
            else:
                print('第',qid,'个任务完成')
        except:
            print('url cannot open')
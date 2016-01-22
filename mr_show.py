# -*- coding:utf-8 -*-
from urllib import request,parse
import urllib
import http.cookiejar
from bs4 import BeautifulSoup
import re
'''
show class
'''
class mr_show(object):
    schedule='http://jw.hzau.edu.cn/xskbcx.aspx?xh=2013307201006&xm=%B3%CC%CA%E9%D2%E2&gnmkdm=N121603'
    
    #School year and Semester
    schoolYear='2015-2016'
    semester='2'
    
    def __init__(self):
        FileCookie='D:\\workspace\\python\\hzau\\course\\config\\cookie.conf'
        cj=http.cookiejar.LWPCookieJar()
        cookie_support=urllib.request.HTTPCookieProcessor(cj)
        opener=urllib.request.build_opener(cookie_support,urllib.request.HTTPHandler)
        urllib.request.install_opener(opener)
        cj.load(FileCookie, ignore_discard=True, ignore_expires=True)
    
    def getView(self,url):
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
        viewstate=None
        req=urllib.request.Request(url,headers=headers)
        while viewstate is None:
            try:
                html=urllib.request.urlopen(req, timeout=3).read().decode('gbk')
                soup=BeautifulSoup(html,'html.parser')
                try:
                    soup=soup.find_all(attrs={'name':'__VIEWSTATE'})[0]
                    viewstate=soup.get('value')
                except:
                    print('get response but cant get VIEWSTATE')
                    continue
            except:
                print('get schedule has not accepted response')
                continue
        return viewstate
    # only get the html not filter
    # finish this maybe you should see someting in demo.py
    def showClass(self):
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
            'Referer':'http://jw.hzau.edu.cn/xskbcx.aspx?xh=2013307201006&xm=%B3%CC%CA%E9%D2%E2&gnmkdm=N121603',
            'Upgrade-Insecure-Requests':'1',
            'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/47.0.2526.106 Safari/537.36'
            }
        form={
            '__EVENTTARGET':'xqd',
            '__EVENTARGUMENT':'',
            '__VIEWSTATE':self.getView(self.schedule),
            'xnd':self.schoolYear,
            'xqd':self.semester
            }
        post_data=urllib.parse.urlencode(form).encode(encoding='utf_8')
        req=urllib.request.Request(self.schedule,post_data,headers)
        html=urllib.request.urlopen(req).read().decode('gbk')
# -*- coding:utf-8 -*-
from urllib import request,parse
import urllib
import http.cookiejar
from bs4 import BeautifulSoup
import re
'''
select course
step 1:loading cookie
step 2:open course page and get viewstate
step 3:generate form and headers ,then open course page which modify the pagesize for 150,finally input number which you want choose
step 4:post data and check response
'''
class mr_select:
    
    flag='成功' #set flag for successfully course 
    
    #ddl_kcgs the sort for nature science or people cuture and so on
    #tid means the position of the target class in the list 
    def __init__(self,ddl_kcgs):
        FileCookie='D:\\workspace\\python\\hzau\\course\\config\\cookie.conf'
        cj=http.cookiejar.LWPCookieJar()
        cookie_support=urllib.request.HTTPCookieProcessor(cj)
        opener=urllib.request.build_opener(cookie_support,urllib.request.HTTPHandler)
        urllib.request.install_opener(opener)
        cj.load(FileCookie, ignore_discard=True, ignore_expires=True)
        self.ddl_kcgs=ddl_kcgs
    
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
                print('get available course table has not accepted response')
                continue
        return viewstate
    def showAvailableCourse(self):
        viewstate=None
        reqURL='http://jw.hzau.edu.cn/xf_xsqxxxk.aspx?xh=2013307201006&xm=%B3%CC%CA%E9%D2%E2&gnmkdm=N121111'
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
        if viewstate is None:
            viewstate=self.getView(reqURL)
        while True:
            form={
                '__EVENTTARGET':'dpkcmcGrid:txtPageSize',
                '__EVENTARGUMENT':'',
                '__VIEWSTATE':viewstate,
                'ddl_kcxz':'',
                'ddl_ywyl':'%D3%D0',
                'ddl_kcgs':self.ddl_kcgs,#select sort 人文科学
                'ddl_xqbs':1,
                'ddl_sksj':'',
                'TextBox1':'',
                'dpkcmcGrid:txtChoosePage':1,
                'dpkcmcGrid:txtPageSize':150,
                'Button1':'  提交  '
            }
            post_data=urllib.parse.urlencode(form).encode(encoding='utf-8')
            req=urllib.request.Request(reqURL,post_data,headers)
            try:
                html=urllib.request.urlopen(req, timeout=3).read().decode('gbk')
                if not re.findall('课程归属',str(html)):
                    print('can\'t find the successful flag')
                    continue
                else:
                    soup=BeautifulSoup(html,'html.parser')
                    try:
                        view=soup.find_all(attrs={'name':'__VIEWSTATE'})[0]
                        viewstate=view.get('value')
                        if viewstate is None or viewstate=='':
                            print('cant get viewstate call again')
                            continue
                        soup=soup.find_all('table')[0]
                        soup=soup.find_all('tr')
                        for i in range(len(soup)):
                            item=str(soup[i])
                            dr = re.compile(r'<[^>]+>',re.S)#[^>] compile not '>' and ending until find '>'
                            dd = dr.sub('',item)
                            dd="".join(dd.split())          #delete \n\r
                            print('%-5s' %str(i+1), dd)     #format output
                        tid=input('please input which course you want choose:')
                        break
                    except:
                        print('beautiful soup may be a monster')
                        continue
            except:
                print('available course page has no accepted response')
                continue
        self.course(tid,viewstate)
    def course(self,tid,viewstate):
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
        kcmcGrid='kcmcGrid:_ctl'+tid+':xk'
        form={
            '__EVENTTARGET':'',
            '__EVENTARGUMENT':'',
            '__VIEWSTATE':viewstate,
            kcmcGrid:'on',
            'dpkcmcGrid:txtChoosePage':1,
            'dpkcmcGrid:txtPageSize':150,
            'Button1':' \314\341\275\273'#submit
        }
        while True:
            post_data=urllib.parse.urlencode(form).encode(encoding='utf-8')
            req=urllib.request.Request(reqURL,post_data,headers)
            try:
                html=urllib.request.urlopen(req, timeout=3).read().decode('gbk')
                if not re.findall(self.flag,str(html)):
                    print(html[0:100])
                else:
                    break
            except:
                print('course not response')
                continue
            break
    def door(self):
        self.showAvailableCourse()
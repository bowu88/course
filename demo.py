# -*- coding:utf-8 -*-
from bs4 import BeautifulSoup
import re
import urllib
from urllib import request,parse
reqURL='http://jw.hzau.edu.cn/xf_xsqxxxk.aspx?xh=2013307201006&xm=%B3%CC%CA%E9%D2%E2&gnmkdm=N121111'
f=urllib.request.urlopen(url, data, timeout)
form={
    '__EVENTTARGET':'',
    '__EVENTARGUMENT':'',
    '__VIEWSTATE':'viewstate',
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
post_data=urllib.parse.urlencode(form).encode(encoding='utf-8')
print(post_data)
exit()
path='D:\\workspace\\python\\hzau\\course\\config\\allCourse.conf'
file=open(path,'r')
def has_class_but_no_id(tag):
    return tag.has_attr('class') and not tag.has_attr('id')
html=file.read()
soup=BeautifulSoup(html,'html.parser')
soup=soup.find_all(attrs={'name':'__VIEWSTATE'})
print(soup)
'''lis=soup.find_all('tr')
path='D:\\workspace\\python\\hzau\\course\\config\\table.html'
file=open(path,'a')
for i in range(1,16):
    l=str(lis[i].encode(encoding='utf-8', errors='strict'))
    file.write(l)
file.close()'''
#print(len(soup.find_all('tr',id=re.compile('kcmcGrid'))))
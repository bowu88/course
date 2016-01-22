# -*- coding:utf-8 -*-
from bs4 import BeautifulSoup
import re
import urllib
from urllib import request,parse
path='D:\\workspace\\python\\hzau\\course\\config\\allCourse.conf'
file=open(path,'r',encoding='utf-8')
html=file.read()
soup=BeautifulSoup(html,'html.parser')
soup=soup.find_all('table')[0]
soup=soup.find_all('tr')
for i in range(len(soup)):
    item=str(soup[i])
    dr = re.compile(r'<[^>]+>',re.S)
    dd = dr.sub('',item)
    dd="".join(dd.split())
    print('%-5s' %str(i+1), dd)
#soup=str(soup)
#pattern01='<td align="Center" rowspan="2" width="7%">(.*?)<br>(.*?)<br>(.*?)<br>(.*?)<br>(.*?)</br></br></br></br></td>'
#pattern02='<td align="Center" rowspan="2">(.*?)<br>(.*?)<br>(.*?)<br>(.*?)<br>(.*?)</td>'
#result=re.findall(pattern02,str(soup))
'''lis=soup.find_all('tr')
path='D:\\workspace\\python\\hzau\\course\\config\\table.html'
file=open(path,'a')
for i in range(1,16):
    l=str(lis[i].encode(encoding='utf-8', errors='strict'))
    file.write(l)
file.close()'''
#print(len(soup.find_all('tr',id=re.compile('kcmcGrid'))))
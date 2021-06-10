import requests
from bs4 import BeautifulSoup
import urllib.request
import random
import threading
import time
import pymysql
db = pymysql.connect(host='remotemysql.com', user="LKrNYglnPu",password='SJP4zwTBe0',database="LKrNYglnPu",charset='utf8')
cursor = db.cursor()
def 上传数据库(img):
    

    sql="""INSERT INTO `imgs` (`url`) VALUES ('"""+img+"""');"""

    try:
        
       cursor.execute(sql)  
       db.commit()
       print('上传成功')

    except:
   # 如果发生错误则回滚
        db.rollback()

urls = []

r=requests.get('https://qiqimh.top/?232xe-tupianqu/YSE/index_21.html')
html=r.text
sp=BeautifulSoup(html,"lxml")
for x in sp.find_all('a'):
    if x.get('href').find('232xe-tttppp') >=0 :
        print(x.get('href'))
        urls.append(x.get('href'))
for url in urls :
    r=requests.get('http://qiqimh.top/'+url)
    html=r.text
    sp=BeautifulSoup(html,'lxml')
    for x in sp.find_all('img'):
        print(x.get('src'))
        上传数据库(img=x.get('src'))
        
        
        
    




    
    


    



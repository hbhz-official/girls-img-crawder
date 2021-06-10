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
def 爬虫(num):
    urls = []
    r=requests.get('https://qiqimh.top/?232xe-tupianqu/YSE/index_'+num+'.html')
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
            time.sleep(0.5)
            上传数据库(img=x.get('src'))


    
for i in range(16,20):
    t = threading.Thread(target=爬虫,kwargs={'num':str(i)})
    t.setDaemon(True)
    t.start()
    print('线程启动')
    
    
t.join()
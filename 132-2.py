import requests
from bs4 import BeautifulSoup
import urllib.request
import random
import threading
import time
import pymysql

total=0
a=time.time()

def 爬虫(num):
    db = pymysql.connect(host='remotemysql.com', user="V0Y3Pj4eE9",password='bHlu56mY0A',database="V0Y3Pj4eE9",charset='utf8')
    cursor = db.cursor()
    urls = []
    r=requests.get('https://qiqimh.top/?232xe-tupianqu/MSE/index_'+num+'.html')
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
            img=x.get('src')
            print(img)           
            sql="""INSERT INTO `imgs-2` (`url`) VALUES ('"""+img+"""');"""
            try:        
                cursor.execute(sql)  
                db.commit()
                global total
                total = total+1                
                print('上传成功: '+total)               
            except:
            # 如果发生错误则回滚
                db.rollback()
    db.close()
    

    
for i in range(16,20):        
    while True :  
        thread_num=len(threading.enumerate())    
        if thread_num<9:
            t = threading.Thread(target=爬虫,kwargs={'num':str(i)})
            t.setDaemon(True)
            t.start()
            print('线程启动')
            break              
t.join()
b=time.time()

print('共耗时：'+str(b-a))
print('累计上传'+total)



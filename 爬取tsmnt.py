import requests
from bs4 import BeautifulSoup
import urllib.request
import random
import threading
import time
import pymysql

total=0

def 爬虫(url):
    db = pymysql.connect(host='remotemysql.com', user="LKrNYglnPu",password='SJP4zwTBe0',database="LKrNYglnPu",charset='utf8')
    cursor = db.cursor()
    
    
    imgs=[]
    r=requests.get(url)
    html=r.text
    sp=BeautifulSoup(html,"lxml")
    for x in sp.find_all('a'):
        if len(x.get('href'))<=17:
            r=requests.get(url[0:50]+x.get('href'))
            html=r.text
            sp=BeautifulSoup(html,"lxml")
            if sp.find('img') != None:
                img= sp.find('img').get('src')
                print(img)
                global total
                total = total+1
                sql="""INSERT INTO `imgs` (`url`) VALUES ('"""+img+"""');"""

                try:

                    cursor.execute(sql)  
                    db.commit()                   
                    print('上传成功:'+str(total))

                except:
   # 如z果发生错误则回滚

                    db.rollback()
    db.close()         




for i in range (1,77):
    a=time.time()


    urls = []
    r=requests.get('http://www.qjtaotu.com/quanji/tutups/pr/'+str(i)+'.html')
    html=r.text
    sp=BeautifulSoup(html,"lxml")
    for x in sp.find_all('a'):
        if x.get('href').find('quanji')>=0:
            print(x.get('href'))
            urls.append('http://www.qjtaotu.com'+x.get('href'))



# 写法1
    for url in urls:
        
        while True :
            thread_num = len(threading.enumerate())
            if thread_num < 9:            
                t=threading.Thread(target=爬虫,kwargs={'url':url})
                t.setDaemon(True)
                t.start()
                print('线程启动')
                break         
    t.join()
    b=time.time()

    print('上传完成！')
    print(len(urls))
    print(b-a)  
    
print('已上传：'+str(total))


    

# 写法2
# for url in urls:
    
    
        # t=threading.Thread(target=爬虫,kwargs={'url':url})
        # t.setDaemon(True)
        # t.start()
        # print('线程启动')
        # time.sleep(5)
    



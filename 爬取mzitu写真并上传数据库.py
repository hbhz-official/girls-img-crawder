import requests
from bs4 import BeautifulSoup
import urllib.request
import pymysql
import threading
import time
db = pymysql.connect(host='remotemysql.com', user="LKrNYglnPu",password='SJP4zwTBe0',database="LKrNYglnPu",charset='utf8')
cursor = db.cursor()


def 数字处理(num):
    if num < 10:
        return('0'+str(num))
    if num >= 10:
        return(str(num))
    
def 上传数据库(img):
    

    sql="""INSERT INTO `img` (`url`, `style`) VALUES ('"""+img+"""', '');"""

    try:
        
       cursor.execute(sql)  
       db.commit()
       print('上传成功')

    except:
   # 如果发生错误则回滚
        db.rollback()
    


for month in range (1,12):
    for head in range(1,28):    
        for foot in range(1,16):
            img='https://imgpc.iimzt.com/2019/'+数字处理(month)+'/'+数字处理(head)+'b'+数字处理(foot)+'.jpg'             
            print(img)
            上传数据库(img)
            
    



# for aurl in urls:
    # t = threading.Thread(target=上传数据库,kwargs={'img':aurl})
    # t.setDaemon(True)
    
    # t.start()    
    # t.join()

    
        
        
        
        



# 关闭数据库连接
db.close()



# while(n1<sta+10):
    # for i in range(1,11):
       # img='https://imgpc.iimzt.com/2020/07/'+str(n1)+'a0'+str(i) 
       # print(img)
    
    
    

    
    
    
 
    # n1=n1 + 1

    

    # r=requests.get(u1)
    
    
    # html=r.text
    # sp=BeautifulSoup(html,"lxml")
    

    
    
    # for x in sp.find_all('img'):
         
         # print(x.get('src'))
         # dpic(x.get('src'),str(random.randint(-100000,1000000)))
         
    

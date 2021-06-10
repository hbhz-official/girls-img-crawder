import requests
from bs4 import BeautifulSoup
import urllib.request
import random
import threading
import time

urls = []
r=requests.get('http://www.xjjmzt.com/xiaojiejie/tuapicgm/25_1.html')
html=r.text
sp=BeautifulSoup(html,"lxml")
for x in sp.find_all('a'):
    print(x.get('href'))




    
    


    
while(n<sta+1):
    
    u0="http://nsfwpicx.com"
    
    
    
    u1=u0+'/'+str(n)+'.html'
    
    
    

    r=requests.get(u1)
    
    
    html=r.text
    sp=BeautifulSoup(html,"lxml")

    n=n+1
    
    
    for x in sp.find_all('img'):
         

        print(x.get('src'))
        urls.append(x.get('src'))
        
print(len(urls),'number') 
a=time.time()

for url in urls:
    t = threading.Thread(target=dpic,args=(url,))
    t.setDaemon(True)
    t.start()

b=time.time()
print(b-a)

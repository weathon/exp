#coding:utf-8
#from https://www.cnblogs.com/ichunqiu/p/9145125.html
import requests
from bs4 import BeautifulSoup as bs  #这里吧模块命名为了bs，方面我们调用。
import re
def main():
    for i in range(0,10,10000):
        url='https://www.baidu.com/s?wd=site:www.bilibili.com&pn=%s'%(str(i))
        headers={'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:60.0) Gecko/20100101 Firefox/60.0'}
        r=requests.get(url=url,headers=headers)
        soup=bs(r.content,'lxml')
        urls=soup.find_all(name='a',attrs={'data-click':re.compile(('.')),'class':None})#利用bs取出我们想要的内容，re模块是为了让我们取出这个标签的所有内容。
        #print(urls)
        for urli in urls:
            print(urli['href'])

            f=open("urls","w")
            f.write(urli['href'])
            f.close()
main()

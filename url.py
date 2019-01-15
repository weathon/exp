#coding:utf-8
#from https://www.cnblogs.com/ichunqiu/p/9145125.html
def main():
    for i in range(0,10,10):
        url='https://www.baidu.com/s?wd=芒果&pn=%s'%(str(i))
        headers={'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:60.0) Gecko/20100101 Firefox/60.0'}
        r=requests.get(url=url,headers=headers)
        soup=bs(r.content,'lxml')
        urls=soup.find_all(name='a',attrs={'data-click':re.compile(('.')),'class':None})#利用bs取出我们想要的内容，re模块是为了让我们取出这个标签的所有内容。
        for url in urls:
            r_get_url=requests.get(url=url['href'],headers=headers,timeout=4)#请求抓取的链接，并设置超时时间为4秒。
            if r_get_url.status_code==200:#判断状态码是否为200
                url_para= r_get_url.url#获取状态码为200的链接

                url_index_tmp=url_para.split('/')#以“/”分割url
                url_index=url_index_tmp[0]+'//'+url_index_tmp[2]#将分割后的网址重新拼凑成标准的格式。
                print url_index

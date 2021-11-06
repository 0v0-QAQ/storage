# 扩展模块
import urllib3
import certifi
import socket
import chardet

# 设置工作目录至:项目根目录
from lxml import etree

# 单页html源码下载
def spider1(url):
    http = urllib3.PoolManager(cert_reqs="CERT_REQUIRED", ca_certs=certifi.where())
    url = url.replace("https://", "http://")
    timeout = 5
    socket.setdefaulttimeout(timeout)
    response = http.request('GET', url)  # TODO all https:// --> http://   ?

    # 获得html源码并解码
    encode = chardet.detect(response.data)
    return response.data.decode(encoding=encode['encoding']), encode['encoding']  # encode['encoding']

def xpath_crawler(url, xpath):
    t,_ = spider1(url)
    html = etree.HTML(t)
    res = html.xpath(xpath)
    return res

if __name__ == '__main__':
    url = "https://www.qkl123.com/ranking"
    # url = input("输入url：")
    # print(url)

    xpath = "//*[@id='market-section']/div/div[2]/div/div[1]/div[3]/table/tbody/tr[2]/td[10]/div/span[2]/span[1]"
    # xpath = input("输入xpath：")
    # print(xpath)

    print(xpath_crawler(url, xpath)[0].text)

import requests
import random
import threading
import re
from lxml import etree
import xlrd
import xlwt


headersList = [
    "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36",
    "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/22.0.1207.1 Safari/537.1",
    "Mozilla/5.0 (X11; CrOS i686 2268.111.0) AppleWebKit/536.11 (KHTML, like Gecko) Chrome/20.0.1132.57 Safari/536.11",
    "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.6 (KHTML, like Gecko) Chrome/20.0.1092.0 Safari/536.6",
    "Mozilla/5.0 (Windows NT 6.2) AppleWebKit/536.6 (KHTML, like Gecko) Chrome/20.0.1090.0 Safari/536.6",
    "Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/19.77.34.5 Safari/537.1",
    "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/536.5 (KHTML, like Gecko) Chrome/19.0.1084.9 Safari/536.5",
]
usableIP = []


def header():
    headers = {"User-Agent": random.choice(headersList)}
    return headers

try:
    # myworkbook=xlrd.open_workbook('')

    myworkbook = xlwt.Workbook()
    myworksheet = myworkbook.add_sheet('test')


    print("正在获取代理IP...")
    for page in range(1,11):
      print("测试第"+str(page)+"页")
      #print(page)
      url = "http://www.qydaili.com/free/?action=china&page=" + str(page)
      headers = header()
      sess = requests.Session()
      html = sess.get(url, headers=headers).text
      selector = etree.HTML(html)
      # 获取ip
      ipList = selector.xpath('//td[1]/text()')
      # 获取端口号
      portList = selector.xpath('//td[2]/text()')
      # 获取ip类型
      typeList = selector.xpath('//td[4]/text()')
      #获取位置
      locationList = selector.xpath('//td[5]/text()')
      for j in range(1,11):
          print(str(j))
          myworksheet.write((page-1)*10+j, 0, ipList[j-1])
          myworksheet.write((page-1)*10+j, 1, portList[j-1])
          myworksheet.write((page-1)*10+j, 2, typeList[j-1])
          myworksheet.write((page-1)*10+j, 3, locationList[j-1])
      #http: // www.ip3366.net / free /?stype = 1 & page = 1
      #page = 1
      # print("测试第"+str(page)+"页")
      url = "http://www.ip3366.net/free/?stype=1&page=" + str(page)
      headers = header()
      sess = requests.Session()
      html = sess.get(url, headers=headers).text
      selector = etree.HTML(html)
      # 获取ip
      ipList = selector.xpath('//td[1]/text()')
      # 获取端口号
      portList = selector.xpath('//td[2]/text()')
      # 获取ip类型
      typeList = selector.xpath('//td[4]/text()')
      # 获取位置
      locationList = selector.xpath('//td[5]/text()')
      for j in range(1,11):
          #print('j='+str(j))
          myworksheet.write((page-1)*10+j, 5, ipList[j-1])
          myworksheet.write((page-1)*10+j, 6, portList[j-1])
          myworksheet.write((page-1)*10+j, 7, typeList[j-1])
          myworksheet.write((page-1)*10+j, 8, locationList[j-1])
      #myworksheet.write(page+1, 0, ipList[0])
      #myworksheet.write(page+1, 1, portList[0])
      #myworksheet.write(page+1, 2, typeList[0])
      #myworksheet.write(page+1, 3, locationList[0])
    myworkbook.save('d:/takeip.xls')
except:
    print("获取失败")
import random
import xlrd
import xlwt
import urllib
import requests
import xlutils

mynewworkbook=xlwt.Workbook()
mynewworksheet=mynewworkbook.add_sheet('proxy')
#myworksheet.write(0,0,'=today()')
#myworksheet.write(0,1,'=column()')
#myworksheet.write(0,2,'=2*3')
#myworkbook.save('d:/test.xls')

myworkbook=xlrd.open_workbook('d:/test.xls','rb')
mysheet=myworkbook.sheet_by_name('test')
maxrows=mysheet.nrows
#maxrows=5
validproxy=0
for i in range(1,maxrows):
    IP=mysheet.cell_value(i,0)
    xy=mysheet.cell_value(i,1)
    #requests.adapters.DEFAULT_RETRIES = 3
    #IP = random.choice(IPAgents)
    #thisProxy = "http://" + IP
    thisProxy = IP
    thisIP = "".join(IP.split(":")[0:1])
    print(thisIP)
    print(thisProxy)
    #if xy=="http":
    #    res = requests.get(url="http://icanhazip.com/", timeout=8, proxies={"http": thisProxy})
    #if xy=="https" :
    #     res = requests.get(url="http://icanhazip.com/", timeout=8, proxies={"https": thisProxy})
    #if xy=="socks4":
    #     res = requests.get(url="http://icanhazip.com/",timeout=8,proxies={"socks4":thisProxy})
    #if xy="socks5"
    #     res = requests.get(url="http://icanhazip.com/", timeout=8, proxies={"socks5": thisProxy})
    try:
       res = requests.get(url="http://icanhazip.com/", timeout=3, proxies={xy: thisProxy})
       proxyIP = res.text
       lenip=len(proxyIP)
       print(proxyIP[0:lenip-1]+"="+thisIP)
       if(proxyIP[0:lenip-1] == thisIP):
          print("代理IP:'"+ thisIP + "'有效！有效啦，有效啦，哈哈哈哈哈哈")
          validproxy=validproxy+1
          mynewworksheet.write(validproxy,0,thisProxy)
          #获取响应时间 0:00:00 0000 格式
          mynewworksheet.write(validproxy,1,res.elapsed.total_seconds())
       else:
          print("代理IP:"+thisIP+"无效！")
    except:
          print("代理IP:" + thisIP + "有问题，无法连接！")
mynewworkbook.save('d:/proxy.xls')
print("有效代理"+str(validproxy)+"个")
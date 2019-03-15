#!/usr/bin/python
#coding=utf8
"""
#jd.com网页版,获取京东卡的总额
#20190315

"""
import requests
import re


class jdCardMoney():
    def __init__(self,Cookie):
        ##获取京东卡url
        self.url="https://mygiftcard.jd.com/giftcard/queryGiftCardItemBigImg.action"
        ##Post参加
        ##page为页面参数        
        self.data={
            "cardType": "-1",
            "queryType": "1",
            "page": "1",
            "pageSize": "15",
            "random": "0.08877698125319267"
        }
        ##头部信息
        self.headers={
            "Accept":"text/html, */*; q=0.01",
            "Accept-Encoding":"gzip, deflate, br",
            "Accept-Language":"zh-CN,zh;q=0.9,en;q=0.8",
            "Connection":"keep-alive",
            "Content-Length":"69",
            "Content-Type":"application/x-www-form-urlencoded",
            "Cookie":Cookie,
            "Host":"mygiftcard.jd.com",
            "Origin":"https://mygiftcard.jd.com",
            "Referer":"https://mygiftcard.jd.com/giftcard/myGiftCardInit.action",
            "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.110 Safari/537.36",
            "X-Requested-With":"XMLHttpRequest"
        }

    ##获取京东卡最大页面值
    def getPageCount(self):
        res=requests.post(url=self.url,headers=self.headers,data=self.data)
        #print res.text
        return re.findall("<span>...</span>.*?<a rel=\"(.*?)\"",res.text.encode('utf8'),re.S)[0]

    ##计算京东卡总额
    def getCard(self):
        ##最后页面
        pageCount=self.getPageCount()
        moneyCount=0
        ##循环每页面京东卡余额
        for page in range(1,int(pageCount)+1):
            import time
            time.sleep(1)
            self.data.update({"page":page})
            res=requests.post(url=self.url,headers=self.headers,data=self.data)
            ##获取京东卡余额
            for k in re.findall("余额：<span class=\"icon\">￥</span><span class=\"num\">(.*?)</span>",res.text.encode('utf8'),re.S):
                moneyCount=float(k)+moneyCount

        ##输出京东卡总余额
        print moneyCount


Cookie=""

obj=jdCardMoney(Cookie)
obj.getCard()

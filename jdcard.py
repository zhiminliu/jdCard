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


Cookie="shshshfpa=c70f4b42-ac06-77de-cb47-a62e3c5d27e3-1547198471; shshshfpb=uASrguRlaotGQwGChVSG%2FPw%3D%3D; __jda=122270672.1547198469254459992973.1547198469.1547198469.1547198469.1; __jdc=122270672; pin=qliuzhimin; _tp=VcfwcHL1A976Xws%2FqXtx3Q%3D%3D; _pst=qliuzhimin; user-key=cc83066f-78b2-4787-8ff2-853e6b31f328; cn=0; TrackID=1ren-j59wwoD9W6X9evYE7FvZBL1Q_-vrhSv6fvY3PH3c1rJVZ5b6zOypQtDMgGpA0CiCN_q3MD9WvfcRxvTIMaNbyBhvoRiBx9knE-0y9xUmPOnBII9bpMQKqTxFFnL_; ceshi3.com=000; __jdc=122270672; unpl=V2_ZzNtbUJXE0UhC0cEckpYAWIDF19LAkEQc1oSVHoYXldvCxNbclRCFX0UR1ZnGFoUZwMZXEtcQhdFCEdkexhdBGYKGlRKVXMVcQ8oVRUZVQAJbRFfFgMWHCALT1x7SwsANVAibUFXcxRFCEZVfhBZA2EEFG1yV0sRRQxFUXgbXwxX1LvzlNvlwcyikeb5KVgDZAUWXENWQCV0OEdkLXdcBGYCE1xHV0AXOAhGVX4QWQNhBBRtQ2dA; __jdv=122270672|www.linkstars.com|t_1000089893_156_0_184__23eed8d2891cf4cb|tuiguang|11aae20a8b5541438d347ce1003c9907|1551928082515; mt_xid=V2_52007VwMSU1hRV1wZTh9sVjMGQFJaWFVGGR0fDBliAEVVQVBQWUhVGFQDbwUQV1QKAV0deRpdBW8fE1BBWVRLH0kSXQxsAhRiX2hRahxIH1QAYjMSVlw%3D; PCSYCityID=1601; shshshfp=97be6178d5f7ce8a403fab9129c300ff; areaId=19; ipLoc-djd=19-1601-50283-0; unick=jdqliuzh; pinId=5bF59DptAJtjvB5oK0iAKg; 3AB9D23F7A4B3C9B=IKPLMJYLJZ7U5ZIHRVZMMC5PJF3EHXOJ3CXXOVPTSH6DYCZ6HKI2LSXMDXXSUGD636DXVRWIVOL2UQMUO53XQZ4FZY; __jdu=1547198469254459992973; wlfstk_smdl=v6wot9asoknlkmzakjph2wp0dvrztqxp; logintype=wx; npin=qliuzhimin; thor=D14B29A99CE3619A7EF82B859750FB856B87D679CC221BD74906D91F8B3DB69F0D9A3B36F2556F01825CA2E4612CCAEF936EC3C05FD00B37C9101E4AA5681A1B85A997AA41F38D44C8A80589D986F479DCF525C9CF1C68C027AF0BDB2C7B5DD416231E4BCFF5CDBF8BE0B3A3D74EDC856F2B680EB1A93FE4FFFAA585090329920CA140B04941F7D6D35C3C2DEE0C3AFC; __jda=122270672.1547198469254459992973.1547198469.1547198469.1547198469.1; __jdb=122270672.4.1547198469254459992973|1.1547198469; __jdb=122270672.5.1547198469254459992973|1.1547198469"

obj=jdCardMoney(Cookie)
obj.getCard()

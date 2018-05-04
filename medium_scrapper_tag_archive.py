# -*- coding: utf-8 -*-
"""
Created on Tue May  1 23:30:54 2018

@author: Aiswarya

This scrapper extracts data for a given date and a given tag
"""

import scrapy
import codecs
import json
from datetime import datetime
from datetime import timedelta
import os

def writeTofile(fileName,text):
    with codecs.open(fileName,'w','utf-8') as outfile:
        outfile.write(text)

class MediumPost(scrapy.Spider):
    name='medium_scrapper'
    handle_httpstatus_list = [401,400]
    
    autothrottle_enabled=True
    def start_requests(self):
        
        start_urls = ['https://medium.com/tag/'+self.tagSlug.strip("'")+'/archive/']
        print(start_urls)
        
        cookie={
                                '__cfduid':'da03ee0d47b0f9fc62cd620eb2e19740d1525156135',
                                '_ga':'GA1.2.1177081718.1525156137',
                                '_gid':'GA1.2.1879325541.1525156137',
                                'lightstep_guid/medium-web':'288180d9401c5407',
                                'lightstep_session_id':'fc3f8a3ecff727b0',
                                'pr':'1.25',
                                'tz':'-330', 
                                'uid':'7bbdad3b3571',
                                'sid':'1:BebZ9kr91ptfgtxqzANJqwhq8CuEq1XMkZT1fE3Wm23QnIknPhEjnUEItoNqAm7T',
                                'xsrf':'hBL2qH8I5ckb',
                                'xsrf':'kir9Fl-1QBDt7ZZT', 
                                '__cfruid':'7d89b52dc669786052af0fed2fa8785ca30e374f-1525197176',
                                'sz':'674'
                                  }
        header = {
                        'accept': 'application/json',
                        'accept-encoding': 'gzip, deflate, br',
                        'accept-language': 'en-US,en;q=0.9,ta;q=0.8',
                        'content-type': 'application/json',
                        'referer': 'https://medium.com/tag/data-science/archive/2018/03/23',
                        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.139 Safari/537.36',
                        'x-client-date': '1525197603242',
                        'x-obvious-cid': 'web',
                        'x-opentracing': '{"ot-tracer-spanid":"1cbe927d0f29e9","ot-tracer-traceid":"8f0a5b5308eab","ot-tracer-sampled":"true"}',
                        'x-xsrf-token': 'hBL2qH8I5ckb'
        }   
        #start_date=self.start_date
        #end_date=self.end_date
        startDate=datetime.strptime(self.start_date,"%Y%m%d")
        endDate=datetime.strptime(self.end_date,"%Y%m%d")
        delta=endDate-startDate
        print(delta)
        for i in range(delta.days + 1):
            d=datetime.strftime(startDate+timedelta(days=i),'%Y/%m/%d')
            for url in start_urls:
                print(url+d)
                yield scrapy.Request(url+d,method="GET",headers=header,cookies=cookie,callback=self.parse,meta={'reqDate':d})
        
        #for url in start_urls:
            #yield scrapy.Request(url,method='GET',headers=header,cookies=cookie,callback=self.parse)
            #yield scrapy.Request(url,method='GET',body=json.dumps(formdata),headers=header,cookies=cookie,callback=self.parse)
    
    def parse(self,response):
        response_data=response.text
        response_split=response_data.split("while(1);</x>")
        response_data=response_split[1]
        date_post=response.meta['reqDate']
        date_post=date_post.replace("/","")
        directory=datetime.now().strftime("%Y%m%d")
        if not os.path.exists(directory):
            os.makedirs(directory)
        writeTofile(directory+"//"+self.tagSlug.replace("-","").strip("'")+"Tag"+date_post+".json",response_data)
    

    


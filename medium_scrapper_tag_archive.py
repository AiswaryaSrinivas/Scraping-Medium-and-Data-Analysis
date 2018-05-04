# -*- coding: utf-8 -*-
"""
Created on Tue May  1 23:30:54 2018

@author: Aiswarya

This scrapper extracts data for a given date range for a particular medium Tag
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
        
        #Header and cookie information can be got from the Network Tab in Developer Tools
        cookie=cookie
        header =header 
       
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
    

    


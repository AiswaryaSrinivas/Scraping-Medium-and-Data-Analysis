# -*- coding: utf-8 -*-
"""
Created on Sat Apr 07 20:00:44 2018

@author: Aiswarya

#https://medium.com/tag/data-science -to search my tag
"""

import scrapy
import json
import codecs
import datetime


def writeTofile(fileName,text):
    with codecs.open(fileName,'w','utf-8') as outfile:
        outfile.write(text)
class MediumPost(scrapy.Spider):
    name='medium_scrapper'
    handle_httpstatus_list = [401,400]
    
    autothrottle_enabled=True
    def start_requests(self):
        
        start_urls = ['https://www.medium.com/search/posts?q='+self.searchString]
        
        #set cookie and header info by looking to Network Tab in Developer tools
        cookie=cookie
        header = header 
        for url in start_urls:
            
            yield scrapy.Request(url,method='GET',headers=header,cookies=cookie,callback=self.parse)
            

    
    def parse(self,response):
        #writeTofile("Log"+datetime.datetime.now().strftime("%Y%m%d_%H%M%S")+".txt",response.text)        
        response_data=response.text
        response_split=response_data.split("while(1);</x>")
        #num_split= len(response_split)
        response_data=response_split[1]
        filename="medium_"+self.searchString+datetime.datetime.now().strftime("%Y%m%d_%H%M%S")+".json"
        writeTofile(filename,response_data)
        
        with codecs.open(filename,'r','utf-8') as infile:
            data=json.load(infile)
        #Check if there is a next tag in json data
        if 'paging' in data['payload']:
            data=data['payload']['paging']
            if 'next' in data:
                #Make a post request
                print "In Paging, Next Loop"
                data=data['next']
                formdata={
                        'ignoredIds':data['ignoredIds'],
                        'page':data['page'],
                        'pageSize':data['pageSize']
                        }
                cookie=cookie

                header = header
                yield scrapy.Request('https://www.medium.com/search/posts?q='+self.searchString,method='POST',body=json.dumps(formdata),headers=header,cookies=cookie,callback=self.parse)
        
        
        
        
            
    
            

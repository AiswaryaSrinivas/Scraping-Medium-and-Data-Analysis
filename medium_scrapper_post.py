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
        formdata={'ignoredIds': ['bd48ccde7325',
                                 '646ee2cc21a1',
                                 '2c30fdd008cf',
                                 'b5577d75f8b',
                                 '7a87426e103e',
                                 '749ece4d8860',
                                 'f3d363ad47b',
                                 'a136482da89b',
                                 'e9d72d818745',
                                 '5d87f13f0d51'],
                    'page': 1,
                    'pageSize': 10}
        cookie={
                                '__cfduid':'d74571b7cc34a03a824fa032112ad94af1522260237', 
                                '_ga':'GA1.2.113405192.1522260242',
                                'lightstep_guid/medium-web':'841da38c2558c669',
                                 'lightstep_session_id':'c9a4b24574aa1a5a',
                                 'tz':'-330',
                                 'uid':'7bbdad3b3571',
                                 'sid':'1:qQE1emO87DyjMedi0lgbmq/4F6KNjw4TW8SYiwet820WPZgwj6ItLWVcf2Fvxyp1',
                                 'mpids':'b79e6d124a94'
                                  ,
                                  ' __cfruid':'5aaa112809e04292d44fe6713fcc42d89b7c3db0-1523044028',
                                  '_gid':'GA1.2.932259872.1523044031',
                                  'pr':'1.75',
                                  'sz':'356'
                                  }
        header = {
                        'Accept':'application/json',
                        'Accept-Encoding':'gzip, deflate, br',
                        'accept-language':'en-US,en;q=0.9,ms;q=0.8',
                        #'Cookie':cookie,
                        'content-type':'application/json',
                        'x-obvious-cid':'web',
                        'x-opentracing': {"ot-tracer-spanid":"16ebc273e36b48","ot-tracer-traceid":"57df8a2625602f8e","ot-tracer-sampled":"true"},
                        
    
        'Origin':'https://medium.com' ,
        'Referer':'https://medium.com/search?q='+self.searchString,
        'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36',
        'x-xsrf-token':'ewWvuMVYWS2I'
        } 
        for url in start_urls:
            yield scrapy.Request(url,method='POST',body=json.dumps(formdata),headers=header,cookies=cookie,callback=self.parse)
            #yield scrapy.Request(url,method='GET',body=json.dumps(formdata),headers=header,cookies=cookie,callback=self.parse)
            

    
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
                cookie={
                                '__cfduid':'d74571b7cc34a03a824fa032112ad94af1522260237', 
                                '_ga':'GA1.2.113405192.1522260242',
                                'lightstep_guid/medium-web':'841da38c2558c669',
                                 'lightstep_session_id':'c9a4b24574aa1a5a',
                                 'tz':'-330',
                                 'uid':'7bbdad3b3571',
                                 'sid':'1:qQE1emO87DyjMedi0lgbmq/4F6KNjw4TW8SYiwet820WPZgwj6ItLWVcf2Fvxyp1',
                                 'mpids':'b79e6d124a94'
                                  ,
                                  ' __cfruid':'5aaa112809e04292d44fe6713fcc42d89b7c3db0-1523044028',
                                  '_gid':'GA1.2.932259872.1523044031',
                                  'pr':'1.75',
                                  'sz':'356'
                                  }

                header = {
                        'Accept':'application/json',
                        'Accept-Encoding':'gzip, deflate, br',
                        'accept-language':'en-US,en;q=0.9,ms;q=0.8',
                        #'Cookie':cookie,
                        'content-type':'application/json',
                        'x-obvious-cid':'web',
                        'x-opentracing': {"ot-tracer-spanid":"16ebc273e36b48","ot-tracer-traceid":"57df8a2625602f8e","ot-tracer-sampled":"true"},
                        
    
        'Origin':'https://medium.com' ,
        'Referer':'https://medium.com/search?q='+self.searchString,
        'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36',
        'x-xsrf-token':'ewWvuMVYWS2I'
        }   
                yield scrapy.Request('https://www.medium.com/search/posts?q='+self.searchString,method='POST',body=json.dumps(formdata),headers=header,cookies=cookie,callback=self.parse)
        
        
        
        
            
    
            
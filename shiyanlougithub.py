#!/usr/vin/env python3
#-*- coding:utf-8 -*-
import scrapy

class shiyanlouGithub(scrapy.Spider):

    name = 'shiyanlougithub'

    def start_requests(self):
        #https://github.com/shiyanlou?page=2&tab=repositories
        #https://github.com/shiyanlou?page=3&tab=repositories
        url1 = 'https://github.com/shiyanlou?page={}&tab=repositories'
        urls = (url1.format(i) for i in range(1,5))
        for url in urls:
            print(url)
            yield scrapy.Request(url=url,callback=self.parse)

    def parse(self,response):
        
        for i in response.css('li.col-12'):

            yield {

                "name": i.css('a::text').re_first('\s*(\w*)'),

                "update_time":i.css('relative-time::attr(datetime)').extract_first()
                    
                }

#shiyanlouGithub()

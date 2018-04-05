# -*- coding: utf-8 -*-
import scrapy


class RedditbotSpider(scrapy.Spider):
    name = 'redditbot'
    allowed_domains = ['www.reddit.com/r/Cryptocurrency']
    start_urls = ['http://www.reddit.com/r/Cryptocurrency/',
   	'http://www.reddit.com/r/CryptoCurrency/?count=25&after=t3_89zazs'
    ]

    def parse(self, response):
         #Extracting the content using css selectors
        titles = response.css('.title.may-blank::text').extract()
       
       
        for item in zip(titles):
            #create a dictionary to store the scraped info
            scraped_info = {
                'title' : item[0],
            }

            #give the scraped info to scrapy
            yield scraped_info
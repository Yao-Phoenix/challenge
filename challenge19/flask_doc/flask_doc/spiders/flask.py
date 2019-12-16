# -*- coding: utf-8 -*-
import scrapy
from scrapy.spiders import Rule
from scrapy.linkextractors import LinkExtractor
from flask_doc.items import FlaskDocItem

class FlaskSpider(scrapy.spiders.CrawlSpider):
    name = 'flask'
    
    start_urls = ['http://flask.pocoo.org/docs/1.0']
    rules = (Rule(LinkExtractor(
        allow='http://flask.pocoo.org/docs/1.0/*'), callback='parse',
        follow=True),)
    
    def parse(self, response):
        item = FlaskDocItem()
        item['url'] = response.url
        item['text'] = ' '.join(response.xpath('//text()').extract())
        yield item

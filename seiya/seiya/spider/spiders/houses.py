# -*- coding: utf-8 -*-
import scrapy
from items import HouseItem
from scrapy.spiders import Rule
from scrapy.linkextractors import LinkExtractor

class HousesSpider(scrapy.spiders.CrawlSpider):
    name = 'houses'
    start_urls = ['https://cd.lianjia.com/zufang/rt200600000001/']
    
    rules = (Rule(
        LinkExtractor(
            allow='https://cd.lianjia.com/zufang/pg\drt200600000001/*'),
        callback='parse_house',
        follow=True),)

    def parse_house(self, response):
        for data in response.css('div.content__list--item'):
            item = HouseItem(
                    plot = data.css('p.content__list--item--des a::text'
                        ).extract_first().strip(),
                    type = data.css(
                        'p.content__list--item--des::text').re(r'\S\w.*')[-1].strip(),
                    area = data.css(
                        'p.content__list--item--des::text').re(r'\S\w.*')[0].strip(),
                    rent = data.css('span.content__list--item-price em::text'
                        ).extract_first().strip()
                    )
            yield item


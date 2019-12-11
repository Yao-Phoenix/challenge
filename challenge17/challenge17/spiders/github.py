#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import scrapy
from challenge17.items import Challenge17Item


class GithubSaveSpider(scrapy.Spider):
    name = 'github'
    
    @property
    def start_urls(self):
        url_list = ['http://github.com/shiyanlou?tab=repositories']
        return url_list

    def parse(self, response):
        for repositor in response.css('li.public'):
            item = Challenge17Item()
            item['name'] =  repositor.xpath(
                        './/a[@itemprop="name codeRepository"]/text()') \
                                .extract_first().strip(), 
            item['update_time'] =  repositor.xpath('.//relative-time/@datetime') \
                            .extract_first().strip()
            reps_url = response.urljoin(
                    repositor.xpath('.//a/@href').extract_first())
            request = scrapy.Request(reps_url, callback=self.parse_page)
            request.meta['item'] = item
            yield request

        span = response.xpath('//button[@disabled="disabled"]/text()')
        if len(span) == 0 or span[-1].extract() != 'Next':
            next_url = response.css(
                    'div.BtnGroup a:last-child::attr(href)').extract_first()
            yield response.follow(next_url, self.parse)

    def parse_page(self, response):
        item = response.meta['item']
        for num in response.css('ul.numbers-summary'):
            type_text = num.xpath('.//li/a/text()').re(r'\n\s*(.*)\n')
            num_text = num.xpath('.//span[@class="num text-emphasized"]/text()') \
                    .re(r'\n\s*(.*)\n')
            if type_text and num_text:
                for key in type_text:
                    if key in ('commit', 'commits'):
                        item['commits'] = int(num_text[0].replace(',', ''))
                    elif key in ('branch', 'branches'):
                        item['branches'] = int(num_text[1].replace(',', ''))
                    elif key in ('release', 'releases'):
                        item['releases'] = int(num_text[3].replace(',', ''))
        yield item


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
            item = Challenge17Item({
                    'name': repositor.xpath('.//a[@itemprop="name codeRepository"]/text()').extract_first().strip(), 
                    'update_time': repositor.xpath('.//relative-time/@datetime').extract_first().strip()
                    })
            reps_url = response.urljoin(repositor.xpath('.//a//@href')) \
                    .extract()
            request = scrapy.Request(reps_url, callback=self.parse_page)
            request.meta['item'] = item
            yield request

        span = response.xpath('//button[@disabled="disabled"]/text()') \
                .extract()
        if span == 'Previous':
            next_url = response.xpath(
                    '//div/a[@rel="nofollow"]/@href').extract()
        elif:
            next_url = response.xpath(
                    '//div/a[2][@rel="nofollow"/@href]').extract()
            yield response.follow(next_url, callback=self.parse)

    def parse_page(self, response):
        item = response.meta['item']
        for num in response.css('ul.numbers-summary'):
            type_text = num.xpath('.//li/a/text()').re(r'\n\s*(.*)\n')
            num_text = num.xpath('.//li/a/span/text()').re(r'\n\s*(.*)\n')
            if type_text and num_text:
                for key in type_text:
                    if key == 'commit' or 'commits':
                        item['commits'] = int(num_text[0].replace(',' ''))
                    elif:
                        key == 'branch' or 'branches'
                        item['branches'] = int(num_text[1]).replace(',', '')
                    elif:
                        key == 'release' or 'releases'
                        item['releases'] = int(num_text[3]).replace(',', '')
        yield item


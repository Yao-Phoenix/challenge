#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import scrapy
from challenge16.items import Challenge16Item


class GithubSaveSpider(scrapy.Spider):
    name = 'github_save'
    
    @property
    def start_urls(self):
        url_list = [
                'http://github.com/shiyanlou?tab=repositories',
                'https://github.com/shiyanlou?after=Y3Vyc29yOnYyOpK0MjAxNy0wNi0wN1QwMDozMjo1OFrOBZKVFA%3D%3D&tab=repositories',
                'https://github.com/shiyanlou?after=Y3Vyc29yOnYyOpK5MjAxNS0wMi0xMFQxMzowODo0NyswODowMM4B0o4T&tab=repositories',
                'https://github.com/shiyanlou?after=Y3Vyc29yOnYyOpK5MjAxNC0xMi0wN1QyMjoxMTozNSswODowMM4Bpo1E&tab=repositories',
                'https://github.com/shiyanlou?after=Y3Vyc29yOnYyOpK5MjAxNC0xMC0xM1QxMToxNTo0NCswODowMM4Bf5tW&tab=repositories']
        return url_list

    def parse(self, response):
        for repositor in response.css('li.public'):
            item = Challenge16Item({
                    'name': repositor.xpath('.//a[@itemprop="name codeRepository"]/text()').extract_first().strip(), 
                    'update_time': repositor.xpath('.//relative-time/@datetime').extract_first().strip()
                    })
            yield item

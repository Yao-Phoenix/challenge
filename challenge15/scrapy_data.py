#!/usr/bin/env python3
import scrapy

class RepositoriesSpider(scrapy.Spider):

    name = 'respositories'

    def start_requests(self):
        url_list = [
                'https://github.com/shiyanlou?tab=repositories',
                'https://github.com/shiyanlou?after=Y3Vyc29yOnYyOpK0MjAxNy0wNi0wN1QwMDozMjo1OFrOBZKVFA%3D%3D&tab=repositories',
                'https://github.com/shiyanlou?after=Y3Vyc29yOnYyOpK5MjAxNS0wMi0xMFQxMzowODo0NyswODowMM4B0o4T&tab=repositories',
                'https://github.com/shiyanlou?after=Y3Vyc29yOnYyOpK5MjAxNC0xMi0wN1QyMjoxMTozNSswODowMM4Bpo1E&tab=repositories',
                'https://github.com/shiyanlou?after=Y3Vyc29yOnYyOpK5MjAxNC0xMC0xM1QxMToxNTo0NCswODowMM4Bf5tW&tab=repositories'
                ]
        for url in url_list:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        for repositor in response.css('li.public'):
            yield {
                    'name': repositor.xpath('.//a[@itemprop="name codeRepository"]/text()').extract_first().strip(),
                    'update_time': repositor.xpath('.//relative-time/@datetime').extract_first().strip()
                    }


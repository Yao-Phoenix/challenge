# -*- coding: utf-8 -*-
import scrapy
from items import RestaurantItem
from scrapy.spiders import Rule
from scrapy.linkextractors import LinkExtractor

class RestaurantsSpider(scrapy.spiders.CrawlSpider):
    name = 'restaurants'
    start_urls = ['http://www.dianping.com/chengdu/ch10']

    rules = (
            Rule(LinkExtractor(allow='http://www.dianping.com/chengdu/ch10/*'),
            callback='parse_restaurant',
            follow=True),)

    def start_requests(self):
        return [scrapy.Request('https://account.dianping.com/login?redir=http%3A%2F%2Fwww.dianping.com%2Fchengdu%2Fch10', meta={"cookiejar":1}, callback=self.parse_before_login)]

    def parse_before_login(self, response):
        return [FormRequest.form_response(response,
            meta = {'cookiejar' : response.meta['cookiejar']},
            headers = self.headers,
            formdata = {
                'user': '18852983022',
                'password': '53445248zxc'
                },
            callback = self.after_login,
            dont_filter = True)]

    def aftet_login(self, response):
        yield self.make_requests_from_url(start_urls)

    def parse_restaurant(self, response):
        pass

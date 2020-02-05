# -*- coding: utf-8 -*-
import scrapy, re
from items import JobItem
from scrapy.spiders import Rule
from scrapy.linkextractors import LinkExtractor

class JobsSpider(scrapy.spiders.CrawlSpider):
    name = 'jobs'
    start_urls = ['https://www.lagou.com/zhaopin/']
    
    rules = (
            Rule(LinkExtractor(allow='https://www.lagou.com/zhaopin/*'),
                callback='parse_job',
                follow=True),)

    def parse_job(self, response):
        for data in response.css('li.con_list_item'):
            experience = data.xpath("//div[@class='li_b_l']/text()").re_first(r'\S.*')
            experience = re.findall('\d+', experience)
            experience_list = experience if experience else [0, 0]
            experience_list = experience if len(experience) > 1 else [0, 1]
            if len(experience) == 1:
                experience_list = [0, 1]
            item = JobItem(
                    title = data.xpath('//h3/text()').extract_first(),
                    city = data.xpath('//em/text()').re_first(r'\w+'),
                    salary_lower = data.xpath(
                        '//span[@class="money"]/text()').extract_first().split('-')[0],
                    salary_upper = data.xpath(
                        '//span[@class="money"]/text()').extract_first().split('-')[1],
                    experience_lower = experience_list[0],
                    experience_upper = experience_list[1],
                    education = data.xpath(
                        "//div[@class='li_b_l']/text()"
                        ).re_first(r'\S.*').split('/')[1].strip(),
                    tags = ' '.join(data.css(
                        'div.list_item_bot span::text').extract()),
                    company = data.xpath(
                        "//div[@class='company_name']/a/text()"
                        ).extract_first().strip()
                    )
            yield item

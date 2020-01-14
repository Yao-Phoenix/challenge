#!/usr/bin/env python3

import scrapy

class CoursesSpider(scrapy.Spider):

    name = 'courses'

    start_urls = ['https://www.shiyanlou.com/bootcamp/']

    def parse(self, response):
        for course in response.css('div.bootcamp-course-item'):
            yield {
                'name': course.xpath(
                    './/div[@class="course-body"]/p/text()').extract_first().strip(),
                'description': course.xpath(
                    './/div[@class="course-body"]/p[2]/text()') \
                            .extract_first().strip(),
                'image_url': course.xpath(
                    './/div[@class="course-header relative"]/img/@src').extract_first()
                }


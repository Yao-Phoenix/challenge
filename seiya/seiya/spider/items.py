# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class JobItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    title = scrapy.Field()
    city = scrapy.Field()
    salary_lower = scrapy.Field()
    salary_upper = scrapy.Field()
    experience_lower = scrapy.Field()
    experience_upper = scrapy.Field()
    education = scrapy.Field()
    tags = scrapy.Field()
    company = scrapy.Field()

class HouseItem(scrapy.Item):
    plot = scrapy.Field()
    type = scrapy.Field()
    area = scrapy.Field()
    rent = scrapy.Field()

class RestaurantItem(scrapy.Item):
    name = scrapy.Field()
    score = scrapy.Field()
    count = scrapy.Field()
    consumption = scrapy.Field()
    sort = scrapy.Field()
    bussiness_district = scrapy.Field()
    taste = scrapy.Field()
    environment = scrapy.Field()
    seivice = scrapy.Field()

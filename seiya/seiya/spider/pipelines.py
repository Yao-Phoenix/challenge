# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
from job import Job
from base import engine, session
from sqlalchemy.orm import sessionmaker
from items import JobItem, HouseItem, RestaurantItem
from house import House
from restaurant import Restaurant

class SeiyaPipeline(object):

    def process_item(self, item, spider):
        if isinstance(item, JobItem):
            return self._process_job_item(item)
        elif isinstance(item, HouseItem):
            return self._process_house_item(item)
        else:
            return self._process_restaurant_item(item)

    def _process_job_item(self, item):
        item['salary_lower'] = int(item['salary_lower'][:-1])
        item['salary_upper'] = int(item['salary_upper'][:-1])
        item['experience_lower'] = int(item['experience_lower'])
        item['experience_upper'] = int(item['experience_upper'])
        session.add(Job(**item))
        session.commit()
        session.close()
        return item
    
    def _process_house_item(self, item):
        item['area'] = int(item['area'][:-1])
        item['rent'] = int(item['rent'])
        session.add(House(**item))
        session.commit()
        session.close()
        return item
    
    def _process_restaurant_item(self, item):
        pass       
        session.add(Restaurant(**item))
        session.commit()
        session.close()
        return item

    def close_spider(self, spider):
        session.commit()
        session.close()

#!/usr/bin/env python3
import json, time
from selenium import webdriver
from scrapy.http import HtmlResponse
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait

results = []

def parse(response):
    for comments in response.css('div.comment-item'):
        result = dict(
                username = comments.xpath(
                    './/a[@class="name"]/text()').extract_first().strip(),
                content = comments.xpath(
                    './/div[contains(@class, "content")]/text()') \
                            .extract_first().strip())
        print('comments: {}'.format(result))
        results.append(result)

def spider():
    driver = webdriver.Firefox()
    url = 'https://www.shiyanlou.com/courses/427'
    driver.get(url)
    while True:
        wait = WebDriverWait(driver, 1)
        html = driver.page_source
        response = HtmlResponse(url=url, body=html.encode())
        parse(response)
        
        if 'disabled' in response.xpath(
                '//li[contains(@class, "page-item")][2]/@class') \
                        .extract_first():
            break
        driver.find_element_by_xpath(
                '//li[contains(@class, "page-item")][2]').click()
    
    driver.quit()
    with open('comments.json', 'w') as f:
        json.dump(results, f)

if __name__ == '__main__':
    start = time.time()
    spider()
    print('Time: {:.2f}s'.format(time.time()-start))




import csv, asyncio, aiohttp
from scrapy.http import HtmlResponse
results = []

async def fetch(session, url):
    async with session.get(url) as response:
        return await response.text()

def parse(url, body):
    response = HtmlResponse(url=url, body=body)
    for repository in response.css('li.public'):
        name = repository.xpath('.//h3/a/text()').extract_first().strip(),
        update_time = repository.xpath('.//relative-time/@datetime').extract_first()
        results.append((name, update_time))

async def task(url):
    timeout = aiohttp.ClientTimeout(total=10)
    async with aiohttp.ClientSession(timeout=timeout) as session:
        html = await fetch(session, url)
        parse(url, html.encode('utf-8'))

def main():
    loop = asyncio.get_event_loop()
    url_list = ['https://github.com/shiyanlou?tab=repositories',
            'https://github.com/shiyanlou?after=Y3Vyc29yOnYyOpK5MjAxNy0wNi0wN1QwODozMjo1OCswODowMM4FkpUU&tab=repositories',
            'https://github.com/shiyanlou?after=Y3Vyc29yOnYyOpK5MjAxNS0wMi0xMFQxMzowODo0NyswODowMM4B0o4T&tab=repositories',
            'https://github.com/shiyanlou?after=Y3Vyc29yOnYyOpK5MjAxNC0xMi0wN1QyMjoxMTozNSswODowMM4Bpo1E&tab=repositories',
            'https://github.com/shiyanlou?after=Y3Vyc29yOnYyOpK5MjAxNC0xMC0xM1QxMToxNTo0NCswODowMM4Bf5tW&tab=repositories']
    tasks = [task(url) for url in url_list]
    loop.run_until_complete(asyncio.gather(*tasks))
    with open('shiyanlou-repos.csv', 'w', newline='') as f:
        writer = csv.writer(f)
        writer.writerows(results)

if __name__ == '__main__':
    main()

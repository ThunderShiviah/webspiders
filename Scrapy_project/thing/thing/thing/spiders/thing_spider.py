
from scrapy import log # This module is useful for printing out debug information
from scrapy.spider import BaseSpider #should I use BaseSpider instead?
from scrapy.selector import Selector
import re #imports regular expressions
from thing.items import ThingItem

#scrapy crawl thing -o itemsThing.json

class ThingSpider(BaseSpider):     #should this be BaseSpider?
    scrape_number = 1000
    name = "thing"
    allowed_domains = ["http://www.thingiverse.com"]
    start_urls = [
        "http://www.thingiverse.com/thing:%d" %n for n in range(1,scrape_number)
    ]
    print start_urls
    def parse(self, response):
        sel =  Selector(response)
       # sites = []
       # for site in sites:

    
        items = []
        item = ThingItem()
        item['title'] =  sel.xpath('//div[@class="thing-header-data"]/h1/text()')[0].extract()
        item['maker'] = sel.xpath('//div[@class="thing-header-data"]/h2/a/text()')[0].extract()
        item['datePublished'] = sel.xpath('//div[@class="thing-header-data"]/h2/time').extract()
        item['likes'] = sel.xpath('//span[@class="interaction-count"]/text()')[0].extract()
        item['collect'] = sel.xpath('//span[@class="interaction-count collection-count"]/text()')[0].extract()
        item['comments'] = sel.xpath('//div[@class="value"]/text()')[0].extract()
        item['made'] = sel.xpath('//div[@class="value"]/text()')[1].extract()
        item['connections'] = sel.xpath('//div[@class="value"]/text()')[2].extract()
        item['remix'] = sel.xpath('//div[@class="value"]/text()')[3].extract()
        item['views'] = sel.xpath('//span[@class="interaction-count"]/text()')[5].extract()
        item['downloads'] = sel.xpath('//span[@class="interaction-count"]/text()')[6].extract()
        items.append(item)

        return items     
    
 

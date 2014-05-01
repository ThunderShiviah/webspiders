from scrapy.spider import BaseSpider
from scrapy.selector import Selector
import re
from tutorial.items import lbpItem

class lbpSpider(BaseSpider):
    name = "lbp"
    allowed_domains = ["http://lbp.me"]
    start_urls = [
        "http://lbp.me/search?q="
    ]

    def parse(self, response):
        sel = Selector(response)
        sites = sel.xpath('//div[@class = "event-details"]/h3/a/@href').extract()
        items = []
        
        item = lbpItem()
        item['creator'] = sel.xpath('//p[@class="level-creator"]/a/@href').extract()
        item['title'] = sel.xpath('//div[@class="event-details"]/h3/a/text()').extract()
       # item['thumbsup'] = sel.xpath('//ul[@class="feedback clearfix"]/li')[0].extract()
        item['thumbsup_num'] = sel.xpath('//ul[@class="feedback clearfix"]/li[@class="thumbsup"]/text()').extract()
        # item['hearted'] = sel.xpath('//ul[@class="feedback clearfix"]/li')[1].extract()
        item['hearted_num'] = sel.xpath('//ul[@class="feedback clearfix"]/li[@class="hearted"]/text()').extract()
           # item['played'] = sel.xpath('//ul[@class="feedback clearfix"]/li')[2].extract()
        item['played_num'] = sel.xpath('//ul[@class="feedback clearfix"]/li[@class="plays"]/text()').extract()
           # item['published'] = sel.xpath('//ul[@class="feedback clearfix"]/li')[3].extract()
        item['published_num'] = sel.xpath('//ul[@class="feedback clearfix"]/li[@class="listed"]/text()').extract()
        item['first_published'] = sel.xpath('//div[@id="moar-info"]/ul/li/text()').extract()

        items.append(item)
        return items




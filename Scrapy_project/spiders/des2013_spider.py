from scrapy.spider import BaseSpider
from scrapy.selector import Selector
from tutorial.items import DesItem
"""This spider returns title, designer name, number of votes, and score for either a printed or not printed design from threadless.com. 
Output is stored in itemsDes.json in the directory where the spider was run."""



"""To run: scrapy crawl des -o items.json -t json"""
class des_Spider(BaseSpider):
   name = "des"
   allowed_domains = ["threadless.com"]
   start_urls = [
   "http://www.threadless.com/thebiglebowski/you-said-it-man-2/", ###the big lebowski is an example of a NOT printed design
  # "http://www.threadless.com/product/4762/Birth_of_a_Legend" ###The birth of a legend is an example of a printed design.
   ]

   def parse(self, response):
       sel = Selector(response)
       ############ Printed designs #####################
       """When used with a url of the form http://www.threadless.com/product/[product_number]/[title]
       will return correct info for votes, designer, score, and title"""

       # sites = site.xpath('//a[contains(@href, "product")]/@href')
       items = []
       item = DesItem()
       """item['title'] = sel.xpath('//h1/text()').extract() ###Remove the quote marks (and add them to the Not printed design items) when running printed designs.
       # item['titleNum'] =
       # item['desNum'] = 
       item['designer'] = sel.xpath('//p[@class = "img_container"]/a/@href').extract()
       item['votes'] =sel.xpath('//dl/dd[2]/text()').extract()
       item['score'] =  sel.xpath('//dl/dd[1]/text()').extract()"""
       ############## Not Printed Designs ###################################
       """When used with a url of the form http://www.threadless.com/[special_design(i.e. the big lebowski)]/[title]/
       will return correct info for votes, designer, score, and title"""

       item['s_title'] = sel.xpath('//h2/text()')[0].extract()
       item['s_designer'] =  sel.xpath('//*[@class="intro"]/a/@href').extract()
       item['s_votes'] = sel.xpath('//ul/li/strong/text()')[1].extract()
       item['s_score'] =  sel.xpath('//ul/li/strong/text()')[0].extract()
       
       items.append(item)


        # for site in sites:
          # item = DesItem()
          # item['score'] =  site.xpath('//dl/dd[1]/text()').extract()
           
           # item['link'] = site.xpath('a/@href').extract()
           # item['desc'] = site.xpath('text()').extract()
          # items.append(item)  
       return items
      


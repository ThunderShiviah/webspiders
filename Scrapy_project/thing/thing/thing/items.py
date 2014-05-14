# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

from scrapy.item import Item, Field

class ThingItem(Item):
    # define the fields for your item here like:
    # name = Field()
    # pass
     title = Field()
     maker = Field()
     datePublished = Field()
     likes = Field()
     collect = Field()
     comments = Field()
     made = Field()
     connections = Field()
     remix = Field()
     views = Field()
     downloads = Field()


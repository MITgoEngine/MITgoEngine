# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class MitmediaItem(scrapy.Item):
    # define the fields for your item here like:
    Title = scrapy.Field()
    Date = scrapy.Field()
    Authors = scrapy.Field()
    Abstract = scrapy.Field()
    Keywords = scrapy.Field()
    URL = scrapy.Field()
    DownloadURL = scrapy.Field()
    OfficialURL = scrapy.Field()



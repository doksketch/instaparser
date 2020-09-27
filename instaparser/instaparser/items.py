# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy

class InstaparserItem(scrapy.Item):
    # define the fields for your item here like:
    _id = scrapy.Field()
    user_name = scrapy.Field()
    full_name = scrapy.Field()
    photo = scrapy.Field()
    insert_to_collection = scrapy.Field()


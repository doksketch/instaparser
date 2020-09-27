# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from scrapy.pipelines.images import ImagesPipeline
import scrapy
from pymongo import MongoClient


class InstagramPhotosPipeline(ImagesPipeline):

    def get_media_requests(self, item, info):
        if item['photo']:
            try:
                yield scrapy.Request(item['photo'], meta=item)
            except Exception as e:
                print(e)

    def item_completed(self, results, item, info):
        if results:
            item['photo'] = results[0][1] if results[0][0] else None
        return item


class DataBasePipeline:

    def __init__(self):
        self.client = MongoClient('localhost', 27017)
        self.mongodb = self.client.instagram

    def __del__(self):
        self.client.close()

    def process_item(self, item, spider):

        collection = item['insert_to_collection']
        del item['insert_to_collection']

        if self.mongodb[collection].count_documents({'_id': item['_id']}) == 0:
            self.mongodb[collection].insert_one(item)

        return item

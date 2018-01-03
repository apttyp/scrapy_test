# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
import pymongo
# import settings
from .settings import MONGO_URI
from .settings import MONGO_DB

class TttPipeline(object):
    # def process_item(self, item, spider):
    #     return item

    ##example1:save to txt
    # def process_item(self, item, spider):
    # 	with open('res.txt', 'w', encoding='utf-8') as f:
    # 		words = item['words']
    # 		author = item['author']
    # 		for i,j in zip(words, author):
    # 			f.write(i+ ':' + j + '\n')
    # 	return item

    collection = 'quotes'

    def __init__(self, mongo_uri, mongo_db):
    	self.mongo_uri = mongo_uri
    	self.mongo_db = mongo_db

    @classmethod
    def from_crawler(cls, crawler):
    	return cls(
                mongo_uri = crawler.settings.get('MONGO_URI'),
                mongo_db = crawler.settings.get('MONGO_DB')
    	)
    def open_spider(self, spider):
    	self.client = pymongo.MongoClient(self.mongo_uri)
    	self.db = self.client[self.mongo_db]

    def close_spider(self, spider):
    	self.client.close()

    def process_item(self, item, spider):
    	words = item['words']
    	author = item['author']
    	# table = self.db[self.collection]
    	db = self.client.collection
    	for i,j in zip(words, author):
    		data = {}
    		data['words&author'] = i + '&' + j
    		db.col.insert(data)
    	return item
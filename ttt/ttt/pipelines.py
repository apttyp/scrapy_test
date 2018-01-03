# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html


class TttPipeline(object):
    # def process_item(self, item, spider):
    #     return item

    def process_item(self, item, spider):
    	with open('res.txt', 'w', encoding='utf-8') as f:
    		words = item['words']
    		author = item['author']
    		for i,j in zip(words, author):
    			f.write(i+ ':' + j + '\n')
    	return item
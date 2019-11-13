# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html

import codecs


class PafjPipeline(object):
    def __init__(self):
        self.houseList = []
        self.cityInfo = {}
        self.file=codecs.open(filename='fj.json',mode='w+',encoding='utf-8')

    def open_spider(self, spider):
        print('房价爬虫开始了...')
        pass

    def process_item(self, item, spider):
        print('进入房间爬虫信息处理阶段...')
        self.houseList.append(item)
        item['auth'] = 'gq'
        return item

    def close_spider(self, spider):
        print('房价爬虫结束。。。。')
        self.cityInfo[self.houseList[0]['city']] = self.houseList
        self.file.write(str(self.cityInfo))
        self.file.close()


class CityPipeline(object):
    def __init__(self):
        self.cityList = []
        self.file = codecs.open(filename='city.json',mode='w+',encoding='utf-8')

    def open_spider(self, spider):
        print('城市爬虫开始了...')
        pass

    def process_item(self, item, spider):
        self.cityList.append(item['name'])
        return item

    def close_spider(self, spider):
        print('城市爬虫结束。。。。')
        self.file.write(str(self.cityList))
        self.file.close()
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


    def open_spider(self, spider):
        print('房价爬虫开始了...')
        pass

    def process_item(self, item, spider):
        print('进入房间爬虫信息处理阶段...')
        self.houseList.append(item)
        return item

    def close_spider(self, spider):
        print('房价爬虫结束。。。。')
        fileName = self.houseList[0]['city']
        file = codecs.open(filename=(fileName+'.json'), mode='w+', encoding='utf-8')
        self.cityInfo[fileName] = self.houseList
        file.write(str(self.cityInfo))
        file.close()


class CityPipeline(object):
    def __init__(self):
        self.myJson = {}
        self.file = codecs.open(filename='city.json',mode='w+',encoding='utf-8')

    def open_spider(self, spider):
        print('城市爬虫开始了...')
        pass

    def process_item(self, item, spider):
        self.myJson[item['name']] = item['cityKey']
        return item

    def close_spider(self, spider):
        print('城市爬虫结束。。。。')
        self.file.write(str(self.myJson))
        self.file.close()
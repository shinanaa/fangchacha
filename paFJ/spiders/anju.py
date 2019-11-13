# -*- coding: utf-8 -*-
import random
import scrapy
from paFJ.items import PafjItem  # 使用item

class AnjuSpider(scrapy.Spider):
    name = 'anjuke'  # spider的名称，影响不大
    allowed_domains = ['anjuke.com']  # 允许爬取的域，为空则是允许当前spider爬取所有的域名
    start_urls = ['https://heb.anjuke.com/community/p50/']
    USER_AGENT_LIST = [
        'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.100 Safari/537.36',
        'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.87 Safari/537.36'
    ]
    custom_settings = {
        "USER_AGENT": random.choice(USER_AGENT_LIST),
        'ITEM_PIPELINES': {'paFJ.pipelines.PafjPipeline': 300}
    }
    def parse(self, response):
        # 获取 【哈尔滨】
        city = response.xpath('//div[@class="sortby"]/span[@class="tit"]/em/text()').extract()[0]  # 使用xpath从response中获取需要的html块
        print('获取的城市是%s' %city)
        # item['city'] = city
        div_item_list = response.xpath('//div[@class="li-itemmod"]')  # 使用xpath从response中获取需要的html块
        for div in div_item_list:
            name = div.xpath('./div[@class="li-info"]/h3/a/text()').extract()  # 名字
            money = div.xpath('./div[@class="li-side"]/p[1]/strong/text()').extract() # 钱
            trend = div.xpath('./div[@class="li-side"]/p[2]/text()').extract() # 趋势
            # photo = div.xpath('./a[@class="img"]/img/@src').extract() # 图片
            item = PafjItem()
            item['name'] = name
            item['money'] = money
            item['trend'] = trend
            # item['photo'] = photo
            item['city'] = city
            yield item
            # print('获取的城市是%s,小区名%s,房价%s,图片%s,趋势%s' % (city,name,money,photo,trend))
        next_ = response.xpath('//a[@class="aNxt"]/@href').extract_first()  # 获取下一页的链接
        if next_ :
           yield response.follow(url=next_, callback=self.parse)
        # yield response.follow(url=next_, callback=self.parse)  # 将下一页的链接加入爬取队列~~
        # yield response.follow(url='https://heb.anjuke.com/community/p2/', callback=self.parse)  # 将下一页的链接加入爬取队列~~

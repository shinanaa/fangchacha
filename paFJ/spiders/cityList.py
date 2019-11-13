# -*- coding: utf-8 -*-
import random
import scrapy
from paFJ.items import cityItem  # 使用item


class CityListSpider(scrapy.Spider):
    name = 'cityList'  # spider的名称，影响不大
    allowed_domains = ['anjuke.com']  # 允许爬取的域，为空则是允许当前spider爬取所有的域名
    start_urls = ['https://www.anjuke.com/sy-city.html']
    USER_AGENT_LIST = [
        'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.100 Safari/537.36',
        'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.87 Safari/537.36'
    ]
    custom_settings = {
        "USER_AGENT": random.choice(USER_AGENT_LIST),
        'ITEM_PIPELINES': {'paFJ.pipelines.CityPipeline': 300}
    }

    def parse(self, response):
        # 获取 城市列表
        cityList = response.xpath('//div[@class="city_list"]')  # 使用xpath从response中获取24个字母的列表
        for div in cityList:
            names = div.xpath('./a/@href').extract()  # 名字
            for name in names:
                # https://xa.anjuke.com/community/p1/
                cityKey = 'https://%s.anjuke.com/community/p1/' % name.split(".", 1)[0][8:]
                item = cityItem()
                item['name'] = cityKey
                yield item
            # print('获取的城市是%s,小区名%s,房价%s,图片%s,趋势%s' % (city,name,money,photo,trend))
        # next_ = response.xpath('//a[@class="aNxt"]/@href').extract_first()  # 获取下一页的链接
        # if next_ :
        #    yield response.follow(url=next_, callback=self.parse)
        # yield response.follow(url=next_, callback=self.parse)  # 将下一页的链接加入爬取队列~~
        # yield response.follow(url='https://heb.anjuke.com/community/p2/', callback=self.parse)  # 将下一页的链接加入爬取队列~~

# -*- coding: utf-8 -*-
import random
import scrapy
from paFJ.items import CityItem, PafjItem  # 使用item
from scrapy import Request
import codecs

class CityListSpider(scrapy.Spider):
    name = 'cityList'  # spider的名称，影响不大
    allowed_domains = ['anjuke.com']  # 允许爬取的域，为空则是允许当前spider爬取所有的域名
    start_urls = ['https://www.anjuke.com/sy-city.html']
    USER_AGENT_LIST = [
        'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.100 Safari/537.36'
        # 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.100 Safari/537.36',
        # 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.87 Safari/537.36'

    ]
    custom_settings = {
        "USER_AGENT": random.choice(USER_AGENT_LIST),
        'ITEM_PIPELINES': {'paFJ.pipelines.CityPipeline': 300}
    }

    def parse(self, response):
        # 获取 城市列表
        key = 'C'
        # 如开启27行 则爬取 city页面所有的650个省份  如果使用28行 则根据22行对应的key 获取省份列表
        cityList = response.xpath('//div[@class="city_list"]')  # 使用xpath从response中获取24个字母的列表
        # cityList = response.xpath('//label[@class="label_letter" and contains(text(),"%s")]/following-sibling::div[@class="city_list"]' % key)  # 使用xpath从response中根据我设定的Key 获取 对应首字母的div
        for div in cityList:
            # names = div.xpath('./a/@href').extract()  # 名字
            aS = div.xpath('./a')  # 名字
            for a in aS:
                href = a.xpath('./@href').extract_first()  # href
                name = a.xpath('./text()').extract_first()  # href
                # https://xa.anjuke.com/community/p1/
                cityKey = 'https://%s.anjuke.com/community/p1/' % href.split(".", 1)[0][8:]
                ct = CityItem()
                ct['cityKey'] = cityKey
                ct['name'] = name
                yield ct


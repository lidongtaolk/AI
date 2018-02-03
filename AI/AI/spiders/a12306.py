# -*- coding: utf-8 -*-
import scrapy
from scrapy.selector import Selector
from AI.items import AiItem
import json

class A12306Spider(scrapy.Spider):
    name = 'a12306'
    allowed_domains = ['dynamic.12306.cn']
    start_urls = ['http://dynamic.12306.cn/otn/board/query']

    def parse(self, response):
        str=json.loads(response.body_as_unicode())
        item=AiItem()
        for n in range(0,159):
            item[u'start']=str[u'data'][u'values'][n][u'from_station_telecode_name']
            item[u'dest']=str[u'data'][u'values'][n][u'to_station_telecode_name']
            item[u'date3']=str[u'data'][u'values'][n][u'values'][u'20180203']
            item[u'date4']=str[u'data'][u'values'][n][u'values'][u'20180204']
            item[u'date5']=str[u'data'][u'values'][n][u'values'][u'20180205']
            item[u'date6']=str[u'data'][u'values'][n][u'values'][u'20180206']
            yield item
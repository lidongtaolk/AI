# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class AiItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    start=scrapy.Field()
    dest=scrapy.Field()
    date3=scrapy.Field()
    date4=scrapy.Field()
    date5=scrapy.Field()
    date6=scrapy.Field()
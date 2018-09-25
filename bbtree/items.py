# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class BbtreeItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    tree01 = scrapy.Field()
    tree02 = scrapy.Field()
    tree03 = scrapy.Field()
    article_url = scrapy.Field()
    article_name = scrapy.Field()
    article_read_num = scrapy.Field()
    article_key_words = scrapy.Field()
    article_discuss_number = scrapy.Field()



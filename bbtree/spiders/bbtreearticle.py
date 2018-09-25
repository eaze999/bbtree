# -*- coding: utf-8 -*-
import scrapy


class BbtreearticleSpider(scrapy.Spider):
    name = 'bbtreearticle'
    allowed_domains = ['babytree.com']
    start_urls = ['http://babytree.com/']

    def parse(self, response):
        pass

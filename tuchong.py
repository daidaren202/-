# -*- coding: utf-8 -*-
import scrapy
from scrapy import Request
import scrapy.spiders
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor
import requests
from items import TuchongItem
import re
from selenium import webdriver
import time
class Spider(CrawlSpider):
    name = 'tuchong'
    allowed_domains = ['tuchong.com']
    start_urls = [#'https://tuchong.com/categories/location/',
                  'https://tuchong.com/categories/subject/',
                  #'https://tuchong.com/categories/equipment/'
                  ]
    img_urls = []
    rules = (
        Rule(LinkExtractor(allow=('https://tuchong.com/tags/(%[A-Z0-9]{2}){0,10}',)),
             callback='parse_tags', follow=False),
        Rule(LinkExtractor(allow=('https://tuchong.com/tags/.{0,25}',)), callback='parse_single', follow=False),
        Rule(LinkExtractor(allow=('https://tuchong.com/tags.{0,25}',)), callback='parse_test', follow=False),
        Rule(LinkExtractor(), callback='parse_default', follow=False),
    )


    def parse_tags(self, response):
        """
        :param response: 下载器返回的response
        :return:
        """
        print response

        pass

    def parse_single(self, response):
        print 123
        print response
        pass

    def parse_test(self, response):
        print 'test'
        pass

    def parse_default(self, response):
        print 'default'
        print response
        pass


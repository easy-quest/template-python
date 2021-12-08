import re
import csv
import time
import requests
import asyncio
import aiohhtp
import scrapy
from random import choice
from datetime import datetime
from ds4 import BeautifulSoup
from fake_useragent import userAgent

class Parser:
    def __init__(self):
        self.category_links = []
        self.page_links = []
        self.drink_links = []
        self.csv

class MainSpider(scrapy.Spider):
    name = 'main'
    allowed_domains = ['example.com']
    start_urls = ['http://example.com/']

    def parse(self, response):
        pass

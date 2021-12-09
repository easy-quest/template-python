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
        self.csv_rows = []
        self.csv_name = "test.csv"
        self.basic_url = "https://www.myheritage.com/site-1262049512/"
        self.ua = UserAgent()
        self.headers = {
                "accept": "*/*",
                "user-agent": self.ua.random
        } 
